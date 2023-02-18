# Frontiers-Boss-Music-Replacer

Allows easy modification of boss music in Sonic Frontiers
-By CoolguyTC

Github page: https://github.com/CoolguyTC/Frontiers-Boss-Music-Replacer

Prerequisites:

Any audio editing tool e.g. Audacity
Foobar2000 with the VGMstream plugin
Eternity Audio Tool

Tutorial:

1. Locate the music that you want to replace. It will be located within the directory "SonicFrontiers\image\x64\raw\sound", will start with "bgm_", will include boss/miniboss in the title and will have one .ACB and one .AWB file. Open up Foobar2000 and drag the .AWB file onto the window. From here you can preview the individual tracks within the file as well as view their lengths and other info. Once your certain this is the file you want to mod, copy and paste the .ACB and .AWB file into a folder outside of the game's directory.

2. Create the audio
You can create your own audio tracks using any audio editing program e.g. Audacity. Audio needs to be exported as a .WAV at 48000HZ. Before naming your exported audio files it is important that you open up Eternity Audio Tool use it to open your copied .ACB file. Doing this you can see the correct order of the tracks as they are stored in the game files. Make sure to name each track the track ID that is displayed. (You can use Foobar2000 to help figure out which tracks are which but remember Foosbar2000 will occasionally show tracks in the wrong order)

3. Using Eternity Audio Tool to replace tracks
In Eternity Audio Tool, with your copied .acb file open, select a track that you want to replace and choose the .WAV file with the same ID. Just to be safe hit "Don't loop" when given the option (Don't worry your track will still loop if it needs to). Once each track you want modded has been replaced make sure to save and you can now close Eternity Audio Tracker and Foobar2000 if you still have them open.

4. The final step!
You should now have a folder containing a .ACB file, .AWB file and each of your named .WAV files. Just double check that everything is set and there is nothing else in that folder before continuing. (This step will require the original .ACB file to be intact withing it's original directory. Basically as long as you haven't overwritten or deleted it your good). Now the easy part, simply drag and drop the coppied .AWB file onto "frontiers_boss_music_replacer.exe" and wait for it to finish. Assuming you didn't get any errors (Check "I got an error!" section below) your .ACB and .AWB files are complete! Drag and drop them into the same location you got them from (Making sure to make a backup of the originals of course) or more preferably make your own HedgeMod mod.


I got an error!

This program is has not been tested on every file so bugs may exist. If you encounter any bugs first ensure you followed the steps in the tutorial correctly, then contact me by leaving a comment on the tool's Gamebanana page: LINK