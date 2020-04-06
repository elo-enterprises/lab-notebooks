# Printing Variables

------------

This page contains data on individual printer variables, as well as a discussion of the software tools used to operate the printer.

------------
## General Discussion
[Main Page - Variables List](README.md#printing-variables)

[System Assembly & Repair - Part 3 Step 08](system-assembly--repair.md#part-3--step-8-printing-settings-for-slicing-software)

[System Assembly & Repair - Part 3 Step 09](system-assembly--repair.md#part-3--step-9-running-your-first-print)

### PrusaSlicer vs Slic3r vs Simplify3D
* The Prusa company, a 3D printer manufacturer, has forked the code for Slic3r and improved the user interface. Modix instructions suggest changing the mode to Expert to gain access to all parameters.
* Simplify3D is proprietary software, recommended by Modix, but it is unclear why Modix prefers this software.

### PrusaSlicer vs Pronterface vs Marlin
* It is not immediately clear how each software layer interacts with the others. Whenever possible, the goal is to allow the PrusaSlicer parameters to dominate the system. This design basis has several implications:
  * Pronterface might not be necessary at all.
  * The bed temperature is set only at the heater box and is thus not adjustable by any software.
  * UBL mesh data, along with the manual overrides to correct weak spots in the validate mesh pattern, are not entered into slicing software and are controlled entirely by Marlin, the printer's firmware.

### Slicing Objects
When slicing an object, PrusaSlicer breaks it down into printer-relevant “feature types”:
* Perimeter
* External Perimeter
* Overhang Perimeter
* Internal Infill
* Solid Infill
* Top Solid Infill
* Bridge Infill
* Gap Fill
* Skirt
* Support Material
* Support Material Interface
* Wipe Tower
* Custom

------------
## PrusaSlicer Plater Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Big60_PLA Value | Elo Value | Units | Notes |
|------------|----------------|-----------|-----------------|-----------|-------|-------|
| General | supports | select list | none | none | none, build plate only, support enforcers only, everywhere | not in the INI file;  |
| General | infill | float | 20 | 100 | % | 3-13 - 40% for strong part, 20% for a solid model; not in the INI file;  |
| General | position X | float | 290 | 290 | mm | not in the INI file;  |
| General | position Y | float | 300 | 300 | mm | not in the INI file;  |
| General | position Z | float | 20.7 | 1 | mm | not in the INI file;  |
| General | rotate X | float | 0 | 0 | degrees | not in the INI file;  |
| General | rotate Y | float | 0 | 0 | degrees | not in the INI file;  |
| General | rotate Z | float | 0 | 0 | degrees | not in the INI file;  |
| General | scale X | float | 50 | 50 | % | not in the INI file;  |
| General | scale Y | float | 50 | 50 | % | not in the INI file;  |
| General | scale Z | float | 50 | 50 | % | not in the INI file;  |

------------
## PrusaSlicer Print Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Big60_PLA Value | Elo Value | Units | Notes |
|------------|----------------|-----------|-----------------|-----------|-------|-------|
| Layers and Perimeters | print_settings_id | text | BIG60_PLA_basicc_onfig.ini | elo-print |  |  |
| Layers and Perimeters | layer_height | float | 0.2 | 0.3 | mm |  |
| Layers and Perimeters | first_layer_height | float | 0.2 | 0.35 | mm or % |  |
| Layers and Perimeters | perimeters | integer | 3 | 3 |  | 3-13 - 3 is a good starting point |
| Layers and Perimeters | spiral_vase | boolean | 0 | 0 |  |  |
| Layers and Perimeters | top_solid_layers | integer | 3 | 3 | layers | 3-13 - 3 is a good starting point, if your model has a lot of top curves, increase to 4 or 5 |
| Layers and Perimeters | bottom_solid_layers | integer | 3 | 3 | layers | 3-13 - start with 3 |
| Layers and Perimeters | extra_perimeters | boolean | 1 | 1 |  |  |
| Layers and Perimeters | ensure_vertical_shell_thickness | boolean | 0 | 0 |  |  |
| Layers and Perimeters | avoid_crossing_perimeters | boolean | 0 | 0 |  |  |
| Layers and Perimeters | thin_walls | boolean | 1 | 1 |  |  |
| Layers and Perimeters | overhangs | boolean | 1 | 1 |  |  |
| Layers and Perimeters | seam_position | select list | Random | Random | Random, Nearest, Aligned, Rear |  |
| Layers and Perimeters | external_perimeters_first | boolean | 0 | 0 |  |  |
| Infill | fill_density | float | 20% | 100% | % |  |
| Infill | fill_pattern | select list | Rectilinear | Rectilinear | Rectilinear, Grid, Triangles, Stars, Cubic, Line, Concentric, Honeycomb, 3D Honeycomb, Gyroid, Hilbert Curve, Archimedean Chords, Octagram Spiral |  |
| Infill | top_fill_pattern | select list | Rectilinear | Rectilinear | Rectilinear, Concentric, Hilbert Curve, Archimedean Chords, Octagram Spiral |  |
| Infill | bottom_fill_pattern | select list | Rectilinear | Rectilinear | Rectilinear, Concentric, Hilbert Curve, Archimedean Chords, Octagram Spiral |  |
| Infill | infill_every_layers | integer | 1 | 1 | layers |  |
| Infill | infill_only_where_needed | boolean | 0 | 0 |  |  |
| Infill | solid_infill_every_layers | integer | 0 | 0 | layers |  |
| Infill | fill_angle | float | 45 | 45 | degrees |  |
| Infill | solid_infill_below_area | float | 70 | 70 | mm2 |  |
| Infill | bridge_angle | float | 0 | 0 | degrees |  |
| Infill | only_retract_when_crossing_perimeters | boolean | 1 | 1 |  |  |
| Infill | infill_first | boolean | 0 | 0 |  |  |
| Skirt and Brim | skirts | integer | 2 | 2 |  |  |
| Skirt and Brim | skirt_distance | float | 10 | 8 | mm |  |
| Skirt and Brim | skirt_height | integer | 1 | 1 | layers |  |
| Skirt and Brim | min_skirt_length | float | 0 | 0 | mm |  |
| Skirt and Brim | brim_width | float | 0 | 0 | mm |  |
| Support Material | support_material | boolean | 1 | 0 |  |  |
| Support Material | support_material_auto | boolean | 1 | 0 |  |  |
| Support Material | support_material_threshold | float | 60 | 0 | degrees |  |
| Support Material | support_material_enforce_layers | integer | 0 | 0 | layers |  |
| Support Material | raft_layers | integer | 0 | 0 | layers |  |
| Support Material | support_material_contact_distance | select list | 0.2  (detachable) | 0.2  (detachable) | 0 (soluble), 0.2  (detachable) |  |
| Support Material | support_material_pattern | select list | Rectilinear | Rectilinear | Rectilinear, Rectilinear Grid, Honeycomb |  |
| Support Material | support_material_with_sheath | boolean | 1 | 1 |  |  |
| Support Material | support_material_spacing | float | 2.5 | 2.5 | mm |  |
| Support Material | support_material_angle | float | 0 | 0 | degrees |  |
| Support Material | support_material_interface_layers | integer | 3 | 3 | layers |  |
| Support Material | support_material_interface_spacing | float | 0 | 0 | mm |  |
| Support Material | support_material_interface_contact_loops | boolean | 0 | 0 |  |  |
| Support Material | support_material_buildplate_only | boolean | 0 | 0 |  |  |
| Support Material | support_material_xy_spacing | float | 50% | 50% | mm or % |  |
| Support Material | dont_support_bridges | boolean | 1 | 1 |  |  |
| Support Material | support_material_synchronize_layers | boolean | 0 | 0 |  |  |
| Speed | perimeter_speed | float | 50 | 60 | mm/s |  |
| Speed | small_perimeter_speed | float | 15 | 15 | mm/s or % |  |
| Speed | external_perimeter_speed | float | 50% | 50% | mm/s or % |  |
| Speed | infill_speed | float | 50 | 80 | mm/s |  |
| Speed | solid_infill_speed | float | 80% | 20 | mm/s or % |  |
| Speed | top_solid_infill_speed | float | 80% | 15 | mm/s or % |  |
| Speed | support_material_speed | float | 60 | 60 | mm/s |  |
| Speed | support_material_interface_speed | float | 100% | 100% | mm/s or % |  |
| Speed | bridge_speed | float | 80 | 60 | mm/s |  |
| Speed | gap_fill_speed | float | 20 | 20 | mm/s |  |
| Speed | travel_speed | float | 70 | 130 | mm/s |  |
| Speed | first_layer_speed | float | 30% | 30 | mm/s or % |  |
| Speed | perimeter_acceleration | float | 0 | 0 | mm/s2 |  |
| Speed | infill_acceleration | float | 0 | 0 | mm/s2 |  |
| Speed | bridge_acceleration | float | 0 | 0 | mm/s2 |  |
| Speed | first_layer_acceleration | float | 0 | 0 | mm/s2 |  |
| Speed | default_acceleration | float | 0 | 0 | mm/s2 |  |
| Speed | max_print_speed | float | 80 | 50 | mm/s | 3-13 - start with 50mm/s and increase for draft up to 100 mm/s, can be as slow as 40 for a detailed print (or even slower for maximum detail) |
| Speed | max_volumetric_speed | float | 0 | 0 | mm3/s |  |
| Multiple Extruders | perimeter_extruder | integer | 1 | 1 |  |  |
| Multiple Extruders | infill_extruder | integer | 1 | 1 |  |  |
| Multiple Extruders | solid_infill_extruder | integer | 1 | 1 |  |  |
| Multiple Extruders | support_material_extruder | integer | 1 | 1 |  |  |
| Multiple Extruders | support_material_interface_extruder | integer | 1 | 1 |  |  |
| Multiple Extruders | ooze_prevention | boolean | 0 | 0 |  |  |
| Multiple Extruders | standby_temperature_delta | float | -10 | -5 | C |  |
| Multiple Extruders | wipe_tower | boolean | 0 | 0 |  |  |
| Multiple Extruders | wipe_tower_x | float | 180 | 180 | mm |  |
| Multiple Extruders | wipe_tower_y | float | 140 | 140 | mm |  |
| Multiple Extruders | wipe_tower_width | float | 60 | 60 | mm |  |
| Multiple Extruders | wipe_tower_rotation_angle | float | 0 | 0 | degrees |  |
| Multiple Extruders | wipe_tower_bridging | float | 10 | 10 | mm |  |
| Multiple Extruders | single_extruder_multi_material_priming | boolean |  | 1 |  |  |
| Multiple Extruders | interface_shells | boolean | 0 | 0 |  |  |
| Advanced | extrusion_width | float | 0 | 0.45 | mm or % |  |
| Advanced | first_layer_extrusion_width | float | 100% | 0.42 | mm or % |  |
| Advanced | perimeter_extrusion_width | float | 0 | 0.45 | mm or % |  |
| Advanced | external_perimeter_extrusion_width | float | 0 | 0.45 | mm or % |  |
| Advanced | infill_extrusion_width | float | 0 | 0.45 | mm or % |  |
| Advanced | solid_infill_extrusion_width | float | 0 | 0.45 | mm or % |  |
| Advanced | top_infill_extrusion_width | float | 0 | 0.4 | mm or % |  |
| Advanced | support_material_extrusion_width | float | 0 | 0.35 | mm or % |  |
| Advanced | infill_overlap | float | 25% | 25% | mm or % |  |
| Advanced | bridge_flow_ratio | float | 1 | 1 |  |  |
| Advanced | slice_closing_radius | float | 0.049 | 0.049 | mm |  |
| Advanced | resolution | float | 0 | 0 | mm |  |
| Advanced | xy_size_compensation | float | 0 | 0 | mm |  |
| Advanced | elefant_foot_compensation | float | 0 | 0 | mm |  |
| Advanced | clip_multipart_objects | boolean | 0 | 0 |  |  |
| Output Options | complete_objects | boolean | 0 | 0 |  |  |
| Output Options | extruder_clearance_radius | float | 20 | 20 | mm |  |
| Output Options | extruder_clearance_height | float | 20 | 20 | mm |  |
| Output Options | gcode_comments | boolean | 0 | 0 |  |  |
| Output Options | gcode_label_objects | boolean | 0 | 0 |  |  |
| Output Options | output_filename_format | text | [input_filename_base].gcode | [input_filename_base].gcode |  |  |
| Output Options | post_process | script text |  |  |  |  |
| Notes | notes | text |  |  |  |  |

------------
## PrusaSlicer Filament Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Big60_PLA Value | Elo Value | Units | Notes |
|------------|----------------|-----------|-----------------|-----------|-------|-------|
| Filament | filament_settings_id | text | BIG60_PLA_basicc_onfig.ini | elo-filament |  |  |
| Filament | filament_colour | color code | #1100B2 | #1100B2 |  |  |
| Filament | filament_diameter | float | 1.75 | 1.75 | mm |  |
| Filament | extrusion_multiplier | float | 1 | 1 |  | 3-13 - lower to 0.9 for models that have moving parts or need high accuracy, make it 1.15 for thin wall parts that need some extra strength. |
| Filament | filament_density | float | 0 | 0 | g/cm3 |  |
| Filament | filament_cost | float | 0 | 0 | money/kg |  |
| Filament | first_layer_temperature | float | 220 | 200 | C | 3-13 - keep at 230°C for PLA to get a good first layer |
| Filament | temperature | float | 210 | 203 | C | 3-13 - keep around 210-220°C for PLA, depends on the filament provider |
| Filament | first_layer_bed_temperature | float | 0 | 0 | C | this field can only be set at the printer |
| Filament | bed_temperature | float | 0 | 0 | C | this field can only be set at the printer |
| Cooling | fan_always_on | boolean | 0 | 0 |  |  |
| Cooling | cooling | boolean | 1 | 1 |  |  |
| Cooling | min_fan_speed | float | 35 | 35 | % |  |
| Cooling | max_fan_speed | float | 100 | 100 | % |  |
| Cooling | bridge_fan_speed | float | 100 | 100 | % |  |
| Cooling | disable_fan_first_layers | integer | 1 | 3 |  |  |
| Cooling | fan_below_layer_time | float | 60 | 60 | s |  |
| Cooling | slowdown_below_layer_time | float | 5 | 5 | s |  |
| Cooling | min_print_speed | float | 10 | 10 | mm/s |  |
| Advanced | filament_type | select list | PLA | PLA | PLA, ABS, PET, FLEX, HIPS, EDGE, NGEN, NYLON, PVA, PC, PP, PEI, PEEK, PEKK, POM, PSU, PVDF, SCAFF |  |
| Advanced | filament_soluble | boolean | 0 | 0 |  |  |
| Advanced | filament_max_volumetric_speed | float | 0 | 0 | mm3/s |  |
| Advanced | filament_minimal_purge_on_wipe_tower | float | 15 | 15 | mm3 |  |
| Advanced | filament_loading_speed_start | float | 3 | 3 | mm/s |  |
| Advanced | filament_loading_speed | float | 28 | 28 | mm/s |  |
| Advanced | filament_unloading_speed_start | float | 100 | 100 | mm/s |  |
| Advanced | filament_unloading_speed | float | 90 | 90 | mm/s |  |
| Advanced | filament_load_time | float | 0 | 0 | s |  |
| Advanced | filament_unload_time | float | 0 | 0 | s |  |
| Advanced | filament_toolchange_delay | float | 0 | 0 | s |  |
| Advanced | filament_cooling_moves | integer | 4 | 4 |  |  |
| Advanced | filament_cooling_initial_speed | float | 2.2 | 2.2 | mm/s |  |
| Advanced | filament_cooling_final_speed | float | 3.4 | 3.4 | mm/s |  |
| Advanced | filament_ramming_parameters | - |  | 120 100 6.6 6.8 7.2 7.6 7.9 8.2 8.7 9.4 9.9 10.0 0.05 6.6 0.45 6.8 0.95 7.8 1.45 8.3 1.95 9.7 2.45 10 2.95 7.6 3.45 7.6 3.95 7.6 4.45 7.6 4.95 7.6 | - |  |
| Filament Overrides | filament_retract_length | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_lift | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_lift_above | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_lift_below | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_speed | float | nil | nil | mm/s |  |
| Filament Overrides | filament_deretract_speed | float | nil | nil | mm/s |  |
| Filament Overrides | filament_retract_restart_extra | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_before_travel | float | nil | nil | mm |  |
| Filament Overrides | filament_retract_layer_change | boolean | nil | nil |  |  |
| Filament Overrides | filament_wipe | boolean | nil | nil |  |  |
| Filament Overrides | filament_retract_before_wipe | float | nil | nil | % |  |
| Custom G-Code | start_filament_gcode | g-code | ; Filament gcode\n | ; Filament gcode\n |  |  |
| Custom G-Code | end_filament_gcode | g-code | ; Filament-specific end gcode \n;END gcode for filament\n | ; Filament-specific end gcode \n;END gcode for filament\n |  |  |
| Filament Notes | filament_notes | text |  |  |  |  |

------------
## PrusaSlicer Printer Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Big60_PLA Value | Elo Value | Units | Notes |
|------------|----------------|-----------|-----------------|-----------|-------|-------|
| General | printer_settings_id | text | BIG60_PLA_basicc_onfig.ini | elo-printer |  |  |
| General | bed_shape | float | 0x0,600x0,600x600,0x600 | 0x0,580x0,580x600,0x600 | mm | 3-09, set the bed shape to match the big60 |
| General | max_print_height | float | 200 | 200 | mm |  |
| General | z_offset | float | 0 | 0 | mm | 3-06-04 - Modix said that values in this field in PrusaSlicer will override the value in Marlin |
| General | "Extruders" | integer | 1 | 1 |  |  |
| General | single_extruder_multi_material | boolean | 0 | 0 |  |  |
| General | host_type | select list | OctoPrint | OctoPrint | Octoprint, Duet |  |
| General | printhost_cafile | file |  |  |  |  |
| General | printhost_apikey | api key |  |  |  |  |
| General | gcode_flavor | select list | RepRap/Sprinter | Marlin | RepRap/Sprinter, Repetier, Teacup, MakerWare, Marlin, Sailfish, Mach3/LinuxCNC, Machinekit, Smoothie, No Extrusion |  |
| General | silent_mode | boolean | 1 | 1 |  |  |
| General | remaining_times | boolean | 0 | 0 |  |  |
| General | use_relative_e_distances | boolean | 0 | 0 |  |  |
| General | use_firmware_retraction | boolean | 0 | 0 |  |  |
| General | use_volumetric_e | boolean | 0 | 0 |  |  |
| General | variable_layer_height | boolean | 1 | 1 |  |  |
| Custom G-Code | start_gcode | g-code | G28 ; home all axes | G28 ; home all axes\nG1 Z5 F5000 ; lift nozzle\n |  | 3-09 added per instructions |
| Custom G-Code | end_gcode | g-code | M104 S0 ; turn off temperature\nG28 X0  ; home X axis\nM84     ; disable motors\n | M104 S0 ; turn off temperature\nG28 X0  ; home X axis\nM84     ; disable motors\n |  | 3-09 added per instructions |
| Custom G-Code | before_layer_gcode | g-code |  |  |  |  |
| Custom G-Code | layer_gcode | g-code |  |  |  |  |
| Custom G-Code | toolchange_gcode | g-code |  |  |  |  |
| Custom G-Code | between_objects_gcode | g-code |  |  |  |  |
| Machine Limits | machine_max_feedrate_x | float |  | 500, 200 | mm/s, mm/s |  |
| Machine Limits | machine_max_feedrate_y | float |  | 500, 200 | mm/s, mm/s |  |
| Machine Limits | machine_max_feedrate_z | float |  | 12, 12 | mm/s, mm/s |  |
| Machine Limits | machine_max_feedrate_e | float |  | 120, 120 | mm/s, mm/s |  |
| Machine Limits | machine_max_acceleration_x | float |  | 90, 10, 000 | dm/s2, dm/s2 |  |
| Machine Limits | machine_max_acceleration_y | float |  | 90, 10, 000 | dm/s2, dm/s2 |  |
| Machine Limits | machine_max_acceleration_z | float |  | 500, 200 | mm/s2, mm/s2 |  |
| Machine Limits | machine_max_acceleration_e | float |  | 100, 50, 000 | dm/s2, dm/s2 |  |
| Machine Limits | machine_max_acceleration_extruding | float |  | 15, 001, 250 | dm/s2, dm/s2 |  |
| Machine Limits | machine_max_acceleration_retracting | float |  | 15, 001, 250 | dm/s2, dm/s2 |  |
| Machine Limits | machine_max_jerk_x | float |  | 10, 10 | mm/s, mm/s |  |
| Machine Limits | machine_max_jerk_y | float |  | 10, 10 | mm/s, mm/s |  |
| Machine Limits | machine_max_jerk_z | float |  | 0.2, 0.4 | mm/s, mm/s |  |
| Machine Limits | machine_max_jerk_e | float |  | 2.5, 2.5 | mm/s, mm/s |  |
| Machine Limits | machine_min_extruding_rate | float |  | 0, 0 | mm/s, mm/s |  |
| Machine Limits | machine_min_travel_rate | float |  | 0, 0 | mm/s, mm/s |  |
| Extruder 1 | nozzle_diameter | float | 0.4 | 0.4 | mm | 3-09 set per the nozzle |
| Extruder 1 | min_layer_height | float | 0.07 | 0.07 | mm |  |
| Extruder 1 | max_layer_height | float | 0 | 0 | mm |  |
| Extruder 1 | extruder_offset | float | 0x0 | 0x0 | mm, mm |  |
| Extruder 1 | retract_length | float | 2 | 2 | mm |  |
| Extruder 1 | retract_lift | float | 0.2 | 0 | mm |  |
| Extruder 1 | retract_lift_above | float | 0 | 0 | mm |  |
| Extruder 1 | retract_lift_below | float | 0 | 0 | mm |  |
| Extruder 1 | retract_speed | float | 40 | 40 | mm/s |  |
| Extruder 1 | deretract_speed | float | 0 | 0 | mm/s |  |
| Extruder 1 | retract_restart_extra | float | 0 | 0 | mm |  |
| Extruder 1 | retract_before_travel | float | 3 | 2 | mm |  |
| Extruder 1 | retract_layer_change | boolean | 1 | 1 |  |  |
| Extruder 1 | wipe | boolean | 0 | 0 |  |  |
| Extruder 1 | retract_before_wipe | float | 0% | 0% | % |  |
| Extruder 1 | retract_length_toolchange | float | 10 | 10 | mm |  |
| Extruder 1 | retract_restart_extra_toolchange | float | 0 | 0 | mm |  |
| Extruder 1 | extruder_colour | color code |  |  |  |  |
| Printer Notes | printer_notes |  |  |  |  |  |

------------
## PrusaSlicer Unidentified INI Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Big60_PLA Value | Elo Value | Units | Notes |
|------------|----------------|-----------|-----------------|-----------|-------|-------|
| bed_custom_model |  |  |  |  |  |
| bed_custom_texture |  |  |  |  |  |
| colorprint_heights |  |  |  |  |  |
| cooling_tube_length |  | 5 |  |  |  |
| cooling_tube_retraction |  | 91.5 |  |  |  |
| default_filament_profile |  |  |  |  |  |
| default_print_profile |  |  |  |  |  |
| duplicate_distance |  | 6 |  |  |  |
| extra_loading_move |  | -2 |  |  |  |
| extrusion_axis |  | E |  |  |  |
| high_current_on_filament_swap |  | 0 |  |  |  |
| parking_pos_retraction |  | 92 |  |  |  |
| print_host |  |  |  |  |  |
| printer_model |  |  |  |  |  |
| printer_technology |  | FFF |  |  |  |
| printer_variant |  |  |  |  |  |
| printer_vendor |  |  |  |  |  |
| serial_port |  |  |  |  |  |
| serial_speed |  | 250000 |  |  |  |
| threads |  | 4 |  |  |  |
| thumbnails |  |  |  |  |  |
| wipe_into_infill |  | 0 |  |  |  |
| wipe_into_objects |  | 0 |  |  |  |
| wiping_volumes_extruders |  | 70, 70 |  |  |  |
| wiping_volumes_matrix |  | 0 |  |  |  |

------------
## Marlin Variables
[Main Page - Variables List](README.md#printing-variables)

| Group Name | Parameter Name | Data Type | Parameter Value | Units | Notes |
|------------|----------------|-----------|-----------------|-------|-------|
| Tuning | Speed | integer | 100 |  |  |
| Tuning | Fade Height | integer | 0 |  |  |
| Tuning | Nozzle 1 | integer | 200 |  |  |
| Tuning | Nozzle 2 | integer | 0 |  |  |
| Tuning | Fan Speed | integer | 0 |  |  |
| Tuning | Flow | integer | 100 |  |  |
| Tuning | Flow 1 | integer | 100 |  |  |
| Tuning | Flow 2 | integer | 100 |  |  |
| Tuning | Probe Z Offset | float | -0.700 |  |  |
| Control - Temperature | Nozzle 1 | integer | 0 |  |  |
| Control - Temperature | Nozzle 2 | integer | 0 |  |  |
| Control - Temperature | Fan Speed | integer | 0 |  |  |
| Control - Temperature | Autotemp | On-Off | Off |  |  |
| Control - Temperature | Min | integer | 0 |  |  |
| Control - Temperature | Max | integer | 250 |  |  |
| Control - Temperature | Fact | float | 0.1 |  |  |
| Control - Temperature | PID-P | float | 22.2 |  |  |
| Control - Temperature | PID-I | float | 1.08 |  |  |
| Control - Temperature | PID-D | float | 59.5 |  |  |
| Control - Motion - Velocity | Vmax X | integer | 500 |  |  |
| Control - Motion - Velocity | Vmax Y | integer | 500 |  |  |
| Control - Motion - Velocity | Vmax Z | integer | 12 |  |  |
| Control - Motion - Velocity | Vmax E | integer | 120 |  |  |
| Control - Motion - Velocity | Vmin | integer | 0 |  |  |
| Control - Motion - Velocity | Vtrav min | integer | 0 |  |  |
| Control - Motion - Acceleration | Accel | integer | 1500 |  |  |
| Control - Motion - Acceleration | A-retract | integer | 1500 |  |  |
| Control - Motion - Acceleration | A-travel | integer | 1500 |  |  |
| Control - Motion - Acceleration | Amax X | integer | 9000 |  |  |
| Control - Motion - Acceleration | Amax Y | integer | 9000 |  |  |
| Control - Motion - Acceleration | Amax Z | integer | 500 |  |  |
| Control - Motion - Acceleration | Amax E | integer | 10000 |  |  |
| Control - Motion - Jerk | Vx-jerk | integer | 10 |  |  |
| Control - Motion - Jerk | Vy-jerk | integer | 10 |  |  |
| Control - Motion - Jerk | Vz-jerk | float | 0.2 |  |  |
| Control - Motion - Jerk | Ve-jerk | integer | 3 |  |  |
| Control - Motion - Steps-mm | Xsteps-mm | float | 200 |  |  |
| Control - Motion - Steps-mm | Ysteps-mm | float | 100 |  |  |
| Control - Motion - Steps-mm | Zsteps-mm | float | 2000 |  |  |
| Control - Motion - Steps-mm | Esteps-mm | float | 418.5 |  |  |
| Control - Filament | Advance K | float | 0 |  |  |
| Control - Filament | E in mm3 |On-Off | Off |  |  |
| Control - Filament | Unload mm | integer | 100 |  |  |
| Control - Filament | Unload mm 1 | integer | 100 |  |  |
| Control - Filament | Unload mm 2 | integer | 100 |  |  |
| Control - Filament | Load mm | integer | 0 |  |  |
| Control - Filament | Load mm 1 | integer | 0 |  |  |
| Control - Filament | Load mm 2 | integer | 0 |  |  |
