# Traffic sign detection 

The inference results are provided in the eCAL topic `traffic_sign_detection` as JSON data. The following example show how an object could look like:

```json
{
    "iso_timestamp": "2024-11-04T12:50:48.697684",
    // Class labels for each detected traffic sign
    "class_ids": [
        22.0, // info_crosswalk
        40.0 // priority_stop
    ],
    // Confidence scores for detected traffic sign
    "confidences": [
        0.7705173492431641, // confidence info_crosswalk
        0.29842549562454224 // confidence priority_stop
    ]
}
```

The following table describes the class ids with the corresponding lables:

| Class ID | Label Name                            |
|----------|---------------------------------------|
|        0 | prohibitory_no_entry                  |
|        1 | prohibitory_left                      |
|        2 | prohibitory_overtake                  |
|        3 | prohibitory_right                     |
|        4 | prohibitory_speed_limit_10            |
|        5 | prohibitory_speed_limit_100           |
|        6 | prohibitory_speed_limit_130           |
|        7 | prohibitory_speed_limit_20            |
|        8 | prohibitory_speed_limit_30            |
|        9 | prohibitory_speed_limit_40            |
|       10 | prohibitory_speed_limit_5             |
|       11 | prohibitory_speed_limit_50            |
|       12 | prohibitory_speed_limit_60            |
|       13 | prohibitory_speed_limit_70            |
|       14 | prohibitory_speed_limit_80            |
|       15 | prohibitory_speed_limit_90            |
|       16 | prohibitory_stopping                  |
|       17 | prohibitory_trucks                    |
|       18 | prohibitory_u_turn                    |
|       19 | prohibitory_weight_over_3.5t          |
|       20 | prohibitory_weight_over_7.5t          |
|       21 | info_bus_station                      |
|       22 | info_crosswalk                        |
|       23 | info_highway                          |
|       24 | info_one_way_traffic                  |
|       25 | info_parking                          |
|       26 | info_taxi_parking                     |
|       27 | mandatory_bike_lane                   |
|       28 | mandatory_left                        |
|       29 | mandatory_left_right                  |
|       30 | mandatory_pass_left                   |
|       31 | mandatory_pass_left_right             |
|       32 | mandatory_pass_right                  |
|       33 | mandatory_right                       |
|       34 | mandatory_roundabout                  |
|       35 | mandatory_straigh_left                |
|       36 | mandatory_straight                    |
|       37 | mandatory_straight_right              |
|       38 | priority_give_way                     |
|       39 | priority_road                         |
|       40 | priority_stop                         |
|       41 | warning_children                      |
|       42 | warning_construction                  |
|       43 | warning_crosswalk                     |
|       44 | warning_cyclists                      |
|       45 | warning_domestic_animals              |
|       46 | warning_other_dangers                 |
|       47 | warning_poor_road_surface             |
|       48 | warning_roundabout                    |
|       49 | warning_slippery_road                 |
|       50 | warning_speed_bumper                  |
|       51 | warning_traffic_light                 |
|       52 | warning_tram                          |
|       53 | warning_two_way_traffic               |
|       54 | warning_wild_animals                  |
|       55 | other_restriction_ends_80             |
|       56 | prohibitory_speed_limit_120           |
|       57 | warning_priority_at_next_intersection |
|       58 | prohibitory_no_vehicles               |
|       59 | warning_bend                          |
|       60 | warning_road_narrows                  |
|       61 | warning_traffic_jam                   |
|       62 | warning_icy_road                      |
|       63 | other_restriction_ends                |
|       64 | other_restriction_ends_overtaking     |
|       65 | priority_road_ends                    |

