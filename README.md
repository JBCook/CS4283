# CS4283
Computer Networks Final Project

Attached is arduino code that controls an LED light via a webpage with buttons that is interactive with a user  
The arduino itself creates the webpage (as shown in ledcontroller_2.html)  
The user uses the IP address 192.168.4.1 in web/mobile browser to see page.  
This page acts at the client which sends requests to the arduino itself  
Right now HTML uses buttons for "LED ON/OFF", which will be updated to PLAY, PAUSE, NEXT, VOLUME  
The buttons redirect user to different URL with the action appended to the end  
when we search for the keyword, an index will appear, which determines whether the button was click and the URL changed  
(if that word does not appear, then the index is not greater than one).  
FIX: user needs to press "back" to press another button  
We are working to modify this code in order to control an SD card with sound. By the presentation day we are planning to have implemented an "MP3 player" that is able to be controlled via a computer with buttons as a user interface that is accessible via a mobile device or a laptop. We need to figure out how the SD card can be configured with the arduino device to play songs - this will have to do with start and end bytes of each music file.
For the demonstration, we will have the ability to control *atleast* a LED light via a network. We're hoping to make this translate into controlling an SD card preloaded with music for the demonstration. 
