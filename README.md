# ESP32 Base <!-- From ESP32-Base, CHANGE for an actual project README -->

## Overview <!-- From ESP32-Base, CHANGE for an actual project README -->

This repository holds a base all-in-one build setup for ESP32. Included are the tools required for VS Code compilation, upload and flashing the ESP32.

## Creating an ESP32-Based project <!-- From ESP32-Base, REMOVE for an actual project README -->

The easiest way to create a new ESP32 project is by importing this repository. This can be done with the following steps:
1. Create a new git repository (in the correct organization) using GitHub's green **New**  button on the organization page.
2. Put in a reasonable name under **Repository name** (and maybe a description in the next box), then hit **Create repository**.
3. In the bottom-left of the page, hit the **Import code** button.
4. Now, paste in this git link ```https://github.com/therealergo/Base-ESP32.git``` under **Your old repository’s clone URL**.
5. Hit **Begin import**. At this point, you may have to input your GitHub credentials. When this is done, your development git repository is ready to use.

## VS Code environment setup <!-- From ESP32-Base, DONT CHANGE for an actual project README -->

1. Download the prerequisites:
    1. VS Code editor from their [downloads page](https://code.visualstudio.com/download).
    2. Python3 for your operating system from [their website](https://realpython.com/installing-python/).
    3. Git source control from their [downloads page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. You will need to download the CP210x driver from [here](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers).
    1. **Windows** - Download the driver for Windows 10 Universal. If using Windows 7 or 8 be sure to select the correct driver.
    2. **Mac OS** - The driver listed should work for all current versions of Mac OS - Note: You may have to open the Security tab in System Preferences and press *Allow* during or after installation for proper operation.
    3. **Linux** - The CP210x driver should be installed by default. There is a link on the page if your distribution does not include the driver.
3. Copy the following command: ```git clone https://github.com/therealergo/Base-ESP32.git```
4. Open the terminal for your operating system.
    1. **Windows** - Use the Windows start menu to open the PowerShell.
    2. **Mac OS** - Use Spotlight search to open the Terminal application.
    3. **Linux** - Open the Terminal for your specific distribution using the application menu.
5. Navigate to the location you'd like the repository cloned into using ```cd path/to/desired/location```.
6. Paste in the line copied in Step 3. The terminal may request you to login using your GitLab credentials. 
7. Open up the VS Code application we downloaded in Step 1.
8. Use the *Open folder...* option and navigate to the *Base-ESP32* folder you just cloned. Press *Open*.
9. Once the folder has opened, it is time to run the build tasks. Navigate to the *Terminal* tab in the menu bar. Select *Run Build Task...*.
10. Use the arrow keys to select "Clean and Build" and give it a minute to compile all the code.
11. Plug your ESP32 into your computer. 
12. Repeat Step 8 to open the build tasks menu again. This time press *Flash*.

Your ESP32 should now be flashed with the firmware!

## Merging ESP32 Base changes <!-- From ESP32-Base, DONT CHANGE for an actual project README -->

From time to time, improvements may be made to the ESP32 project base. To bring those changes into your existing project (on the master branch), take the following steps:
1. Run the following command: ```git pull https://github.com/therealergo/Base-ESP32.git master```
2. If there are any CONFLICT's listed, merge the changes together. This should be uncommon, but you'll have to use your brain to ensure the result is correct.
3. If a merge was necessary, run ```git commit``` to finish the merge.
4. Test your tools to ensure that everything is working as intended.
5. Now run ```git push``` to actully push your changes to GitHub.
