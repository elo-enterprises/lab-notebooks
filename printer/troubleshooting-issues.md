# Troubleshooting Issues

------------

# Layer Shifts
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

Layer shifts can happen for a few reasons, please check the following:

### Y-axis
* Make sure the belt on the Y-axis and on the Y motor is tightened and doesn't slip. See [01-15, Installing the Y Axis Timing Belt](system-assembly--repair.md#part-1--step-15-installing-the-y-axis-timing-belt).
* Reducing printing speed (40-50mm/s), traveling and acceleration will definitely help. Especially the first layer should be 50% or less than the main speed.
* Make sure to set 'Z-hop' or 'vertical lift' in the slicer (lifting the nozzle when traveling).
* Make sure that the fan on the electronics box is cooling the stepper drivers.
* Make sure the wiring isn't loose or torn both on the controller board and on the motor.
* Make sure that the driver has enough current, it should be no more than 1.1 V. But as low as possible. The current can be increased by turning the Vref clockwise 1/4 turn at the time. Attached is a photo on how to measure the current - (-) on the GND pin and (+) on the Vref.
* Try to replace a stepper driver (the kit comes with spares).

### X-axis
* Make sure the belts on the X-axis and on the X motor are tightened and don't slip. See [01-16, Installing the Timing Belt at the Back X Axis ](system-assembly--repair.md#part-1--step-16-installing-the-timing-belt-at-the-back-x-axis) and [01-17, Installing the Timing Belt at the Front X Axis](system-assembly--repair.md#part-1--step-17-installing-the-timing-belt-at-the-front-x-axis).
* Make sure the pulleys on the X-shaft and on the X-motor are tightened and don't slip. See [01-12, Installing the X Shaft](system-assembly--repair.md#part-1--step-12-installing-the-x-shaft) and [01-14, Installing the Motors](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Reducing printing speed (40-50mm/s), traveling and acceleration will definitely help. Especially the first layer should be 50% or less than the main speed.
* Make sure to set 'Z-hop' in the slicer (lifting the nozzle when traveling).
* Make sure that the fan on the electronics box is cooling the stepper drivers.
* Make sure the Y-axis rail is parallel to the X shaft and doesn't have an angle. See [01-13, Assembling the Y Axis](system-assembly--repair.md#part-1--step-13-assembling-the-y-axis).
* Make sure the wiring isn't loose or torn both on the controller board and on the motor.
* Make sure that the driver has enough current, it should be no more than 1.1 V. The current can be increased by turning the Vref clockwise 1/4 turn at the time. Attached is a photo on how to measure the current - (-) on the GND pin and (+) on the Vref
* Try to replace a stepper driver (the kit comes with spares).

# Z Motors Binding Up
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

When first turning the printer on, we encountered serious trouble with the Z motors and received support from Modix. The motors could lower the bed down, but when going up, seemingly randomly, would encounter friction and try to move, but the bed did not move, and we would turn the printer off before causing more damage. The list of things to check included:
* Before leveling the bed, make sure to level the base frame.
* Check the bottom shaft of each z-screw, make sure it doesn't go all the way down and touching the aluminum profile.
* Make sure that all pulleys and gears are well tightened and don't slip. See [01-10, Assembling the Z Axis Sets](system-assembly--repair.md#part-1--step-10-assembling-the-z-axis-sets) and [01-14, Installing the Motors](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Try to move each screw manually on both directions (when the z screws are disassembled from the bed brackets).
* The belts that drive the z-screws could be to tightened too much, check that as well. They need to be tightened to point they sit straight and don't sag, no more than that
* Try to move each screw with a separate cable, without a split. You can use the spare cable you have. Are they moving smoothly? Can you spot any damaged wire connections on the Z cable and motors? See [02-01, Wiring the Motors and End Stops](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* You can also replace the stepper driver for z with one of the spares you got with the kit.
* Check the current on the stepper driver with a multimeter. It should be no more than 1.2V. The way to measure it is to set the multimeter to 2V, red pin on the Vref, black pin on GND pin on the stepper driver. If it's lower than 1.2V, turn the Vref (potentiometer) clockwise, no more than 1/4 turn at a time.
* Check that there's nothing wrong in the firmware settings, so connect to Pronterface and send Modix the output log once connected, or send command M503. See [03-05, Terminal Software and Basic G-Code](system-assembly--repair.md#part-3--step-5-terminal-software-and-basic-g-code).

# Poor Bridging
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)



# Spaghetti Monster
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

