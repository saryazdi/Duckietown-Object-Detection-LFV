<h1>Duckietown LFV using Pure Pursuit and Object Detection</h1>

<h2>Table of Contents</h2>
<p align="right">
  <a href="https://www.duckietown.org/"><img align="right" src="https://www.duckietown.org/wp-content/uploads/2018/05/duckie2-300x270.png" alt="Duckietown Logo" style="width:100%"></a>
</p>
<ul>
  <li><a href="#quickstart">Quick Start</a></li>
  <ul>
    <li><a href="#preliminaries">Preliminaries</a></li>
    <li><a href="#simulation">Run in Simulation</a></li>
    <li><a href="#hardware">Run on Hardware</a></li>
    <li><a href="#paramtuning">Tuning the Parameters</a></li>
  </ul>
  <li><a href="#videos">Videos of expected results</a></li>
  <ul>
  <li><a href="#steady">Steady Lane Following</a></li>
  <li><a href="#fast">Fast Lane Following</a></li>
  <li><a href="#lfv1">Lane Following with Vehicle Avoidance 1</a></li>
  <li><a href="#lfv2">Lane Following with Vehicle Avoidance 2</a></li>
  <li><a href="#trainedmodel">Faster RCNN Object Detection</a></li>
  </ul>
  <li><a href="#lanefollowing">Lane Following</a></li>
  <ul>
    <li><a href="#targetpoint">Finding the Target Point</a></li>
    <li><a href="#varyingspeed">Varying Speed and Omega Gain</a></li>
    <li><a href="#lanefilter">Modified Lane Filter</a></li>
  </ul>
  <li><a href="#lanefollowingvehicles">Lane Following with Vehicles</a></li>
  <ul>
    <li><a href="#objectdetection">Object Detection</a></li>
    <ol>
      <li><a href="#deeplearning">Deep Learning</a></li>
      <ul>
        <li><a href="#dataset">The Dataset</a></li>
        <li><a href="#model">The Model</a></li>
      </ul>
      <li><a href="#imageprocessing">Image Processing</a></li>
     </ol>
    <li><a href="#groundprojections">Modified Ground Projections</a></li>
    <li><a href="#vehicleavoidance">Vehicle Avoidance</a></li>
  </ul>
</ul>

<a name="quickstart"/>
<h2>Quick Start</h2>
<ul>
  <a name="preliminaries"/>
  <li><h3>Preliminaries</h3></li>
  The quick start assumes that you have followed all of the steps in the <a href="https://docs.duckietown.org/daffy/opmanual_duckiebot/out/index.html">Duckiebook operational manual</a> up to "<a href="https://docs.duckietown.org/daffy/opmanual_duckiebot/out/demo_lane_following.html">Unit E-12: Lane following</a>".
  
  <a name="simulation"/>
  <li><h3>Run in Simulation</h3></li>
  Clone the repository:
  
      $ cd <LOCAL-DUCKIETOWN-DIRECTORY>/catkin_ws/src
      $ git clone https://github.com/saryazdi/pp-navigation.git
        
  Start docker container:
  
      $ cd <LOCAL-DUCKIETOWN-DIRECTORY>
      $ docker-compose up
        
   Build the package within the container and source the workspace:
   
      [CONTAINER]$ catkin build --workspace catkin_ws
      [CONTAINER]$ source catkin_ws/devel/setup.bash
   
   Run the code within the container:
   
      [CONTAINER]$ roslaunch catkin_ws/src/pp-navigation/packages/pure_pursuit_lfv/launch/lfv_start.launch
  
  
  <a name="hardware"/>
  <li><h3>Run on Hardware</h3></li>
  
  With your computer and the duckiebot connected to the same network, run the following command on your computer to pull the image onto the duckiebot:
  
      $ docker -H <DUCKIEBOT_NAME>.local pull saryazdi/pp-navigation:v1-arm32v7
  
  Run the following command on your computer to start running the lane following with vehicles code on your robot:
  
      $ dts duckiebot demo --demo_name HW_lfv_start --package_name pure_pursuit_lfv --duckiebot_name <DUCKIEBOT_NAME> --image saryazdi/pp-navigation:v1-arm32v7
      
  That's it! Your duckiebot should start moving within a minute or two.
  <a name="paramtuning"/>
  <li><h3>Tuning the Parameters</h3></li>
      The parameters might need to be re-tuned on different versions of the simulator (e.g. if the camera calibration or the camera blur or FPS changes) and on different duckiebots as well (due to different wheel/camera calibrations). In our experience, this becomes more important if you want to use high speeds. Luckily, there is a pipeline in place for changing the parameters as the code is running and see the effects right away.
   <br/><br/>
   
   If running in simulation, first run the below command to get a bash in the container running your code (hint: if you do not know the container name, run ```docker ps``` to see a name list of all of the currently running containers):
      
      $ docker exec -it <CONTAINER_NAME> /bin/bash
   If running on hardware, first run the below command to get a bash in the container running your code and source the workspace:
   
      $ docker -H <DUCKIEBOT_NAME>.local exec -it demo_HW_lfv_start /bin/bash
      
      [CONTAINER]$ source /code/catkin_ws/devel/setup.bash
   
   From here, you can view the names of all of the parameters related to pure pursuit and duckiebot detection by running:
      
      [CONTAINER]$ rosparam list | grep -E 'pure_pursuit|duckiebot_detection'
   
   And from that list, you can change the value of any parameter by running:
   
      [CONTAINER]$ rosparam set <PARAMETER_NAME> <PARAMETER_VALUE>
