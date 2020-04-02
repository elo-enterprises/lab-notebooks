# Recalibration
[Printer Operating Procedures List](README.md#operating-procedures)
* To begin, check the level of the frame itself. Place a level on the four bottom frame walls, and use a wrench to make adjustments to the height of the printer's feet until all sides are level and the printer is stable on all four feet and not wobbling.
* Before running the Tilt Calibration procedure, place two levels on the bed at a right angle and manually twist the gears at the base of the ball screws until both directions appear level.

* Next, run the Tilt Calibration procedure. 
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Start Process. The print head will move to the center of the bed and the bed height will auto-home. Place a metal bracket, preferably [BIG-00-EXT-008](parts-lists.md#box-18---mtl1), under the print head in the center of the bed. 
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Adjust height (Z). Reduce the height until you can slide the bracket while feeling resistance from the print head. 
    * Note - start by adjusting 10mm at a time, then switch to adjusting 1mm at a time, then switch to adjusting 0.1mm at a time. Switch to a smaller interval well in advance to avoid crashing the print head.
  * On the printer console, go to Big-60 Calibration --> Tilt Calibration --> Calibrate Left --> Go to L Screw. The print head will move to a position over the left ball screw. Place the bracket under the print head, then manually twist the gear at the base of the left ball screw until the bracket slides between the bed and the print head with the same level of resistance as in the previous step. Repeat this process for the other two ball screws with the commands Calibrate Right --> Go to R Front Screw and Calibrate Right --> Go to R Rear Screw.
    * Note - this process should be repeated several times until the manual adjustments are not necessary, since changing one screw will change the bed's position at the other screws. 
    * Note - if the print head is not over the PEI sheet on the right side, go to Prepare --> Move Axis --> Move X on the printer console and move the X axis back 20-30mm toward the center until the bracket can slide under the print head while completely on the PEI sheet.

* Next, run the UBL procedure. 
  * On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Deactivate UBL (scroll down, as this option is at the bottom of the menu).
* On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Step-By-Step UBL --> 1 Build Mesh. The printer will undergo an automated procedure for ~15 minutes, moving the print head around the bed, raising and lowering the bed.
    * Note - if interrupted, restart this procedure from scratch.
* When the Build Mesh process is complete, on the printer console, go to Big-60 Calibration --> Unified Bed Leveling -->Step-By-Step UBL and click each of the buttons on the UBL menu, in order. You should hear a beep after each button. 
    * 2 Smart Fill-In
    * 3 Activate UBL
    * 4 Save Bed Mesh
* Next, check the mesh in Pronterface.
  * Physically connect the printer to a computer running Pronterface via the USB cable connection on the side of the electronics box. 
  * Open Pronterface and connect the appropriate port to the printer.
  * On the printer console, go to Big-60 Calibration --> Unified Bed Leveling --> Send Mesh to PC. Inspect the data output in Proneterface, and verify that the largest variance is less than 1mm. If not, revisit the Tilt Calibration step.

* Next, run the Z offset calibration procedure. Current Z offset value is -.7, but start at 1.5 and decrease until the head is close enough to the bed to produce a good test line.

* Next, run the Validate Mesh pattern and verify that the print produces clean lines and circles.

# Running a Print
[Printer Operating Procedures List](README.md#operating-procedures)
* Clean out any print material from previous prints. If there is filament stuck to the hot-end, go to Prepare-->Preheat PLA-->Preheat PLA 1, and when the hot-end is hot, peel the filament loose from the hot-end.
* Clean the bed with isopropyl alcohol and a cloth.
* Turn on the bed heater by flipping both switches. Use the up/down arrow buttons on the bed heater box to set T=70. The switches will start flashing when the target temperature is reached.
* Turn the printer on by flipping the switch on the electronics box and insert an SD card with the desired g-code file into the LCD Panel.
* Go to the Load/Unload Filament menu and select "Go to the Front." The printer will Auto-Home, then move to the front/center.
* Return to the Load/Unload Filament menu, select "Load/Unload E0", then select "Load filament E0." After the hot-end is heated, purge filament until you can verify that the filament is loaded and working.
* Go to the Z-offset calibration menu and click verify height.
* Go to the main menu, print from SD, select the file, and click on it.

# Filament Change
[Printer Operating Procedures List](README.md#operating-procedures)
* click on Pause Print, if the g-code did not do so automatically.
* click on load/unload filament, unload filament, and unthread the filament. If the PTFE tube comes loose, reinsert into the extruder, careful not to cause dents, kinks or excess friction.
* Insert the new filament, make sure the hot-end is still hot, move the print head to a position outside the range of the printing object, and purge the new filament until you can verify it is moving through the system.
* Resume the print.
