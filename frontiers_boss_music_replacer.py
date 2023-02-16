import sys
import os
import music_replacer as mr

def main():
    if len(sys.argv) > 1:
        file_name = os.path.splitext(sys.argv[1])
        if (file_name[1] == ".awb"):
            if os.path.exists(file_name[0] + ".acb"):
                mr.main(sys.argv[1])
            else:
                print("Corresponding .acb file not found!")
        else:
            print("File was not a .awb file!")
        input()


if __name__ == '__main__':
    #mr.main("F:\Modding\Sonic Frontiers Modding\My Mods\Its Art over Im with you\\bgm_lastboss.awb")
    main()