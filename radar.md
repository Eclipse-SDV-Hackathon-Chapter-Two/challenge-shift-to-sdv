# Radar data

You have access to the data of the front left and front right radar of the vehicle.

The data looks like the following:

eCAL Topics (fl = front left, fr = front right):
* `radar_far_fl`
* `radar_far_fr`
* `radar_near_fl`
* `radar_near_fr`

Note: For near type scans there is only the `scantype` set to `SRR_RDI_NEAR_SCAN`, but the explanation of the fields remain the same to the far scan shown below.

```json
{
    "aRadardetectionheader": {
        "uNofdetections": 24, // number of detections for one measurement cycle
        "fVambig": 19.147312, // ambigous free doppler range [m/s]
        // ...
        "signalheader": {
            // ...
        }
    },
    "scantype": "SRR_RDI_FAR_SCAN", // far scan
    "aRadardetectionlist": [ // detection data of the radar
        {
            "fRange": 3.8074365, // radial range in [m]
            "fAzang": -0.012371942, // azimuth angle in [rad]
            "fVrelrad": 0.1098722, // ambigous doppler measurement in [m/s]
            "fRcs": 3.5483885, // measured radar cross section
            "uPdh0": [ // false alarm probability
                0, //u_Pdh0[0] false alarm probability Near Range False Detection
                0, //f_Pdh0[1] false alarm probability Ramp Artifact
                0, //u_Pdh0[2] false alarm probability Interference False Detection
                0, //u_Pdh0[3] false alarm probability Sidelobe Detection
                0 //u_Pdh0[5] false alarm probability Range Spectrum
            ]
        },
        {
            "fRange": 4.0829744,
            "fAzang": 0.40815526,
            "fVrelrad": 8.924424,
            "fRcs": -17.741934,
            "uPdh0": [
                0,
                0,
                0,
                0,
                0
            ]
        },
        // .. more detections, it's a list...
    ]
}
```
