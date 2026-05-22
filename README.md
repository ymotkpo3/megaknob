# Volume-controller
I'm not taking classes because my university is on a stricke so I'm working and making my own projects.

This is a try to learn about connectivity between windows and the serial port of my arduino UNO and a little bit of the Windows audio stack. My objective is to documentate and demostrate the results of this project.

I'm doing the entire project with Python and the ArduinoIDE to load the program in C++.  

# Changelog

## 5/21/26

I've edited the Arduino firmware to make it detect only when you press and then release the button. This prevents the serial port from spamming the message "select". Now, the message is transmited one time each time I press the button. 

## 5/20/26

I've edited the connection.py file to be more modular. Now I have all methods in functions and now I can call them from the main file. Also I've added a new function called readSerial, that as it name tells, can read the serial port of the arduino with Python. 

## 5/19/26

To begin, I have been playing with the python packages pyserial and pycaw.

### Pyserial:

this is the package used to communicate with the Arduino Board with the serial communication method. All the things I did can be seen on the [connection.py](connection.py) file. It is a short program that detects the port where the Arduino is connected.

### Pycaw:

This package is very useful to control the audio of different Windows processes. This part can be found inside the [main.py](main.py) file. When I started trying to detect all the sound processes running in my computer, I had some problems because there where duplicated processes or processes with names that aren't de program real name. For example, the Whatsapp Web process is called msedgewebview2.exe. For now, this is not a problem because I'm learning how it works. 

### Arduino connection:

The objective is to use a rotary encoder, but to test the programs and the general method of working, I will use a button with the following connection scheme:

<img width="3000" height="4000" alt="20260520_133810" src="https://github.com/user-attachments/assets/bb5afa91-90a6-4e77-a627-d72c7ade4af2" />

<img width="1371" height="555" alt="image" src="https://github.com/user-attachments/assets/4e915545-e001-413a-ae2f-c4caa836acd6" />

This is called a pull-up resistance connection. It results that you cant connect te Arduino pin directly to the button and then to the ground or the 5V port because it can't read any information if the button isn't pressed. Also, if you connect the button between the 5V port and the ground port and the digital pin in parallel in the middle of that circuit, you are making a short-circuit.

#### Program:

The program can be found on the [ArduinoUNO.ino](https://github.com/ymotkpo3/proyecto-controlador-de-volumen/blob/main/Arduino%20Code/ArduinoUNO.ino) . There is not too much to see. It initializes te serial monitor and writes the word "select" when I press the button
