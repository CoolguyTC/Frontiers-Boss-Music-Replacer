import sys
import os
import binascii as ba
import wave

class MusicReplacer:
    def __init__(self, mod_dir, current_dir):
        self.mod_dir = mod_dir
        self.ACB_file_path = mod_dir + ".acb"
        self.AWB_file_path = mod_dir + ".awb"
        self.current_dir = current_dir
        self.frontiers_dir = ""

        if os.path.exists(os.path.join(current_dir, "config.ini")):
            self.read_config()
        else:
            self.create_config()

        file = open(self.ACB_file_path, "rb")
        self.ACB_file = ba.hexlify(file.read())
        file = open(self.AWB_file_path, "rb")
        self.AWB_file = ba.hexlify(file.read())
        file = open(self.get_original_file_path(), "rb")
        self.original_ACB_file = ba.hexlify(file.read())

        self.original_times = []
        self.new_times = []
        self.original_time_offsets = []
        self.get_time_data()

        print("Successfully read time data from .acb and .wav files")

    def get_original_file_path(self): # returns the path of the unmodified .acb file from the game directory
        file_name = os.path.basename(self.ACB_file_path)
        search_folder = os.path.join(self.frontiers_dir, "image\\x64\\raw\\sound")

        for root, dirs, files in os.walk(search_folder): # only saves first instance of the file
            if file_name in files:
                file_path = os.path.join(root, file_name)
                print('File found at:', file_path)
                break

        return file_path

    def read_config(self): # sets values from config.ini
        settings = open(os.path.join(self.current_dir, "config.ini"), "r").readlines()
        
        for setting in settings:
            temp_setting = setting.split("=")
            match temp_setting[0]:
                case "GameDir":
                    self.frontiersDir = temp_setting[1]

        print("Read config from " + os.path.join(self.current_dir, "config.ini") + "\n")

    def create_config(self): # creates a new config.ini
        print("Enter Sonic Frontier's base directory:")
        user_input = input()
        if os.path.exists(os.path.join(user_input, "SonicFrontiers.exe")):
            self.frontiers_dir = user_input

        file = open(os.path.join(self.current_dir, "config.ini"), "w")
        file.write("GameDir=" + self.frontiers_dir)

        file.close()
        print("Wrote config to " + os.path.join(self.current_dir, "config.ini") + "\n")

    def changes(self): # commits necessary changes locally
        self.original_ACB_file = self.replace_HCA_segments()
        self.original_ACB_file = self.replace_timestamps()
        self.original_ACB_file = self.replace_AFS2_segment()

    def find_HCA_offsets(self, hex_list): # locates each offset containing 48 43 41 00 followed shortly by 66 6D 74
        hex_offsets = []
        header = b'48434100'
        footer = b'666d74'
        start = 0

        while True:
            index = hex_list.find(header, start)
            if index == -1:
                break
            
            start = index + 1
            if index + 16 == hex_list.find(footer, start):
                hex_offsets.append(index // 2)
            
        return hex_offsets

    def replace_HCA_segments(self): # copies each corresponding 48 43 41 00 of length 0x1460 from .awb to .acb
        ACB_HCA_offsets = self.find_HCA_offsets(self.original_ACB_file)
        AWB_HCA_offsets = self.find_HCA_offsets(self.AWB_file)

        ACB_file = ba.unhexlify(self.original_ACB_file)
        AWB_file = ba.unhexlify(self.AWB_file)
        
        segment_size = 5216
        index = 0
        while index < len(ACB_HCA_offsets) - 1: # iterates through each HCA offset
            ACB_file = ACB_file[:ACB_HCA_offsets[index]] + AWB_file[ACB_HCA_offsets[index]:ACB_HCA_offsets[index] + segment_size] + ACB_file[ACB_HCA_offsets[index] + segment_size:]
            print("Replaced .acb HCA segment (" + hex(ACB_HCA_offsets[index]) + ") with .awb HCA segment (" + hex(AWB_HCA_offsets[index]) + ")")
            index += 1
        
        return ba.hexlify(ACB_file)

    def replace_AFS2_segment(self): # copies the corresponding 41 46 53 32 segment of length 0x5C from .awb to .acb
        ACB_file = ba.unhexlify(self.original_ACB_file)
        AWB_file = ba.unhexlify(self.AWB_file)
        segmentSize = 92

        ACB_file = ACB_file[:len(ACB_file) - segmentSize] + AWB_file[:segmentSize] # predefined offset of 92 bytes
        print("Replaced .acb AFS2 Segment")

        return ba.hexlify(ACB_file)

    def get_time_data(self): # saves timing and offset data from .awb and .acb files
        original_times = self.get_track_lengths(self.original_ACB_file)
        #newTimes = self.getTrackLengths(self.ACBFile)
        new_times = self.get_WAV_durations(original_times)
        # gets duration in milliseconds of default and modified tracks
        
        original_offsets = []
        index = 0
        while index < len(original_times):
            original_offsets.append(self.get_time_offsets(index, original_times[index]))
            index += 1
        # retrieves multiple offsets for each track

        self.original_times = original_times
        self.new_times = new_times
        self.original_time_offsets = original_offsets
        print("Found track lengths")

    def get_track_lengths(self, file): # gets the track lengths and ids from the default .acb file
        track_lengths = []
        header = b'547261636b4576656e7400436f6d6d616e64' # TrackEvent.Command
        hex_subseq = b'07d104' # before each time prepended by track number

        start = 0
        start = file.find(header, start)

        while True: # iterates through the .acb file recording track durations found
            index = file.find(hex_subseq, start)
            if index == -1:
                break
            index += 6
            start = index + 1
            track_lengths.append(int.from_bytes(ba.unhexlify(file[index:(index) + 8]), byteorder='big'))
        
        return track_lengths

    def get_time_offsets(self, id, time): # returns a list of default offsets for a given track
        time_offsets = []
        time_bytes = ba.hexlify(time.to_bytes(4, byteorder='big', signed=False))

        start = 0
        header = b'547261636b4576656e7400436f6d6d616e64' # TrackEvent.Command
        hex_subseq = ba.hexlify(id.to_bytes(1, byteorder='big', signed=False)) + b'07d104' + time_bytes # TrackEvent.Command formatting
        start = self.original_ACB_file.find(header, start)
        index = self.original_ACB_file.find(hex_subseq, start)
        index += 8
        time_offsets.append(index // 2)

        start = 0
        header = b'010b300000012100' # ControlWorkArea2 approx header
        hex_subseq = ba.hexlify((id + 4).to_bytes(2, byteorder='big', signed=False)) + time_bytes + b'00' # ControlWorkArea2 formatting
        start = self.original_ACB_file.find(header, start)
        index = self.original_ACB_file.find(hex_subseq, start)
        index += 4
        time_offsets.append(index // 2)

        return time_offsets

    def replace_timestamps(self): # replaces each vanilla song length in the .acb file with its modded counterpart
        index = 0
        ACB_file = ba.unhexlify(self.original_ACB_file)
        while index < len(self.original_times): # iterates through each individual replacement
            for offset in self.original_time_offsets[index]:
                ACB_file = ACB_file[:offset] + self.new_times[index].to_bytes(4, byteorder='big', signed=False) + ACB_file[offset + 4:]
                print("Replaced track length " + str(self.original_times[index]) + "ms with " + str(self.new_times[index]) + "ms at offset " + hex(offset))
            index += 1
        
        return ba.hexlify(ACB_file)

    def write_ACB_file(self): # writes changes to the .acb file 
        file = open(self.ACB_file_path, "wb")
        file.write(ba.unhexlify(self.original_ACB_file))
        print("Successfully wrote changes to " + self.ACB_file_path)

    def get_WAV_durations(self, original_times): # returns a list of track durations in milliseconds
        extention = ".wav"
        search_folder = os.path.dirname(self.mod_dir)
        new_times = original_times.copy()

        for root, dirs, files in os.walk(search_folder): # locates all correctly formatted .wav files
            for file in files:
                if file.endswith(extention):
                    print(os.path.join(search_folder, file))
                    try:
                        new_times[int(file[:5])] = self.get_WAV_ms(os.path.join(search_folder, file))
                    except:
                        print("Invalid filename '" + file + "'")

        return new_times
    
    def get_WAV_ms(self, filename): # finds the duration in milliseconds of a .wav file
        with wave.open(filename, 'rb') as wav_file:
            frames = wav_file.getnframes()
            frame_rate = wav_file.getframerate()

            duration_sec = frames / float(frame_rate)
            duration_ms = int(duration_sec * 1000)
            
            return duration_ms

def main(file_path):
    current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # testing
    music_replacer = MusicReplacer(os.path.splitext(file_path)[0], current_dir)
    music_replacer.changes()
    music_replacer.write_ACB_file()

    print("\nYou should be good to go!")