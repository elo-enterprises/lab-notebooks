# Troubleshooting Issues

------------

This page contains data on problems encountered in printer operation, as well as a list of troubleshooting references at the bottom of the page.


------------
## Current Issues

EEPROM / UBL Fine-Tuning
* produce grid of small parts across the entire bed

Grinding / Stripping Filament

Install Casters

Test Detailed Hot End

Purchase Supervolcano 3mm Hot End Package

------------
## Z Motors Binding Up
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

When first turning the printer on, serious trouble with the Z motors was encountered, prompting repeated customer support interactions with Modix. The motors could lower the bed down correctly. When going up, however, seemingly at random, the motors would encounter friction and try to move without moving the bed up. The printer was turned off before causing further damage. Modix sent a checklist of potential issues:
* Before leveling the bed, make sure to level the base frame.
* Try to move each screw manually in both directions when the ball screws are disassembled from the bed brackets. See [Part 1 Step 09](system-assembly--repair.md#part-1--step-9-assembling-the-z-axis-mid-brackets)
* Check the bottom shaft of each ball screw. Make sure it does not sit all the way down; the base of the ball screws should not touch the base of the pillow bearings, or excess friction will result. See [Part 1 Step 10](system-assembly--repair.md#part-1--step-10-assembling-the-z-axis-sets).
* Make sure that all pulleys and gears are well tightened and do not slip. See [Part 1 Step 10](system-assembly--repair.md#part-1--step-10-assembling-the-z-axis-sets) and [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Check whether the belts that drive the ball screws are tightened too much. They need to be tightened to the point that they sit straight and do not sag and no further. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
* Try to move each screw individually with the spare motor cable. Make sure they are moving smoothly. Look for damaged wire connections on the Z cable and on the motors. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the Z motors with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Check the current on the stepper driver with a multimeter. It should be no more than 1.2V. The way to measure it is to set the multimeter to 2V, red pin on the Vref, black pin on the GND pin on the stepper driver. If the current is lower than 1.2V, turn the Vref (potentiometer) clockwise, no more than 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Check that there is nothing wrong with the firmware settings. Connect to Pronterface and send Modix the output log once connected or send command M503. See [Part 3 Step 05](system-assembly--repair.md#part-3--step-5-terminal-software-and-basic-g-code).

------------
## Stripped Set Screws
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

At several steps, the 3mmx3mm set screws used to tighten gears stripped. 
* Take extra care to tighten the set screws effectively to the flat sides of the motors to avoid problems with the motors spinning freely without turning the pulleys.
* To avoid causing damage requiring replacement of more expensive parts, the 3mmx3mm set screws were replaced with externally purchased [4mmx3mm set screws](parts-lists.md#tools). These screws added more contact surface area between the inside of the screw and the hex key. A new [hex key](parts-lists.md#tools) was also used, and no further stripping was detected. See the following steps: 
  * [Part 1 Step 08](system-assembly--repair.md#part-1--step-8-assembling-the-z-axis-bottom-brackets);
  * [Part 1 Step 09](system-assembly--repair.md#part-1--step-9-assembling-the-z-axis-mid-brackets);
  * [Part 1 Step 12](system-assembly--repair.md#part-1--step-12-installing-the-x-shaft);
  * [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).

------------
## LCD Screen Button Friction
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

The main LCD screen button is vulnerable to a relatively serious problem. In the case of excess friction, the main LCD screen button can trigger the click action while turning to scroll through options lists. Removing the plastic cover from the button and using the metal knob underneath suffices as a temporary solution. //TODO: Replace the button and contact customer support if the problem persists. See [Part 1 Step 22](system-assembly--repair.md#part-1--step-22-assembling-the-lcd-screen).

------------
## Layer Shifts
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

[Operating Procedures - Calibration - Validate Mesh](operating-procedures.md#validate-mesh-calibration-procedure)

Layer shifts were a serious early issue. When printing test patterns, circles printed as ellipses. In correspondence, Modix customer support indicated that this problem is caused by the Y axis not being perfectly square and supplied the following checklist:

### Y Axis
* Make sure the belts on the Y axis and on the Y motor are tightened and do not slip. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors) and [Part 1 Step 15](system-assembly--repair.md#part-1--step-15-installing-the-y-axis-timing-belt).
* Make sure the wiring is not loose or torn either on the controller board or on the Y motor. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Make sure that the stepper driver for the Y motor has enough current. It should be no more than 1.1 V, as low as possible. The current can be increased by turning the Vref clockwise 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the Y motor with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).

### X Axis
* Make sure the pulleys on the X shaft and on the X motor are tightened and do not slip. See [Part 1 Step 12](system-assembly--repair.md#part-1--step-12-installing-the-x-shaft) and [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors).
  * Make sure the Y axis rail is parallel to the X shaft and does not have an angle. See [Part 1 Step 13](system-assembly--repair.md#part-1--step-13-assembling-the-y-axis). To reposition the Y axis, 
    * loosen the front X idler and the set screw of the pulley connecting the front X belt to the X shaft;
    * loosen the front X belt;
    * connect the Y axis to the frame using the calibration jigs;
    * loosen the screws holding the Y axis profile to the X rails;
    * tighten the X belt;
    * tighten the Y axis screws;
    * tighten the pulley connecting the front X belt to the X shaft and the X idler;
    * remove the calibration jigs.
* Make sure the belts on the X axis and on the X motor are tightened and do not slip. See [Part 1 Step 14](system-assembly--repair.md#part-1--step-14-installing-the-motors), [Part 1 Step 16](system-assembly--repair.md#part-1--step-16-installing-the-timing-belt-at-the-back-x-axis) and [Part 1 Step 17](system-assembly--repair.md#part-1--step-17-installing-the-timing-belt-at-the-front-x-axis).
* Make sure the wiring is not loose or torn either on the controller board or on the X motor. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Make sure that the stepper driver for the X motor has enough current. It should be no more than 1.1 V, as low as possible. The current can be increased by turning the Vref clockwise 1/4 turn at a time. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* Replace the stepper driver for the X motor with one of the spares. See [Part 2 Step 01](system-assembly--repair.md#part-2--step-1-wiring-the-motors-and-end-stops).
* To be completely thorough, revisit [Part 2 Step 15](system-assembly--repair.md#part-2--step-15-tightening-all-screws), loosen and tighten the screws, being extremely careful to measure right angles. 

### Overall
* Make sure that the fan on the electronics box is working and successfully cooling the stepper drivers. See [Part 2 Step 04](system-assembly--repair.md#part-2--step-4-installing-the-electronics-box-cover).
* Reducing [printing speed](printing-variables.md#prusaslicer-print-variables) (40-50mm/s), traveling and acceleration will definitely help. The [first layer speed](printing-variables.md#prusaslicer-print-variables) is especially important and should be 50% or less than the main speed.
* Make sure to use the [Z retract lift](printing-variables.md#prusaslicer-printer-variables) setting in the slicer (lifting the nozzle when traveling).

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/layer-shifting/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#layers-shifting-misaligned-layers-19)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue8)

------------
## Poor Bridging
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/poor-bridging/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#poor-bridging-37)
  
------------
## Spaghetti Monster
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

On the print MU75_joint_ring_extension, the same failure scenario was encountered twice. The object is a tall cylinder, which means it does not have a lot of surface area to bind with the bed. Both times, ~75% of the object built correctly, and on a layer in which four columns are recombined to form a circle, the printer head pushed the object off the bed. 

<center>
<table>
  <tr>
    <td><a href=img/Troubleshooting_Spaghetti_Cylinder_1.jpg><img src=img/Troubleshooting_Spaghetti_Cylinder_1.jpg width=550px></a></td>
    <td><a href=img/Troubleshooting_Spaghetti_Cylinder_2.jpg><img src=img/Troubleshooting_Spaghetti_Cylinder_2.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure TSpaghetti1 - Cylinder 1</p></td>
    <td><p align="center">Figure TSpaghetti2 - Cylinder 2</p></td>
  </tr>
  <tr>
    <td><a href=img/Troubleshooting_Spaghetti_Dome_1.jpg><img src=img/Troubleshooting_Spaghetti_Dome_1.jpg width=550px></a></td>
    <td><a href=img/Troubleshooting_Spaghetti_Dome_2.jpg><img src=img/Troubleshooting_Spaghetti_Dome_2.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure TSpaghetti3 - Dome 1</p></td>
    <td><p align="center">Figure TSpaghetti4 - Dome 2</p></td>
  </tr>
  <tr>
    <td><a href=img/Troubleshooting_Spaghetti_Array.jpg><img src=img/Troubleshooting_Spaghetti_Array.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure TSpaghetti5 - Array of Objects</p></td>
  </tr>
</table>
</center>

------------
## Stringing & Oozing
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

If the nozzle is not sufficiently tightened, leaks in the hot end can result. During printing, the leaks will appear as strings being left behind on a print; while not printing, the nozzle may be visibly oozing filament. In extreme cases, the nozzle may need to be cleaned or replaced. See [Part 1 Step 18](system-assembly--repair.md#part-1--step-18-assembling-the-hot-end) and [Part 3 Step 7](system-assembly--repair.md#part-3--step-7-heat-tightening-the-nozzle).
 
* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/stringing-or-oozing/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#stringing-and-oozing-13)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue9)

------------
## Ugly Overhangs
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue, also known as "Poor Surface Above Supports," presents as visibly poor surface quality directly above supports, or in overhangs where there is no support underneath.
* The first solution to try is lowering the Layer Height setting in the slicer. By dropping the height of each layer, more layers will be printed, allowing for a smoother surface without need of supports. Of course, this technique will result in a longer print time.
* The second solution to try is to adjust the Support Infill Percentage setting in the slicer. If supports are designed too densely, they will be difficult to remove from the finished part, leading to situations where less-dense supports could effectively support the structure but are not used to avoid more-dense supports.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/poor-surface-above-supports/)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue10)

------------
## Z Wobble
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue14)
  
------------
## Scars on Top Surface
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue presents literally from the nozzle being too close to the print, scraping as it moves and creating the appearance of scars.
* The first solution to try is adjusting the Z Offset. Adding even half a millimeter in extra space between the nozzle and the print can help. In addition, consider readjusting the UBL mesh if the problem occurs consistently in some parts of the bed but not in others.
* The second solution to try is making sure the printer is not extruding too much plastic. See the [Over-Extrusion](#over-extrusion) section for details.
* The third solution to try is to make sure the Z Lift setting is enabled in the slicer. This will cause the print head to raise relative to the bed while moving and not extruding, minimizing the time that the print head is close to the surface.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/scars-on-top-surface/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#scratches-on-top-layers-26)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue17)
  
------------
## Over-Extrusion
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue presents as a deformed print, lines that are not crisp, lines that overlap with each other and change the size and shape of the print in progress. 
* The first solution to try is to verify that the filament diameter is correctly recorded in the slicer. Also check the Extrusion Multiplier setting. Manually reducing this setting can ameliorate the problem.
* Several variables could potentially impact the amount of plastic extruded, and on 2020-04-11 it is unclear exactly how these variables interact within the slicer. It is possible that the problem is in the interaction of inconsistent variables, though adjusting the Extrusion Multiplier could potentially override the visible outcome without addressing the underlying variables. These include
  * printing speed; 
  * printing flow rate;
  * layer height;
  * printing thickness.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/over-extrusion/)
  
------------
## Blobs and Zits
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/blobs-and-zits/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#blobs-and-3d-printing-zits-24)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue18)
  
------------
## Curling or Rough Corners
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

On 2020-02-06, the issue of curling was noticed in addition to the issue of the first layer not sticking to the bed. Both of these problems could be related to overheating. Initially, the bed temperature was set to 70, while the Simplify3d guide suggests 60-70 for PLA. The cooling fan was disabled for the first 3 layers, and the extruder temperature was set to 200 for the first layer and 203 for all other layers.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/curling-or-rough-corners/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#curling-and-rough-corners-17)

------------
## Overheating
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#overheating-14)
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/overheating/)

------------
## Warping
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/warping/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#warping-4)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue6)

------------
## Vibrations and Ringing
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/vibrations-and-ringing/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#vibrations-and-3d-printing-ringing-31)
  
------------
## First Layer Not Sticking to the Bed
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

[Operating Procedures - Calibration - Validate Mesh](operating-procedures.md#validate-mesh-calibration-procedure)

The issue of the first layer not sticking to the bed has several possible causes, such as 
 * the bed is not level;
 * the nozzle starts too far away from the bed;
 * the first layer is printing too fast;
 * incorrect temperature or cooling settings;
 * problems with the bed surface.

On 2020-02-06, the issue of curling was noticed in addition to the issue of the first layer not sticking to the bed. Both of these problems could be related to overheating. Initially, the bed temperature was set to 70, while the Simplify3d guide suggests 60-70 for PLA. The cooling fan was disabled for the first 3 layers, and the extruder temperature was set to 200 for the first layer and 203 for all other layers.

The first layer speed was set to 30 mm/s. The Z offset was set to -0.7mm.

Testing
 * For the first test, the bed temperature was lowered to 65 and the bed surface was cleaned with isopropyl alcohol. This did not solve the problem, and the first layer was still not sticking.
 * For the second test, after starting the print, the Z offset was tuned to -0.75mm. The problem persisted, with a few notes: 
   * The test print first layer consists of thin circular walls, which could be more difficult to make the first layer stick than e.g. a single rectangle with a more continuous surface area. 
   * The circles in the middle Y with higher X stick better than the others, which could be explained by differences in height across the bed.
  * For the third test, the first layer speed was lowered to 30% of the 50 mm/s total, rather than 30 mm/s, leaving the Z offset at -0.75. The first layer successfully stuck to the bed.
<center>
<table>
  <tr>
    <td><a href=img/Troubleshooting_1stLayerNotSticking_1.jpg><img src=img/Troubleshooting_1stLayerNotSticking_1.jpg width=550px></a></td>
   <td><a href=img/Troubleshooting_1stLayerNotSticking_2.jpg><img src=img/Troubleshooting_1stLayerNotSticking_2.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure T1stLayer1</p></td>
    <td><p align="center">Figure T1stLayer2</p></td>
  </tr>
</table>
</center>

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-sticking-to-the-bed/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#print-not-sticking-to-the-bed-2)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue2)

------------
## Grinding or Stripping Filament
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

If the extruder grips the filament too tightly, it creates extra friction, which can result in a screeching noise. The filament can become ground up in the extruder gear, and can even be stripped so much that it fails to push forward at all, ending the print. Take the extruder apart, clean the parts, reposition and check for improvement. The extruder screw should be just tight enough to push the filament into the extruder gear. See [Part 1 Step 19](system-assembly--repair.md#part-1--step-19-assembling-the-extruder).
<center>
<table>
  <tr>
    <td><a href=img/Troubleshooting_Grinding_Filament.jpg><img src=img/Troubleshooting_Grinding_Filament.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure TGrinding1 - Stripped Filament Shavings</p></td>
  </tr>
</table>
</center>

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/grinding-filament/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#extruder-is-grinding-filament-8)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue13)

------------
## Clogged Extruder
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue has not yet been encountered.

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/clogged-extruder/)
  * [Rigid.Ink](https://rigid.ink/pages/ultimate-troubleshooting-guide#clogged-nozzle-11)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue3)

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
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue20)
  
------------
## Not Extruding at Start of Print
[Main Page - Troubleshooting Issues List](README.md#troubleshooting-issues)

This issue was briefly encountered during early testing. Several different problems can cause this result, including a clogged nozzle. In this case, the problem disappeared after replacing the Modix-supplied INI file with a custom Elo INI without ever truly understanding what caused the problem.
<center>
<table>
  <tr>
    <td><a href=img/Troubleshooting_NotExtrudingAtStart.jpg><img src=img/Troubleshooting_NotExtrudingAtStart.jpg width=550px></a></td>
  </tr>
  <tr>
    <td><p align="center">Figure TNotExtrudingAtStart1</p></td>
  </tr>
</table>
</center>

* Articles:
  * [Simplify3D Print Quality Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/not-extruding-at-start-of-print/)
  * [Matter Hackers](https://www.matterhackers.com/articles/3d-printer-troubleshooting-guide#Issue1)

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