</ul>

<a name="videos"/>
<h2>Videos of expected results</h2>
<ul>
  
  <a name="steady"/>
  <li><a href="https://youtu.be/mL84DI1Ytk0">Steady Lane Following</a></li>
  <b>14 tiles</b> in <b>30 seconds</b>: 3 left turn tiles, 1 right turn tile, 10 straight path tiles, 0 lane violations
  <a href="https://youtu.be/mL84DI1Ytk0" target="_blank">
    <p align="center">
      <img align="center" height="300" src="https://img.youtube.com/vi/mL84DI1Ytk0/0.jpg"/>
    </p>
    </a>
    <br clear="all" />
    
  <a name="fast"/>
  <li><a href="https://youtu.be/Kl7DO9rEVqQ">Fast Lane Following</a></li>
  <b>33 tiles</b> in <b>60 seconds</b>: 9 left turn tiles, 3 right turn tiles, 21 straight path tiles, 0 lane violations
  <a href="https://youtu.be/Kl7DO9rEVqQ" target="_blank">
    <p align="center">
      <img align="center" height="300" src="https://img.youtube.com/vi/Kl7DO9rEVqQ/0.jpg"/>
    </p>
    </a>
    <br clear="all" />
    
  <a name="lfv1"/>
  <li><a href="https://youtu.be/d7fnCfaGW_U">Lane Following with Vehicle Avoidance 1</a></li>
  <a href="https://youtu.be/d7fnCfaGW_U" target="_blank">
    <p align="center">
      <img align="center" height="300" src="https://img.youtube.com/vi/d7fnCfaGW_U/0.jpg"/>
    </p>
    </a>
   <br clear="all" />
   
   <a name="lfv2"/>
  <li><a href="https://youtu.be/XYgBKyo5pQY">Lane Following with Vehicle Avoidance 2</a></li>
  <a href="https://youtu.be/XYgBKyo5pQY" target="_blank">
    <p align="center">
      <img align="center" height="300" src="https://img.youtube.com/vi/XYgBKyo5pQY/0.jpg"/>
    </p>
    </a>
   <br clear="all" />
   
   <a name="trainedmodel"/>
  <li><a href="https://www.youtube.com/watch?v=3jD02dxL6gg">Faster RCNN Object Detection</a></li>
  <a href="https://youtu.be/3jD02dxL6gg" target="_blank">
    <p align="center">
      <img align="center" height="300" src="https://img.youtube.com/vi/3jD02dxL6gg/0.jpg"/>
    </p>
    </a>
</ul>
<br clear="all" />


<a name="lanefollowing"/>
<h2>Lane Following</h2>
We use a modified version of the pure pursuit controller for lane following which can be found <a href="https://github.com/saryazdi/pp-navigation">here</a>. To learn more about the pure pursuit controller, check out "<a href="https://www.ri.cmu.edu/pub_files/pub3/coulter_r_craig_1992_1/coulter_r_craig_1992_1.pdf">Implementation of the Pure Pursuit Path Tracking Algorithm</a>" by R. Craig Conlter. We use the following modifications on pure pursuit:
<a name="targetpoint"/>
<h3>Finding the Target Point</h3>
We avoided computing the path by directly estimating our target point.
<ul>
  <li>We offset the points on the ground-projected yellow lane to the right, and then take the average of them to have an estimate of our target point.</li>
  <li>If we are not seeing the yellow lane, we offset the points on the ground-projected white lane to the left and then take the average of them to get an estimate of our target point.</li>
  <li>Additionally, the average direction of the line segments is also taken into consideration for computing the offset: E.g., if the ground-projected yellow line segments are perpendicular to us (like when facing a turn), then the target point would not just be to the right of the average of the yellow points, but also downwards (towards the robot).</li>
  <li>In the visualization below, we can see the ground projected and shifted line segments. The cyan point is our robot's position, and the green point is the pure pursuit target (follow) point.</li>
  <br clear="all" />
  <p align="center">
    <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/lf_sim.gif"/>
  </p>
</ul>

<a name="varyingspeed"/>
<h3>Varying Speed and Omega Gain</h3>
<ul>
  <li>Our robot detects whether it is close to a left turn, a right turn or on a straight path. Turns are detected using statistics of detected lines.</li>
  <li> The duckiebot gradually speeds up on straight paths, while reducing the omega gain so that the robot corrects less when moving fast (to avoid jerky movement).</li>
  <li> The duckiebot gradually slows down at turns, while increasing the omega gain (to make nice sharp turns).</li>
  <li> A second order degree polynomial is used for changing the velocity/omega gain. So, after a turn the robot speeds up slowly, giving it enough time to correct its position before going really fast. At turns, the robot will slow down faster to ensure safe navigation of the turn.</li>
