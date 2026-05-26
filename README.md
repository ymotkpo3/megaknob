# Megaknob
I’m not taking classes because my university is on strike, so I’m working and making my own projects.

This is an attempt to learn about connectivity between Windows and the serial port of my Arduino UNO, and a bit of the Windows audio stack. My objective is to document and demonstrate the results of this project.

I’m building the entire project with Python and the Arduino IDE to load the program in C++.

# Changelog

## 5/26/26

Today I decided to focus on process analysis on the computer. Although I can easily obtain the audio session of each program running on my computer, I cannot easily obtain a friendly name or identify the main process to which a subprocess belongs. This happens because many programs nest processes inside other processes. Because of this, I decided to integrate the Psutil library into my project. It is fully compatible with Pycaw and can help me find what I am looking for.

One example of this is WhatsApp Web. I do not fully understand how the audio management of that program works internally, but from what I can observe, the audio session is called msedgewebview2.exe. When I try to search for the parent processes of that process, Psutil only finds msedgewebview2.exe as the highest-level process.

For these reasons, I need to think of a way to find a process higher up in the subprocess tree that is actually related to the main application, which in this case would be WhatsApp. The problem is that if you keep analyzing parent processes all the way to the top, you may eventually encounter system processes. Because of this, I need to define a limit where system processes begin and stop searching before reaching that point.

I made a small program to extract parent processes and inspect the names of the most common system processes that appear above application executables, and I found what can be seen in the image below.

<img width="220" height="321" alt="image" src="https://github.com/user-attachments/assets/e23e0071-1722-4d61-b21e-8203ebade37a" />

To address this, I created a function that applies a heuristic capable of detecting when a process belongs to the system or to the actual program, and when it is not the original application name. What it does is traverse the process tree starting from the process that contains the audio session. It searches for the parent process of each process until it reaches a process that no longer belongs to a specific application, but instead belongs to the system. At this point, I determine that the last non-system process encountered is the parent process of all the remaining subprocesses, including the audio session, thereby identifying the real program name and its executable.

The only issue with this approach is that it relies on a set of conditions I defined manually, which act as exceptions. These exceptions can be found on the config.py file. This is not practical or stable at all, but it is the only way I have found to solve this problem without developing a custom task manager. Eventually, I will keep refining these process name exceptions to make the system more robust.

On the other hand, after spending a considerable amount of time researching the best way to structure the project, I concluded that the best approach is to create an “app” object for each application that produces audio on the computer. In this way, each “app” will contain the audio session process ID, the top process ID, and the friendly name of the application.

## 5/22/26

Today I was reviewing how certain parts of the code worked and correcting them to make the project easier to read and more modular.

Aside from that, I made a small program capable of iterating through a list of elements from beginning to end and returning to the first element after reaching the last one. The program switches between elements whenever the select button is pressed.

On the other hand, I added three buttons to the breadboard and configured each one to send a different message through the serial port.

<img width="1121" height="533" alt="image" src="https://github.com/user-attachments/assets/a13f6e77-3fd4-4091-8bcf-6b4e8adcfc3c" />


## 5/21/26

Today I was trying to think how to solve the problem of the serial port sending the text “select” multiple times per second. I’ve concluded that waiting to the release of the button is very important to detect a single click, so I’ve edited the Arduino firmware to make it detect only when you press and then release the button, adding a 500 millisecond delay. This prevents the serial port from spamming the message “select”. Now, the message is transmitted only one time each time the button is pressed.

## 5/20/26

I’ve edited the connection.py file to be more modular. Now I have all methods in functions, and I can call them from the main file. Also, I’ve added a new function called readSerial, which, as its name suggests, can read the serial port of the Arduino with Python.

## 5/19/26

To begin, I have been playing with the Python packages pyserial and pycaw.

### Pyserial:

This is the package used to communicate with the Arduino Board using the serial communication method. All the things I did can be seen in the [connection.py](connection.py) file. It is a short program that detects the port where the Arduino is connected.

### Pycaw:

This package is very useful to control the audio of different Windows processes. This part can be found inside the [main.py](main.py) file. When I started trying to detect all the sound processes running in my computer, I had some problems because there were duplicated processes or processes with names that weren’t the program's real name. For example, the WhatsApp Web process is called msedgewebview2.exe. For now, this is not a problem because I’m learning how it works.

### Arduino connection:

The objective is to use a rotary encoder, but to test the programs and the general method of working, I will use a button with the following connection scheme:

<img width="3000" height="4000" alt="20260520_133810" src="https://github.com/user-attachments/assets/bb5afa91-90a6-4e77-a627-d72c7ade4af2" />

<img width="1371" height="555" alt="image" src="https://github.com/user-attachments/assets/4e915545-e001-413a-ae2f-c4caa836acd6" />

This is called a pull-up resistance connection. Surprisingly, you can't connect the Arduino pin directly to the button and then to the ground or the 5V port because it can’t read any information if the button isn’t pressed. Also, if you connect the button between the 5V port and the ground port and the digital pin in parallel in the middle of that circuit, you are making a short-circuit.

#### Program:

The program can be found on the [ArduinoUNO.ino](https://github.com/ymotkpo3/proyecto-controlador-de-volumen/blob/main/Arduino%20Code/ArduinoUNO.ino) . There is not too much to see. It initialises the serial monitor and writes the word “select” when I press the button.
