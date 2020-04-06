# Operating Procedures

------------

This page contains step-by-step instructions for operating the printer.

------------
## Recalibration
[Main Page - Operating Procedures List](README.md#operating-procedures)

[Part 3 Step 05](system-assembly--repair.md#part-3--step-5-terminal-software-and-basic-g-code)

### Frame Leveling Procedure
* To begin, check the level of the frame itself. Place a [level](parts-lists.md#tools) on the four bottom frame walls, and use a wrench to make adjustments to the height of the printer's feet until all sides are level and the printer is stable on all four feet and not wobbling.
* Before running the Tilt calibration procedure, place two levels on the bed at a right angle and manually twist the gears at the base of the ball screws until both directions appear level.

### Tilt Calibration Procedure
  * Details can be found in the Modix Customer Zone under [Calibration Guide – 2. Tilt Calibration](http://www.support.modix3d.com/tilt-calibration/)
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Start Process. The print head will move to the center of the bed and the bed height will auto-home. Place a metal bracket, preferably [BIG-00-EXT-008](parts-lists.md#box-18---mtl1), under the print head in the center of the bed. 
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Adjust height (Z). Reduce the height until you can slide the bracket while feeling resistance from the print head. 
    * Note - start by adjusting 10mm at a time, then switch to adjusting 1mm at a time, then switch to adjusting 0.1mm at a time. Switch to a smaller interval well in advance to avoid crashing the print head.
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Calibrate Left --> Go to L Screw. The print head will move to a position over the left ball screw. Place the bracket under the print head, then manually twist the gear at the base of the left ball screw until the bracket slides between the bed and the print head with the same level of resistance as in the previous step. Repeat this process for the other two ball screws with the commands Calibrate Right --> Go to R Front Screw and Calibrate Right --> Go to R Rear Screw.
    * Note - this process should be repeated several times until the manual adjustments are not necessary, since changing one screw will change the bed's position at the other screws. 
    * Note - if the print head is not over the PEI sheet on the right side, go to Prepare --> Move Axis --> Move X on the printer console and move the X axis back 20-30mm toward the center until the bracket can slide under the print head while it is completely over the PEI sheet.

### Unified Bed Leveling (UBL) Calibration Procedure
  * Details can be found in the Modix Customer Zone under [Calibration Guide – 3. Unified Bed Leveling Calibration](http://www.support.modix3d.com/ubl/)
  * On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Deactivate UBL (scroll down, as this option is at the bottom of the menu).
* On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Step-By-Step UBL --> 1 Build Mesh. The printer will undergo an automated procedure for ~15 minutes, moving the print head around the bed, raising and lowering the bed.
    * Note - if interrupted, restart this procedure from scratch.
* When the Build Mesh process is complete, on the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Step-By-Step UBL and click each of the buttons on the UBL menu, in order. You should hear a beep after each button. 
    * 2 Smart Fill-In
    * 3 Activate UBL
    * 4 Save Bed Mesh
* Next, check the mesh in Pronterface.
  * Physically connect the printer to a computer running Pronterface via the USB cable connection on the side of the electronics box. 
  * Open Pronterface and connect the appropriate port to the printer.
  * On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Send Mesh to PC. Alternatively, this can be done by entering the command 'G29 T' into Pronterface. Inspect the data output in Pronterface, and verify that the largest variance is less than 1mm. 
    * If the maximum variance is 1mm or more, repeat the Tilt calibration step.
    * If the Tilt calibration does not fix the problem, look for damage to the PEI sheet, or even the bed itself. They may need to be replaced.

### UBL Adjustment Procedure
  * Use the online tool built by Modix, found [here](http://www.support.modix3d.com/ubl-editor-119/)
  * In the Modix UBL tool, change the size of the grid to 10 x 10.
  * With the computer connected to the printer via Pronterface, once the mesh has been sent to the PC, click 'Upload' on the Modix UBL tool, then 'Click to Process.' 
  * Manually adjust the numbers //INSERT RULES FOR UPDATING NUMBERS
  * Press the 'Export' button and save the gcode file.
  * Load the gcode file into Pronterface, then click 'Print.'
  * Enter the command 'G29 T' into Pronterface and verify that the updated mesh numbers have been saved into Marlin, the printer firmware.

### Z Offset Calibration Procedure 
  * Details can be found in the Modix Customer Zone under [Calibration Guide – 4. Z Offset Calibration](http://www.support.modix3d.com/z-offset-calibration/)
  * Make sure the bed heater is turned on to ~65 degrees and that filament is ready to load, i.e. passed through the filament sensor through the PTFE tube until it touches the gears of the extruder, or is already loaded.
  * On the printer console, go to Load/Unload Filament --> Go to the Front. The print head will travel to the center front of the printer, making it easy to see the filament purging process.
  * On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Preheat PLA (200). The print head heater will begin heating and a message to wait will appear.
  * On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Purge E0. Once the print head is heated, the extruder will attempt to grab the filament and purge through the nozzle. 
    * If the purge is unsuccessful, try purging more while manually applying forward pressure on the filament at the filament sensor, pushing it toward the extruder. 
    * If several purge attempts are unsuccessful, the nozzle may be clogged. While the printer is hot, try scraping off any plastic around the nozzle. If this is unsuccessful, power off and let everything cool down, then remove the nozzle and try cleaning it out.
  * After a successful purge, on the printer console, go to Big-60 Calibration --> Z Offset Calibration --> 1 Set Temperature. Set the temperature to 200 for PLA.
  * On the printer console, go to Big-60 Calibration --> Z Offset Calibration and inspect the current saved Z Offset value. For normal operation in Las Vegas, we have been using -.7mm, but the initial factory setting is 1.5mm to avoid crashing the print head during calibration. If the printer has been significantly moved, reset to 1.5mm and start over.
  * Itertively perform the following operations until you are satisfied that the test line is successful.
    * On the printer console, go to Big-60 Calibration --> Z Offset Calibration --> 3 Verify Height. The bed will move to the saved Z Offset height.
    * On the printer console, go to Big-60 Calibration --> Z Offset Calibration --> 4 Print Test Line. The printer will print out a straight line. 
    * If the print head is too far away from the bed, you will see the vertical gap between the filament and the bed as the test line is printed. In this case, adjust the saved Z Offset value down. If the print head is too close to the bed, the test line will be smeared by the print head itself, and the line will appear flat and nonuniform. In this case, adjust the Z Offset value up.
  * Once you are satisfied with the test line, on the printer console, go to Big-60 Calibration --> Z Offset Calibration --> 5 Save Z Offset.
    * Note that if the UBL mesh is nonuniform across the space of the bed, the X and Y placement of the print head while it is printing the test line is relevant to the correctness of the Z Offset setting.
    
### Validate Mesh Calibration Procedure
  * Details can be found in the Modix Customer Zone under [Calibration Guide – 5. Validate Mesh](http://www.support.modix3d.com/validate-mesh/)
  * Make sure the bed heater is on, set to e.g. ~65 degrees.
  * On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Validate Mesh. Select the filament material and nozzle size in use, e.g. 'PLA, Nozzle:0.4.' The printer will begin printing a pattern of lines and circles across the entire print bed, lasting ~20 minutes. Constant monitoring is not necessary, but several useful conclusions can be drawn from the mesh grid output.
    * If the circles appear as ellipses, this is likely due to improperly aligned X and Y axis belts. See [Troubleshooting - Layer Shifts](troubleshooting-issues.md#layer-shifts).
    * If the circles and lines are clearer in some parts of the bed than others, revisit the previous calibration step using the Modix online tool for UBL adjustment.
    * If the entire pattern is not sticking to the bed, see [Troubleshooting - First Layer Not Sticking to the Bed](troubleshooting-issues.md#first-layer-not-sticking-to-the-bed).

------------
## Running a Print
[Main Page - Operating Procedures List](README.md#operating-procedures)

[Part 3 Step 08](system-assembly--repair.md#part-3--step-8-printing-settings-for-slicing-software)

[Part 3 Step 09](system-assembly--repair.md#part-3--step-9-running-your-first-print)

### Import an STL 3D Model File
* Within PrusaSlicer, use the command File --> Import --> ImportSTL/OBJ/AMF/3MF/PRUSA to import an STL file. A typical STL file is tens of thousands of lines long and is human-unreadable. The file is the output of a 3D modeling tool that has been used to create a model of an object.

### Export an INI PrusaSlicer Configuration File
* Within PrusaSlicer, use the command File --> Export --> ExportConfig to produce an INI file. A typical INI file is a few hundred lines of human-readable text that set values for alphabetically sorted parameters, specifying everything about the system except the details of the STL 3D model file(s), e.g. position, scale, rotation, infill%, and support type.

### Create and Save a 3MF PrusaSlicer Project File
* Within PrusaSlicer, use the command File --> SaveProject to produce a 3MF file, executable within PrusaSlicer. If changes are made to the project in the 3MF project file, any INI files will not be updated.

### Export a GCODE Output File
* Within PrusaSlicer, use the command ExportGCode to create a GCODE file. A typical GCODE file is a hundred thousand lines of code telling the printer every mechanical operation it has to perform, in order, with specific parameter settings. While GCODE is tedious, it is human readable, and lists of common GCODE commands can be found, e.g. http://marlinfw.org/docs/gcode/M206.html.

### At the Printer
* Clean out any print material from previous prints. If there is filament stuck to the hot-end, on the printer console, go to Prepare --> Preheat PLA --> Preheat PLA 1. Once the hot-end is hot, peel the filament loose from the hot-end using a scraping tool.
  * Note - DO NOT TOUCH THE HOT END WITH YOUR HANDS! The whole point is that it is very, very hot.
* Clean the bed with isopropyl alcohol and a cloth.
* Turn on the bed heater by flipping both switches. Use the up/down arrow buttons on the bed heater box to set the temperature, currently in the range 60-70. The switches will start flashing when the target temperature is reached.
* Turn the printer on by flipping the switch on the electronics box.
* Insert an SD card with the desired gcode file into the LCD Panel.
  * Note - be careful when inserting the SD card. If it slips into the control panel, use a hex key to unscrew the control panel and retrieve the SD card.
* On the printer console, go to Load/Unload Filament --> Go to the Front. The print head will auto-home, then move to the front at the center.
* On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Preheat PLA (200). The print head heater will begin heating and a message to wait will appear.
* On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Purge E0. Once the print head is heated, the extruder will attempt to grab the filament and purge through the nozzle. 
  * If the purge is unsuccessful, try purging more while manually applying forward pressure on the filament at the filament sensor, pushing it toward the extruder. 
  * If several purge attempts are unsuccessful, the nozzle may be clogged. While the printer is hot, try scraping off any plastic around the nozzle. If this is unsuccessful, power off and let everything cool down, then remove the nozzle and try cleaning it out.
* On the printer console, go to Big-60 Calibration --> Z Offset Calibration --> 3 Verify Height. The bed will move to the saved Z Offset height. 
  * This step appears unnecessary at first glance, but can be useful in eliminating conflict between the height settings in the slicing software and the height settings in the Marlin firmware.
* On the printer console, go to Print from SD. Select the file, and click on it. The print will start. 
  * Pay special attention to the first layer. If obvious problems arise, it may be worthwhile to stop the print early and restart to avoid wasting time and filament.

------------
## Filament Change
[Main Page - Operating Procedures List](README.md#operating-procedures)
* If the current print's gcode paused automatically, everything is fine. We have not yet attempted to stop a print manually by pressing the pause button, change filament and resume. Be aware that this may ruin the print.
* On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Unload Filament. The extruder gears will turn in reverse, ejecting the filament. While this is happening, gently pull on the filament at the filament sensor to assist in unthreading. 
  * If the PTFE tube comes loose, reinsert it into the extruder, careful not to cause dents, kinks or excess friction.
* Insert the new filament. 
  * On the printer console, go to Load/Unload Filament --> Go to the Front. The print head will travel to the center front of the printer, making it easy to see the filament purging process. If this location overlaps with the print in progress, go to Prepare --> Move Axis --> Move X (and/or Y) and find a suitable purge location.
  * On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Preheat PLA (200). The print head heater will begin heating and a message to wait will appear.
  * On the printer console, go to Load/Unload Filament --> Load/Unload E0 --> Purge E0. Once the print head is heated, the extruder will attempt to grab the filament and purge through the nozzle. 
    * If the purge is unsuccessful, try purging more while manually applying forward pressure on the filament at the filament sensor, pushing it toward the extruder. 
    * If several purge attempts are unsuccessful, the nozzle may be clogged. While the printer is hot, try scraping off any plastic around the nozzle. If this is unsuccessful, power off and let everything cool down, then remove the nozzle and try cleaning it out.
* Resume the print, careful to verify that the print head correctly moved back to the location where the print was paused.