</ul>
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/gearbox_demo_opt.gif"/>
</p>

<a name="lanefilter"/>
<h3>Modified Lane Filter</h3>
<ul>
  <li>We <a href="https://github.com/saryazdi/pp-navigation/blob/47a0f058d8cb0f3a88431c4cd5c32a946b86019b/packages/my_lane_filter/include/my_lane_filter/my_lane_filter.py#L163">modified</a> the "<a href="https://github.com/duckietown/dt-core/tree/daffy/packages/lane_filter">lane_filter</a>" package so that at each update step, it computes how much time has passed since the last update, and based on that we scale the variance of the gaussian that is used for smoothing the belief. This is especially useful if there is too much variance in the FPS: Not scaling the covariance when the FPS has a high variance would cause us to either smoothen the belief too much or too little.</li>
</ul>

<a name="lanefollowingvehicles">
<h2>Lane Following with Vehicles</h2>
We annotated our own real-world duckietown object detection dataset and trained a deep learning model on it. However, since we also needed an object detector in simulation, we made a second object detector using image processing operators. <br/>
  
<br clear="all" />

<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short1.gif" alt="Vehicle Avoidance Behind" style="width:100%">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short2.gif" alt="Vehicle Avoidance Head-on" style="width:100%">
</p>
<b>Disclaimer</b>: We have not been able to get the GPU to work with docker yet, thus we are currently using the vehicle detection with image processing code on hardware as well. This is temporary to show that the pipeline is working correctly and we can integrate our trained deep learning model on hardware once we figure out how to get the GPU working with docker.
<a name="object detection"/>
<h3>Object Detection</h3>

<a name="deeplearning"/>
<ol>
<li><h3>Deep Learning</h3>
<ul>
<a name="dataset"/>
<li><h4>The Dataset</h4></li>
  We annotated our own real-world dataset from Duckietown for detecting duckiebots, duckies and traffic cones. Information regarding our dataset can be found <a href="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/DuckietownObjectDetectionDataset.md">here</a>.

<a name="model"/>
<li><h4>The Model</h4></li>
For object detection with deep learning, we use Faster RCNN architecture with feature pyramid network. Faster RCNN is a popular 2 stage object detection pipeline where first stage is used to get the potential object regions in an image. First stage involves feature map extraction from a backbone network and the usage of region proposal network to find potential object regions. Once we find the object regions, we feed it through the second stage of the network. In the second stage, we do bounding box regression and object classification. In this architecture. We also use Feature Pyramid Network (FPN). FPN enables us to detect objects at various scales and sizes. We extract features at multiple different resolutions and fuse them to get a rich set of features before feeding it to the region proposal network to find final region proposals. FPNs are more effective at detecting small objects. We use the above object detection dataset to train the network. Below is the architecture of Faster RCNN.
<p align="center">
    <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/model_architecture.png" height="220"/>
</p>

In this work, we use <a href="https://github.com/facebookresearch/detectron2">detectron2</a>, a state of the art object detection framework from Facebook AI research. We train the model for 15000 iterations over the dataset with a learning rate of 0.015. We use Resnet 50 backbone for the model. Below are some qualitative results of the object detector, and you can find a video of our object detector in action <a href="#trainedmodel">here in the demos section</a>.
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/predictions/00025.png" width="370"/>
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/fasterRCNN.gif" width="370"/>
</p>
</ul>
</li>

<a name="imageprocessing"/>
<li><h3>Image Processing</h3>
<ul><li>For object detection using image processing, we use HSV filtering followed by erosion and dilation, we then find the bounding boxes around the contours. Bounding boxes with a small area are filtered out.</li></ul></li>
  <p align="center">
    <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/sim_detection_duckiebot.gif"/>
  </p>
</ol>

<a name="groundprojections"/>
<h3>Ground Projections</h3>
<ul><li>We <a href="https://github.com/saryazdi/pp-navigation/blob/47a0f058d8cb0f3a88431c4cd5c32a946b86019b/packages/my_ground_projection/src/ground_projection_node.py#L72">modified</a> the "<a href="https://github.com/duckietown/dt-core/tree/daffy/packages/ground_projection">ground_projection</a>" package to subscribe to the topic with the obstacle bounding box coordinates, and then we ground project those coordinates and re-publish them.</li></ul>

  
<a name="vehicleavoidance"/>
<h3>Vehicle Avoidance</h3>
<ul><li>If we get closer to a vehicle (which is directly in front of us) than some distance threshold, we stop. We stay still until the obstalce is no longer in front of us within that distance threshold. In the visualization below, the gray box is the "safety zone" where we stop if an obstacle is within that box.</li></ul>
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/lfv_sim.gif"/>
</p>
