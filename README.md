# Frontiers-Boss-Music-Replacer

-By CoolguyTC

Allows easy modification of boss music in Sonic Frontiers.<br/>
Applicable tracks will start with **"bgm_boss"** or **"bgm_miniboss"**.<br/>
For any other sound/music check out [Acrolo's guide](https://gamebanana.com/tuts/15462).<br/>

<br/>

**Build Instructions:**

Clone the repository and open CMD in its location.<br/>
Make sure you have Pyinstaller and run the command **"pyinstaller --onefile --icon=BossMusicReplacer.ico frontiers_boss_music_replacer.py"**<br/>
Once done move the .exe from /dist to the base folder and you can delete the generated /build, /dist and .spec<br/>

<br/>

<br/>

## <u>**Tutorial:** </u>

<br/>

**You Need:**

Any audio editing tool e.g. [Audacity](https://www.audacityteam.org/download/)  
[Foobar2000](https://www.foobar2000.org/download) with the [VGMstream plugin](https://github.com/vgmstream/vgmstream/releases/)  
[Eternity Audio Tool](https://mega.nz/file/W5NHxDYD#IM7xirUu1-K8e34lINmgC3MFqG1OWFTuscbSptK5fRw)  
This tool

<br/>

**Steps:**

**1.** Locate the music that you want to replace. It will be located within a subfolder in your game's directory "SonicFrontiers\image\x64\raw\sound".

![](https://i.imgur.com/fKXbBW1.png)  
Copy the applicable .ACB and .AWB files to a new folder somewhere on your PC.  

![](https://i.imgur.com/tXZkqiY.png)  
**[Already made your audio files? Skip to step 4]**

<br/>

**2.** Open up Foobar and drag the .AWB file onto the window. From here you can preview the individual tracks within the file as well as view their lengths and other info. This will be useful when creating your own tracks.

<br/>

**3.** You can create your own audio tracks using any audio editing program but for the sake of this tutorial I will be using Audacity.

Make sure any tracks that loop in-game will loop cleanly. Also if you edit a major bosses' ending track ensure that the music climaxes/ends at around the same time that the base track finishes (failing to do so won't cause any errors but it will most likely not line up with the boss' death cutscene).

Once you're happy with your tracks export your audio as a .WAV at 48000HZ.  
![](https://i.imgur.com/Ilf0UkD.png)  
**[Note: I recommend saving your Audacity project just in case you are not happy with the timings during testing. This makes it much easier to tweak them later.]**

<br/>

**4.** First make sure your .WAV files are in the same folder as your .ACB and .AWB files.  
Then open up Eternity and go to File > Open > and choose the .ACB file. Then name each of your .WAV files to the ID number they are given in Eternity (The order will sometimes be different than displayed in Foobar so only use Eternity for this).  
![](https://i.imgur.com/ccDVKMv.png)

Your folder should now be similar to this:  
![](https://i.imgur.com/mWE7Kkl.png)

<br/>

**5.** In Eternity, select a track you want to replace and hit the replace button. Then find the correct .WAV file and when given the option pick **"Do not loop"**. Do this for every file you wish to replace and then hit save.

<br/>

**6.** Now the easy part, close Eternity and drag your newly generated .AWB file onto the Frontiers Boss Music Replacer .EXE.

![](https://i.imgur.com/ki5hdmq.png)

**[On first run it will ask you to paste in your Sonic Frontiers directory]**

<br/>

**7.** Once the program has ran you can now use these .ACB and .AWB files to listen to your music in-game. Congrats on the mod!

<br/><br/>

## **<u>I got an error!</u>**

This program is has not been tested on every boss and miniboss so bugs may exist. If you encounter any bugs first ensure you followed the steps in the tutorial correctly and that your game's sound files are not modified, then contact me by leaving a comment on [Gamebanana](https://gamebanana.com/tuts/15758) or leaving a bug report on the [Github](https://github.com/CoolguyTC/Frontiers-Boss-Music-Replacer) repo.

**[Specific error is appreciated if you have one]**
