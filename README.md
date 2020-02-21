
## 6Dof Vehicule Localization using Hybrid Octrees Paper (Submitted to XX )
[![](https://img.youtube.com/vi/BLnmOXnFlSA/0.jpg)](https://www.youtube.com/watch?v=BLnmOXnFlSA)

 Yohan Dupuis¹, Vincent VAUCHEY¹, Xavier SAVATIER¹.  
¹[ESIGELEC](http://www.esigelec.fr/) , IRSEEM, Rouen, France, Normandie Univ, UNIROUEN,   
vauchey@esigelec.fr
dupuis@esigelec.fr
fourre@esigelec.fr
savatier@esigelec.fr

# Datasets
Dataset Lidar/IMU/RGBD Camera done by [ESIGELEC](http://www.esigelec.fr/)

[![](https://img.youtube.com/vi/6mwToyNoxMQ/0.jpg)](https://www.youtube.com/watch?v=6mwToyNoxMQ)

The reference dataset for lidar localisation is [KITTY](http://www.cvlibs.net/datasets/kitti/) dataset and is used for a lot of publication and result comparaisons beetweens localization/SLAM algorithms. The main difficultiy to use [KITTY](http://www.cvlibs.net/datasets/kitti/) dataset is the ground true accuracy which is many times more than 20 cm (sometimes more than 50cm if under trees).

We try to provide to the community some datasets done with a reférence position with best positioning systems avaiblaibles in all conditions.
The datasets ground True is done with a Landyns ([IXblue](https://www.ixblue.com/)) IMU based on fiber-optic-gyroscope (FOG), which is a technology wich ensure very low shift and noise between two gps position or when the gps accurancy become low.
In addition of this very accurate IMU, we're also using a postprocessing application ([APPS](https://www.ixblue.com/products/apps)) coupled whith a GPS RTK [septentrio](https://www.septentrio.com/) . The goal of this application is to increase the accurancy of ground true position expecially when there is tree/tunnel by doing forwar/backward Kallman Filter.

| IMU  | LANDYN ([IXblue](https://www.ixblue.com/))        | ATLANS ([IXblue](https://www.ixblue.com/))  | RT 3000 ([Oxts](https://www.oxts.com/))
| :--------------- |:---------------:|:---------------:|:---------------:|
| Position when RTK lost (m)  | 0.20 (GNSS outage 60s) | 0.350 (GNSS outage 60s)  |  1.5 (SPS)
| Pitch/Roll (deg)  | 0.005 (RTK) / 0.005 (GNSS outage 60s) | 0.008 (RTK) / 0.01 (GNSS outage 60s) | 0.03
| Heading (deg)  | 0.01 | 0.020 | 0.1



### DATASET 2020/02/17 (NOT YET AVAILAIBLE) : 
Weather : Winter sun and some clouds
* Loop 1 [30km/h(Download)](http://www.esigelec.fr/) , [40km/h(Download)](http://www.esigelec.fr/),  [50km/h(Download)](http://www.esigelec.fr/)
* Loop 2 [30km/h(Download)](http://www.esigelec.fr/) , [40km/h(Download)](http://www.esigelec.fr/),  [50km/h(Download)](http://www.esigelec.fr/)
* Loop 3 [30km/h(Download)](http://www.esigelec.fr/) , [40km/h(Download)](http://www.esigelec.fr/),  [50km/h(Download)](http://www.esigelec.fr/)
* [carpark(Download)](http://www.esigelec.fr/)

List of sensors and software used :
* vlp16 Lidar synchronised on GPS ([Velodyne](https://velodynelidar.com/))
* GPS AsterRx-U ([septentrio](https://www.septentrio.com/))
* LANDYN IMU + APPS ([IXblue](https://www.ixblue.com/))
* D435 trigged on IMU ([intelrealsense](https://www.intelrealsense.com/depth-camera-d435))
* RTMAPS ([Intempora](https://intempora.com/)) Realtime acquisition software (can also be used to replay datasets)

![](images/espace1.jpg )


### Context :
The dataset localization are datasets on same road than the French Project "Rouen Normandy Autonomous Lab" with Renault and Transdev partners
[![](https://img.youtube.com/vi/eCkQ1vqz_8s/0.jpg)](https://www.youtube.com/watch?v=eCkQ1vqz_8s)





