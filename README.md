<h1>Duckietown LFV using Pure Pursuit and Object Detection</h1>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#quickstart">Quick Start</a></li>
  <ul>
    <li><a href="#simulation">Run in Simulation</a></li>
    <li><a href="#hardware">Run on Hardware</a></li>
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
  <li><a href="#demo">Demo of Results</a></li>
</ul>

<a name="quickstart"/>
<h2>Quick Start</h2>
<ul>
  <a name="simulation"/>
  <li><h3>Run in Simulation</h3></li>
  
  <a name="hardware"/>
  <li><h3>Run on Hardware</h3></li>
</ul>

<a name="lanefollowing"/>
<h2>Lane Following</h2>
We use a modified version of the pure pursuit controller for lane following which can be found <a href="https://github.com/saryazdi/pp-navigation">here</a>. To learn more about the pure pursuit controller, check out <a href="https://www.ri.cmu.edu/pub_files/pub3/coulter_r_craig_1992_1/coulter_r_craig_1992_1.pdf">this paper</a>. We use the following modifications on pure pursuit:
<a name="targetpoint"/>
<h3>Finding the Target Point</h3>
We avoided computing the path by directly estimating our target point.
<ul>
  <li>We offset the points on the ground-projected yellow lane to the right, and then take the average of them to have an estimate of our target point.</li>
  <li>If we are not seeing the yellow lane, we offset the points on the ground-projected white lane to the left and then take the average of them to get an estimate of our target point.</li>
  <li>Additionally, the average direction of the line segments is also taken into consideration for computing the offset: E.g., if the ground-projected yellow line segments are perpendicular to us (like when facing a turn), then the target point would not just be to the right of the average of the yellow points, but also downwards (towards the robot).</li>
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
  <li> A second order degree polynomial is used for changing the velocity/omega gain. So, after a turn the robot speeds up slowly, giving it enough time to correct its position before going fast. At turns, the robot will slow down faster to ensure safe navigation of the turn.</li>
</ul>
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/gearbox_demo_opt.gif"/>
</p>

<a name="lanefilter"/>
<h3>Modified Lane Filter</h3>
<ul>
  <li>We <a href="https://github.com/saryazdi/pp-navigation/blob/47a0f058d8cb0f3a88431c4cd5c32a946b86019b/packages/my_lane_filter/include/my_lane_filter/my_lane_filter.py#L163">modified</a> the "<a href="https://github.com/duckietown/dt-core/tree/daffy/packages/lane_filter">lane_filter</a>" package so that at each update step, it computes how much time has passed since the last update, and based on that we scale the variance of the gaussian that is used for smoothing the belief. This is especially useful if there is too much variance in the FPS and in those cases it helped us get better filtered line segments at turns (when the state suddenly changes).</li>
</ul>

<a name="lanefollowingvehicles">
<h2>Lane Following with Vehicles</h2>
We annotated our own real-world duckietown object detection dataset and trained a deep learning model on it. However, since we also needed an object detector in simulation, we also made an object detector using image processing operators. We have yet to get the GPU to work with docker.
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short1.gif" alt="Vehicle Avoidance Behind" style="width:100%">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short2.gif" alt="Vehicle Avoidance Head-on" style="width:100%">
</p>

<a name="object detection"/>
<h3>Object Detection</h3>

<a name="deeplearning"/>
<ol>
<li><h3>Deep Learning</h3>
<ul>
<a name="dataset"/>
<li><h4>The Dataset</h4></li>
  We captured our own real-world dataset from Duckietown for detecting Duckiebots, duckies and traffic cones. Our dataset can be found <a href="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/ObjectDetectionDataset.md">here</a>.

<a name="model"/>
<li><h4>The Model</h4></li>
We used detectron2. TODO.
</ul>
</li>

<a name="imageprocessing"/>
<li><h3>Image Processing</h3>
<ul><li>We use HSV filtering followed by erosion and dilation, we then find the bounding boxes around the contours. Bounding boxes with a small area are filtered out.</li></ul></li>
  <p align="center">
    <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/sim_detection_duckiebot.gif"/>
  </p>
</ol>

<a name="groundprojections"/>
<h3>Ground Projections</h3>
<ul><li>We <a href="https://github.com/saryazdi/pp-navigation/blob/47a0f058d8cb0f3a88431c4cd5c32a946b86019b/packages/my_ground_projection/src/ground_projection_node.py#L72">modified</a> the "<a href="https://github.com/duckietown/dt-core/tree/daffy/packages/ground_projection">ground_projection</a>" package to subscribe to the topic with the obstacle bounding box coordinates, and then we ground project those coordinates and re-publish them.</li></ul>

  
<a name="vehicleavoidance"/>
<h3>Vehicle Avoidance</h3>
<ul><li>If we get closer to a vehicle (which is directly in front of us) than some threshold distance, we stop. We stay still until the obstalce is no longer in front of us within that threshold distance. </li></ul>
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/lfv_sim.gif"/>
</p>

<a name="demo"/>
<h3>Demo of Results</h3>
<ul>
  <li><a href="https://youtu.be/mL84DI1Ytk0">Steady lane following</a></li>
  [![Steady lane following](https://img.youtube.com/vi/mL84DI1Ytk0/0.jpg)](https://www.youtube.com/watch?v=mL84DI1Ytk0)
  <li><a href="">Fast lane following</a></li>
  <li><a href="">Lane following with vehicles</a></li>
</ul>
