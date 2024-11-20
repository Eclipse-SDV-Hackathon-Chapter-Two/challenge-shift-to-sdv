# Vehicle Dynamics

Retrieve in-vehicle sensor data by subscribing to the eCAL `vehicle_dynamics` topic.

The data received is in JSON format and looks like the following

```json
{
    "header": {
        "timestamp": "1730982505741887"
    },
    // potential sensor errors, can be ignored
    "errs": {
        // ...
    },
    // import in-vehicle signals like speed, acceleration and steering wheel angle, ...
    "signals": {
        "speed": 4.500004, // [m/s] Absolute ego vehicle velocity in earth coordinate system; negative value is backwards.
        "speedDisplayed": 4.722226, // [m/s] Absolute ego vehicle velocity in earth coordinate system shown in Kombi/Tacho
        "speedPerWheel": [ // for each wheel m/s, negative is backwards, [0]:FL, [1]:FR, [2]:RL, [3]:RR
            4.5041704,
            4.49167,
            4.508337,
            4.48542
        ],
        "longAcc": 0.0, // [m/s**2] Longitudinal ego vehicle acceleration
        "latAcc": -0.02, // [m/s**2] Lateral ego vehicle acceleration
        "yawrate": 0.00034906, // [rad/s] Ego vehicle yaw rate measured in center of gravity coordinate system. Driving through a left turn leads to positive values.
        "steeringWheelAngle": -0.064576104, // rad
        "steeringWheelAngleSpeed": 0.0, // rad/s
        "drvSteerTorque": 0.0, // Nm
        "timeSinceLastClick": 0.0, // [s] time since last wheel-tick at one of the 4 wheel (1 tick = 2cm)
        "wheelSteeringAngleFront": 0.0, // [rad] Angle of the front wheels; 0xFFFF = error ;It's a 16bit signal because for the  Cube, the origin signal has 16bit as well.
        "wheelSteeringAngleRear": 0.0 // [rad] Angle of the rear wheels; 0xFFFF = error ;It's a 16bit signal because for the  Cube, the origin signal has 16bit as well.
    },
    // variances, can be ignored
    "variances": {
        // ...
    },
    // timestamps, can be ignored
    "timestamps": {
        // ...
    }
}
```