# Troubleshooting Issues

------------

This page contains data on problems encountered in printer operation, as well as a list of troubleshooting references at the bottom of the page.

------------
## Z Motors Binding Up
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

When first turning the printer on, serious trouble with the Z motors was encountered, prompting repeated customer support interactions with Modix. The motors could lower the bed down correctly. When going up, however, seemingly at random, the motors would encounter friction and try to move without moving the bed up. The printer was turned off before causing further damage. Modix sent a checklist of issues to check:
* Before leveling the bed, make sure to level the base frame.
* Try to move each screw manually in both directions when the ball screws are disassembled from the bed brackets. See [Part 1 Step 09](system-assembly--repair.md#part-1--step-9-assembling-the-z-axis-mid-brackets)
* Check the bottom shaft of each ball screw. Make sure it does not sit all the way down; the base of the ball screws should not touch the base of the pillow bearings, or excess friction will result. See [Part 1 Step 10](system-assembly--repair.md#part-1--step-10-assembling-the-z-axis-sets).
* Make sure that all pulleys and gears are well tightened and do not slip. See [Part 1 Step 10](system-assembly--repair.md#part-1--step-10-assembling-the-z-axis-sets) and [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Check whether the belts that drive the ball screws are tightened too much. They need to be tightened to the point that they sit straight and do not sag and no further. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Try to move each screw individually with the spare motor cable. Make sure they are moving smoothly. Look for damaged wire connections on the Z cable and on the motors. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the Z motors with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Check the current on the stepper driver with a multimeter. It should be no more than 1.2V. The way to measure it is to set the multimeter to 2V, red pin on the Vref, black pin on GND pin on the stepper driver. If the current is lower than 1.2V, turn the Vref (potentiometer) clockwise, no more than 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Check that there is nothing wrong in the firmware settings. Connect to Pronterface and send Modix the output log once connected or send command M503. See [Part 3 Step 05](system-assembly--repair.md#part-3--step-5-terminal-software-and-basic-g-code).

------------
## Stripped Set Screws
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

At several steps, the 3mmx3mm set screws used to tighten gears stripped. To avoid causing damage requiring replacement of more expensive parts, the 3mmx3mm set screws were replaced with externally purchased [4mmx3mm set screws](parts-lists.md#tools). These screws added more contact surface area between the inside of the screw and the hex key. A new [hex key](parts-lists.md#tools) was also used, and no further stripping was detected. See the following steps: 
* [Part 1 Step 08](system-assembly--repair.md#part-1--step-8-assembling-the-z-axis-bottom-brackets);
* [Part 1 Step 09](system-assembly--repair.md#part-1--step-9-assembling-the-z-axis-mid-brackets);
* [Part 1 Step 12](system-assembly--repair.md#part-1--step-12-installing-the-x-shaft);
* [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors);

------------
## LCD Screen Button Friction
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

The main LCD screen button is vulnerable to a relatively serious problem. In the case of excess friction, the main LCD screen button can trigger the click action while turning to scroll through options lists. Removing the plastic cover from the button and using the metal knob underneath suffices as a temporary solution. //TODO: Replace the button and contact customer support if the problem persists. See [Part 1 Step 22](system-assembly--repair.md#part-1--step-22-assembling-the-lcd-screen).

------------
## Layer Shifts
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

Layer shifts were a serious early issue. When printing test patterns, circles printed as ellipses. In correspondence, Modix customer support indicated that this problem is caused by the Y axis not being perfectly square and supplied the following checklist:

### Y-axis
* Make sure the belts on the Y axis and on the Y motor are tightened and do not slip. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors) and [Part 1 Step 15](system-assembly--repair.md#part-1--step-15-installing-the-y-axis-timing-belt).
* Make sure the wiring is not loose or torn either on the controller board or on the Y motor. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Make sure that the stepper driver for the Y motor has enough current. It should be no more than 1.1 V, as low as possible. The current can be increased by turning the Vref clockwise 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the Y motor with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).

### X-axis
* Make sure the pulleys on the X shaft and on the X motor are tightened and do not slip. See [Part 1 Step 12](system-assembly--repair.md#part-1--step-12-installing-the-x-shaft) and [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Make sure the Y axis rail is parallel to the X shaft and does not have an angle. 
  * Loosen the front X idler and the set screw of the pulley connecting the front X belt to the X shaft.
  * Loosen the front X belt.
  * Connect the Y axis to the frame using the calibration jigs.
  * Loosen the screws holding the Y axis profile to the X rails.
  * Tighten the X belt.
  * Tighten the Y axis screws.
  * Tighten the pulley connecting the front X belt to the X shaft and the X idler.
  * Remove the calibration jigs.
   See [Part 1 Step 13](system-assembly--repair.md#part-1--step-13-assembling-the-y-axis).
* Make sure the belts on the X axis and on the X motor are tightened and do not slip. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors), [Part 1 Step 16](system-assembly--repair.md#part-1--step-16-installing-the-timing-belt-at-the-back-x-axis) and [Part 1 Step 17](system-assembly--repair.md#part-1--step-17-installing-the-timing-belt-at-the-front-x-axis).
* Make sure the wiring is not loose or torn either on the controller board or on the X motor. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Make sure that the stepper driver for the X motor has enough current. It should be no more than 1.1 V, as low as possible. The current can be increased by turning the Vref clockwise 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the X motor with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* To be completely thorough, revisit [Part 2 Step 15](system-assembly--repair.md#part-2--step-15-tightening-all-screws), loosen and tighten the screws, being extremely careful to measure right angles. 

### Overall
* Make sure that the fan on the electronics box is working and successfully cooling the stepper drivers. See [Part 2 Step 04](system-assembly--repair.md#part-2--step-4-installing-the-electronics-box-cover).
* Reducing [printing speed](printing-variables.md#prusaslicer-print-variables) (40-50mm/s), traveling and acceleration will definitely help. The [first layer speed](printing-variables.md#prusaslicer-print-variables) is especially important and should be 50% or less than the main speed.
* Make sure to use the [Z retract lift](printing-variables.md#prusaslicer-printer-variables) setting in the slicer (lifting the nozzle when traveling).


------------
## Poor Bridging
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

------------
## Spaghetti Monster
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

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

------------
## Stringing & Oozing
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

If the nozzle is not sufficiently tightened, leaks in the hot end can result. During printing, the leaks will appear as strings being left behind on a print; while not printing, the nozzle may be visibly oozing filament. In extreme cases the nozzle may need to be cleaned or replaced. See [Part 1 Step 18](system-assembly--repair.md#part-1--step-18-assembling-the-hot-end) and [Part 3 Step 7](system-assembly--repair.md#part-3--step-7-heat-tightening-the-nozzle).
 
* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/stringing-or-oozing/)

------------
## Ugly Overhangs
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.


------------
## Z Wobble
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.


------------
## Scars on Top Surface
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.


------------
## Blobs and Zits
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.


------------
## Curling or Rough Corners
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

On 2020-02-06, the issue of curling was noticed in addition to the issue of the first layer not sticking to the bed. Both of these problems could be related to overheating. Initially, the bed temperature is set to 70, while the Simplify3d guide suggests 60-70 for PLA. The cooling fan is disabled for the first 3 layers, and the extruder temperature is set to 200 for the first layer and 203 after that.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/curling-or-rough-corners/)

------------
## Overheating
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/overheating/)

------------
## Warping
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

------------
## Vibrations and Ringing
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

------------
## First Layer Not Sticking to the Bed
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-sticking-to-the-bed/)

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

------------
## Grinding or Stripping Filament
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

If the extruder grips the filament too tightly, it creates extra friction, which can result in a screeching noise. The filament can become ground up in the extruder gear, and can even be stripped so much that it fails to push forward at all, ending the print. Take the extruder apart, clean the parts, reposition and check for improvement. The extruder screw should be just tight enough to push the filament into the extruder gear. See [Part 1 Step 19](system-assembly--repair.md#part-1--step-19-assembling-the-extruder).

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/grinding-filament/)

------------
## Clogged Extruder
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/clogged-extruder/)

------------
## Stops Extruding Mid Print
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

If the extruder stops extruding during a print, this problem could be caused at several places, each with the result of not sufficiently gripping the filament. Check the following:
* The extruder screw could be too loose or disconnected.
* The extruder gear could be clogged with shavings from grinding filament.
* The filament itself may have become kinked or have unnecessary friction with the PTFE tube.

Take the extruder cover off and look for problems. If no obvious problem is found, check that the nozzle is not clogged. See [Part 1 Step 19](system-assembly--repair.md#part-1--step-19-assembling-the-extruder).

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/stops-extruding-mid-print/)

------------
## Not Extruding at Start of Print
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-extruding-at-start-of-print/)

------------
## Troubleshooting Data Sources
[Main Page - Related Work and References List](README.md#related-work-and-references)

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
