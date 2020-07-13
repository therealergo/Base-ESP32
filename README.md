# SaucyBytes ESP32 Base

## Overview

This repository holds a base all-in-one build setup for ESP32. Included are the tools required for VS Code compilation, upload and flashing the ESP32. To get this project running on your machine follow the steps below.

## VS Code environment setup

1. Download the prerequisites:
    1. VS Code editor from their [downloads page](https://code.visualstudio.com/download).
    2. Python3 for your operating system from [their website](https://realpython.com/installing-python/).
    3. Git source control from their [downloads page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. You will need to download the CP210x driver from [here](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers).
    1. **Windows** - Download the driver for Windows 10 Universal. If using Windows 7 or 8 be sure to select the correct driver.
    2. **Mac OS** - The driver listed should work for all current versions of Mac OS - Note: You may have to open the Security tab in System Preferences and press *Allow* during or after installation for proper operation.
    3. **Linux** - The CP210x driver should be installed by default. There is a link on the page if your distribution does not include the driver.
3. Copy the following command: ```git clone https://github.com/SaucyBytes/SB-Base-ESP32.git```
4. Open the terminal for your operating system.
    1. **Windows** - Use the Windows start menu to open the PowerShell.
    2. **Mac OS** - Use Spotlight search to open the Terminal application.
    3. **Linux** - Open the Terminal for your specific distribution using the application menu.
5. Navigate to the location you'd like the repository cloned into using ```cd path/to/desired/location```.
6. Paste in the line copied in Step 3. The terminal may request you to login using your GitLab credentials. 
7. Open up the VS Code application we downloaded in Step 1.
8. Use the *Open folder...* option and navigate to the *SB-Base-ESP32* folder you just cloned. Press *Open*. See image below.
![Screenshot](Images/WhereToClickInVSCode.png)
9. Once the folder has opened, it is time to run the build tasks. Navigate to the *Terminal* tab in the menu bar. Select *Run Build Task...*.
![Screenshot](Images/WhereToOpenBuildTasks.png)
10. Use the arrow keys to select "Clean and Build" and give it a minute to compile all the code.
11. Plug your ESP32 into your computer. 
12. Repeat Step 8 to open the build tasks menu again. This time press *Flash*.

Your ESP32 should now be flashed with the firmware!