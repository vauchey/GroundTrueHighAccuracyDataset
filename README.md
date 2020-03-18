
# 6Dof Vehicule Localization using Hybrid Octrees Paper (Submitted to [ITSC2020](https://www.ieee-itsc2020.org/)  ) by [ESIGELEC](https://www.esigelec.fr/)

## News :
* 2020/03/17 : A second dataset is availaible  [here](#MARCH) on same road than previous.

* 2020/02/18 : A first dataset is availaible [here](#FEBRUARY) (datasets used for ITSC2020).

## Abstract :
This paper presents a 6DoF real-time vehicle localization
based on hybrid octrees and LiDAR data. Our approach is
based on a new representation never applied to vehicle
localization. It allows to reduce the memory footprint of
the map and significantly lower the computation load for
the online localization. Our approach has shown to perform
well on both CPUs and GPUs. The algorithm design allows to
run the localization simultaneously on both architectures.
The paper gives insight covering the calibration of the
mobile mapping setup to the 6 DoF localization process. Our
experiments shows that our method is both accurate and
reliable on several datasets and platforms. The positioning
performance is significant with 5cm and 0.08° angular RMSE. 





[![](https://img.youtube.com/vi/BLnmOXnFlSA/0.jpg)](https://www.youtube.com/watch?v=BLnmOXnFlSA)

Vincent VAUCHEY¹, Yohan DUPUIS¹, Pierre MERRIAUX², Jérémy FOURRE¹, Xavier SAVATIER¹.  
¹[ESIGELEC](http://www.esigelec.fr/) , IRSEEM, Rouen, France, Normandie Univ, UNIROUEN,   
²[Leddartech](http://www.leddartech.com.),   Quebec   City,   Canada

vauchey@esigelec.fr
dupuis@esigelec.fr
fourre@esigelec.fr
savatier@esigelec.fr
pierre.merriaux@leddartech.com


Special Thanks to the members of the [SIRD](http://www.esigelec.fr/en/node/113) team : Marc DEHAIS, Anthony DESHAIS, Christophe ALEGRE
# Datasets
Dataset Lidar/IMU/RGBD Camera done by [ESIGELEC](http://www.esigelec.fr/).

<span style="color:red">Some new dataset on same roads will be availaible each mounth.</span>

[![](https://img.youtube.com/vi/6mwToyNoxMQ/0.jpg)](https://www.youtube.com/watch?v=6mwToyNoxMQ)

The main reference dataset for lidar localisation is [KITTY](http://www.cvlibs.net/datasets/kitti/) dataset and is used for a lot of paper and result comparaisons beetweens localization/SLAM algorithms. The main difficultiy to use [KITTY](http://www.cvlibs.net/datasets/kitti/) dataset is the ground true accuracy which is many times more than 20 cm.

We try to provide to the community some datasets done with a reference position with best positioning systems avaiblaibles in all conditions.
The datasets ground True is done with a Landyns ([IXblue](https://www.ixblue.com/)) IMU based on fiber-optic-gyroscope (FOG), which is a technology wich ensure very low shift and noise between two gps position or when the gps accurancy become low.
In addition of this very high accurate IMU, we're also using a postprocessing application ([APPS](https://www.ixblue.com/products/apps)) coupled whith a GPS RTK [septentrio](https://www.septentrio.com/) . The goal of this application is to increase the accurancy of ground true position expecially when there is tree/tunnel by doing forwar/backward Kallman Filter. Landyn IMU is an "old" IMU without new firmware release but with better FOG than IMU currently saled for civil application by [IXblue](https://www.ixblue.com/). The fact to use APPS software give the possibility to use processing algorithms numpy reinterpret castzof last IMU saled by Ixblue on our Landyn.

## IMU COMPARAISON :
| IMU  | LANDYN ([IXblue](https://www.ixblue.com/))        | ATLANS ([IXblue](https://www.ixblue.com/))  | RT 3000 ([Oxts](https://www.oxts.com/))
| :--------------- |:---------------:|:---------------:|:---------------:|
| Position when RTK lost (m)  | 0.20 (GNSS outage 60s) | 0.350 (GNSS outage 60s)  |  1.5 (SPS)
| Pitch/Roll (deg)  | 0.005 (RTK) / 0.005 (GNSS outage 60s) | 0.008 (RTK) / 0.01 (GNSS outage 60s) | 0.03
| Heading (deg)  | 0.01 | 0.020 | 0.1

<a id="FEBRUARY"></a>
#### DATASET 2020/02/18 : 
* Loop1 : Winter sun and some clouds (~1.5km)
    * [30 km/h dataset A (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/Es6-VHjNiZBOubLo9q2Q1yMBoJ9y7BUGPe2NENOk30hMSA?e=WaCXvv)
    * [30 km/h dataset B (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/Ep6Z90zOKYVCipE6pUHEONwB_tNcZjKDh-ARI84gIa1-2w?e=pM3R5e)
    * [40 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EiKIg8MUu8dOqryis5O0QFYBwbs4CK7igzz_9DlccL1JoA?e=U2rvdL)
    * [50 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EqH7B0M1s0RMvxOBO7FcqfIB1vUxszmcxPL5-d4YIP9YLg?e=0Y0XhP)
    * [Directory Tree and calibrations](#TREE)

    [![](images/LOOP1.gif)](https://www.google.com/maps/d/embed?mid=1cAdJnWjBnK7ZZkCva8ftSXN_qYLh2o9t   )

    [maps preview](https://www.google.com/maps/d/embed?mid=1cAdJnWjBnK7ZZkCva8ftSXN_qYLh2o9t)
    
    


        

* Loop2 : Winter sun and some clouds with one short tunnel (~2.6 km)

    * [30 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EpMb2wsK-NpGrhTXduyHqCsBPwkXS0PnqqerVkWSDt3SBw?e=m6i0lU)
    * [40 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EorAB27JGmBCinzCaIx3-BABeothYaj082p_ULneF3W90A?e=rCeS9S)
    * [50 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EuxwP_jf_ftEgLOtLrW8rEcBcGaAB138aQH0VoWES5mRTQ?e=ZVXkvt)
    * [Directory Tree and calibrations](#TREE)

    [![](images/LOOP2.gif)](https://www.google.com/maps/d/embed?mid=1aRvGyCyWWRs2k5G5HH2M6DCKO5p3p3LA)

    [maps preview](https://www.google.com/maps/d/embed?mid=1aRvGyCyWWRs2k5G5HH2M6DCKO5p3p3LA)



<a id="MARCH"></a>
#### DATASET 2020/03/17 :
Images will be availaible as soon as the containment due to the COVID19 will be finish.

* Loop1 : Winter sun (~1.5km)
    * [30 km/h dataset A (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/Epl3hNJUPLZCoy6IWMNTANUBVNQIBkzYMGPoVdiwesmI8A?e=XlI1bo)
    * [30 km/h dataset B (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EuCzgB2bsMNPvvh2F2uJyXsBR6S94p-nG2j4gCIl95Q2Fg?e=mbxzMa)
    * [40 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EpUYJXIIOBBCmVeVNDTEzY0BeX3aoa13xvPoDsl7oqROzA?e=aLZPNy)
    * [50 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/ErHtWZHchZBNsbFTgj7a4N0BifbNDwc2UOtceli3BklsnQ?e=NnnGL3)
    * [Directory Tree and calibrations](#TREE)

    [![](images/LOOP1_March.gif)](https://www.google.com/maps/d/embed?mid=1cAdJnWjBnK7ZZkCva8ftSXN_qYLh2o9t   )

* Loop2 : Winter sun  (~2.6 km) {: #funky }

    * [30 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/Ejo-BdHUM3RLllubCrM5CR4BcTmivJZkLjhOAkxU6bZ1Lw?e=zA4vqO)
    * [40 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/Empp_AwT1I5Ejkt7ORN6Hb0B3cqe_DiQUn9OsdJWGAfpMw?e=k9qW9w)
    * [50 km/h dataset (Download)](https://esigelec-my.sharepoint.com/:f:/g/personal/vauchey_esigelec_fr/EnGsngNsyfJNmc6OXIcSKVkBsYvJUXxJp0fqcYi46UyvvQ?e=iZAZHV)
    * [Directory Tree and calibrations](#TREE)

    [![](images/LOOP2_March.gif)](https://www.google.com/maps/d/embed?mid=1aRvGyCyWWRs2k5G5HH2M6DCKO5p3p3LA)



List of sensors and software used :
* vlp16 Lidar synchronised on GPS ([Velodyne](https://velodynelidar.com/))
* GPS AsterRx-U ([septentrio](https://www.septentrio.com/))
* LANDYN IMU + post processing software APPS ([IXblue](https://www.ixblue.com/))
* D435 trigged on IMU ([intelrealsense](https://www.intelrealsense.com/depth-camera-d435))
* Peiseler odometer mounted on the right rear wheel.
* RTMAPS ([Intempora](https://intempora.com/)) Realtime acquisition software (can also be used to replay datasets)
* Rtk correction network ([teria](https://www.reseau-teria.com/reseau/)) 
* PCAN-USB ([peak-system](https://www.peak-system.com)) 
![](images/espace1.jpg )

<a id="TREE"></a>

Directory Tree :
* imagesSynchronisedImuPostPro.zip : images + imu + postpro synchronised
* lidarCorrectedSynchronisedImuPostPro.zip : lidar corrected  + imu + postpro synchronised
* lidarUnCompensatedImuPostProUnsynchronised : lidar uncorrected + imu + postpro unsynchronised (Download)

Calibrations (X forward, Y left, Z Up) :
* Transformation IMU to Lidar (Tx,Ty,Tz,Rx,Ry,Rz) : [0.989,-0.024, 2.388,0.0,0.0,-0.385]
* Car odometry and IMU have the same measurement points (rear axle)
* Transformation lidar to rgbd Camera (Tx,Ty,Tz,Rx,Ry,Rz) : [0.74,-0.43, 0.0,0.0,0.0,0.0], python code to read XYZ png file is availaible [here](code/convertionImageXYZto3D.py)

### Context :
The dataset localization are datasets on same road than the French Project "Rouen Normandy Autonomous Lab" with Renault and Transdev partners:

[![](https://img.youtube.com/vi/eCkQ1vqz_8s/0.jpg)](https://www.youtube.com/watch?v=eCkQ1vqz_8s)