On the print MU75_joint_ring_extension, I encountered the same failure scenario twice. The object is a tall cylinder, which means it does not have a lot of surface area to bind with the bed. Both times, ~75% of the object builds correctly, and on a layer in which four columns are recombined to form a circle, the printer head pushes the object off the bed. I will attempt to perform the print again, tuning the printer to slow down just before this layer. I may also try tuning the nozzle height a little higher before the key layer. If this does not work, I will try adding a raft to the base of the object to increase its grip on the bed.

<center>
<table>
  <tr>
    <td><a href=img/fail1.png><img src=img/20200209_152227.jpg width=300px></a></td>
    <td><a href=img/fail1.png><img src=img/20200209_164950.jpg width=300px></a></td>
  </tr>
  <tr>
    <td><a href=img/fail1.png><img src=img/20200209_172458.jpg width=300px></a></td>
    <td><a href=img/fail1.png><img src=img/20200209_222938.jpg width=300px></a></td>
  </tr>
  <tr>
    <td><a href=img/fail1.png><img src=img/20200209_230735.jpg width=300px></a></td>
  </tr>
</table>
</center>



# Stringing & Oozing
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D](https://www.simplify3d.com/support/print-quality-troubleshooting/stringing-or-oozing/)


# Ugly Overhangs
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)




# Z Wobble
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)




# Scars on Top Surface
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)



# Blobs and Zits
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)




# Curling or Rough Corners
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/curling-or-rough-corners/)

On 2020-02-06, the issue of curling was noticed in addition to the issue of the first layer not sticking to the bed. Both of these problems could be related to overheating. Initially, the bed temperature is set to 70, while the Simplify3d guide suggests 60-70 for PLA. The cooling fan is disabled for the first 3 layers, and the extruder temperature is set to 200 for the first layer and 203 after that.


# Overheating
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/overheating/)


# Warping
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)



# Vibrations and Ringing
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)


# First Layer Not Sticking to the Bed
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-sticking-to-the-bed/)

Possible Causes:
 * the bed is not level
 * the nozzle starts too far away from the bed
 * the first layer is printing too fast
 * incorrect temperature or cooling settings
 * problems with the bed surface

On 2020-02-06, the issue of curling was noticed in addition to the issue of the first layer not sticking to the bed. Both of these problems could be related to overheating. Initially, the bed temperature is set to 70, while the Simplify3d guide suggests 60-70 for PLA. The cooling fan is disabled for the first 3 layers, and the extruder temperature is set to 200 for the first layer and 203 after that.

The first layer speed is set to 30 mm/s. The Z offset is set to -0.7mm.

Testing
 * For the first test, I lowered the bed temperature to 65, and cleaned the bed surface with isopropyl alcohol. This did not work, and the first layer is still not sticking.
 * For the second test, I started the print, then tuned the Z offset to -0.75mm. The problem persists, with a few notes: (1) the test print first layer consists of thin circular walls, which could be more difficult to make the first layer stick than e.g. a single rectangle with more continuous surface area. (2) the circles in the middle y with higher x stick better than the others, which could be explained by differences in height across the bed.
  * For the third test, I lowered the first layer speed to 30% of the 50 mm/s total, rather than 30 mm/s, leaving the Z offset at -0.75.


# Grinding or Stripping Filament
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/grinding-filament/)


# Clogged Extruder
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/clogged-extruder/)


# Stops Extruding Mid Print
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/stops-extruding-mid-print/)


# Not Extruding at Start of Print
[Printer Troubleshooting Issues List](README.md#troubleshooting-issues)

[Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-extruding-at-start-of-print/)


# Troubleshooting Data Sources
[Printer Related Work and References List](README.md#related-work-and-references)

| Name | Notes |
|------|-------|
| [Modix Instructions, Part 3 Step 12](http://www.support.modix3d.com/troubleshooting/) | |
| [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/) | |
| [All3DP Basics Guide](https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/) | |
| [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide) | |
| [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide) | |
| [Prusa3D](https://www.prusa3d.com/print-quality-troubleshooting/) | |
| [Ultimaker](https://support.3dverkstan.se/article/23-a-visual-ultimaker-troubleshooting-guide) | |
| [RepRap](https://3dprintingforbeginners.com/glossary/reprap/) | |
| [Reddit Overall](https://www.reddit.com/r/3Dprinting/) | |
| [Reddit Fix My Print](https://www.reddit.com/r/FixMyPrint/) | |
| [3D Printing For Beginners](https://3dprintingforbeginners.com/troubleshoot-3d-printing-problems/) | Compilation of other guides |
| [The Art of Failure](https://richrap.blogspot.com/2011/10/art-of-failure-when-3d-prints-go-wrong.html) | Overall philosophy of failed 3D prints|
