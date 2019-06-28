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
