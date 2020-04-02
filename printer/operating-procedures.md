# Recalibration
[Printer Operating Procedures List](README.md#operating-procedures)
* To begin, check the level of the frame itself. Place a level on the four bottom frame walls, and use a wrench to make adjustments to the height of the printer's feet until all sides are level and the printer is stable on all four feet and not wobbling.
* Next, run the Tilt Calibration procedure. 
  * Start by placing metal bracket BIG-00-EXT-008 under the print head in the center of the bed. 
  * On the printer console, to to Prepare -> Move Axis -> Move Z. Reduce the height until you can slide the bracket while feeling resistance from the print head. 
    * Note - start by adjusting 10mm at a time, then switch to adjusting 1mm at a time, then switch to adjusting 0.1mm at a time. Switch to a smaller interval well in advance to avoid crashing the print head.
  * Move the print head to the left screw and right screws, and twist each screw manually until you feel the same resistance each time. 
    * Note that this should be done several times in series until the manual adjustments are not necessary, since changing one screw will change the bed's position at the other screws. 
    * Note also that if the print head is not over the PEI sheet on the right side, move the x axis back 20-30mm until the bracket can slide under the print head while completely on the PEI sheet.
* Next, run the UBL procedure. When complete, click each of the buttons on the UBL menu, in order. You should hear a beep after each button. Connect the printer to a computer running Pronterface, and send the mesh to the PC. Verify that the largest variance is less than 1mm. If not, revisit the Tilt Calibration step.
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
