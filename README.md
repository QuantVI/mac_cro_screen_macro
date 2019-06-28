# mac_cro_screen_macro
A screen macro in Python for Mac OS - because you'd otherwise have to buy one.

Most decent things in the MacOSX evironment are premium. You pay to download, upgrade, etc. Common utilities that users of Windows can download and use for free, all sit behind $ buttons in the MacOS. TinyTask is a great mouse/keyboard recorder for Windows, that has been around for a long time as a free utility. There's no unpaid MacOSX equivalent. 

Should one need to purchase a program that will click on one spot of the screen?
Is it fun to only use trial versions, with basic functionality?

**Absolutely not**

The Mac screen macro does something very simple
- get the current position of the mouse
- begin left-clicking
- stop left-clicking if the mouse moves from its initial position

I later changed it to
- PAUSE when the mouse moves outside of a certain range/radius of the inital mouse position
- RESUME clicking when the mouse return within that radius

This free, basic clicker that works on MacOSX, is perfect for games such as those on [Kongregate.com](http://kongregate.com)

#### Simple usage
1. Download the .py
- Open IDLE, then open the script in IDLE (one or two external package required)
  - You can edit the size of the error box around the mouse position. Then save.
  - You can edit the times between about 6--8 clicks. It's better for each click to be unevenly spaced.
  - You can edit the loops/time. It's set to several hours worth
- In Mac, you can have a different screen active, than where your mouse is
  - Make sure IDLE shell (i.e. interactive) window is open
  - Have IDLE script (i.e. the .py file) window active
  - Place mouse in the area that needs to be clicked
- Hit F5 on your **KEYBOARD** (with the scrpit windo active, it runs the script)
  - shell winodw become active
  - after a slight pause, the mouse will begin clicking
- Test that clicking stops, when you move a certain range away form inital mouse position  
- Use one of Control+C, Control+D, Control+B to break the loop/stop execution
  - Note: ideally, the shcell window is not within the "error range" of the inital mouse position,
  - That way, clicking will stop, when you need to go to the shell to stop execution
