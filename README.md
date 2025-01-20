# Android Controller Using Python
## Introduction:
This project provides a simple and practical way to control an Android device using Python and ADB. The main features include opening the camera, collecting system logs, recording the screen, and taking pictures. This tool is especially useful for developers and testers who need to automate Android device interactions or debug issues quickly.
## Features:
Open CameraLaunch the phone’s camera app with a single command. Perfect for testing or quick access.
Collect LogsRetrieve system logs from the Android device and save them to a text file for analysis. Ideal for debugging apps or system behavior.
Screen RecordingRecord the phone’s screen and save the video file directly to the device. Great for documenting steps or creating.
## tutorials:
Take PicturesSimulate a photo capture and download the image directly to your computer for immediate use.
## Prerequisites:
Python 3 installed on your system.
ADB installed and added to your system’s PATH.
An Android device with "USB Debugging" enabled.
A USB cable to connect your Android device to the computer.
Ensure ADB is properly set up and can detect your Android device:
adb devices
You should see your device listed.
## Usage
Run the main.py script and follow the on-screen menu to select a feature.
## Run the script:
main.py
## Select a function from the menu:
1: Open Camera
2: Collect Logs
3: Screen Recording
4: Take Picture
5: Exit
## Example
Here’s an example of how to collect logs:
Select option 2 from the menu.
The script will save the logs to a file named device_log.txt in the current directory.
Open the device_log.txt file to view the collected logs.
Troubleshooting
ADB Device Not Found:
Ensure "USB Debugging" is enabled on your phone.
Check that the phone is connected via USB and the ADB connection is authorized.
Permission Denied Errors:
Run the script or ADB commands with administrative privileges.nting steps or creating.
##  From University Project Experience:
This project was developed as part of a university capstone project, where the primary goal was to integrate hardware and software capabilities to create a practical tool for Android developers. 
## Key learning outcomes from this experience include:
### Problem-Solving Skills:
Addressing challenges in integrating Python scripts with ADB for seamless device control.
### Team Collaboration:
Working in a team to design, implement, and test the project, ensuring smooth functionality across all features.
### Innovation: 
Exploring ways to make the tool user-friendly for developers with varying levels of expertise.
### Technical Expertise: 
Strengthening skills in Python programming, ADB commands, and debugging techniques.
This project not only honed technical skills but also emphasized the importance of collaboration, communication, and continuous learning in software development.
