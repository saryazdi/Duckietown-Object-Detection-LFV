<h1>Duckietown LFV using Pure Pursuit and Object Detection</h1>
<h2 align="center">Lane Following</h2>
We use a modified version of the pure pursuit controller for lane following which can be found <a href="https://github.com/saryazdi/pp-navigation">here</a>. To learn more about the pure pursuit controller, check out <a href="https://www.ri.cmu.edu/pub_files/pub3/coulter_r_craig_1992_1/coulter_r_craig_1992_1.pdf">this paper</a>. We use the following modifications on pure pursuit:
<h3>Finding the Target Point</h3>
We avoided computing the path by directly estimating our target point.
<ul>
  <li>We take the average of the points on the yellow lane, and with some offset to the right, we will have an estimate of our target point.</li>
  <li>If we are not seeing the yellow lane, we will take the average of the points on our white lane, and offset that point to the left to get an estimate of our target point.</li>
  <li>Additionally, the average direction of the points is also taken into consideration for computing the offset: E.g., if yellow line segments are perpendicular to us, then the target point would not just be to the right of the average of the yellow points, but also downwards (towards the robot).</li>
</ul>

<h3>Varying Speed and Omega Gain</h3>
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/gearbox_demo_opt.gif"/>
</p>
<ul>
  <li>Our robot detects whether it is close to a left turn, a right turn or on a straight path. Turns are detected using statistics of detected lines.</li>
  <li> The duckiebot gradually speeds up on straight paths, while reducing the omega gain (so that the robot corrects less when moving fast to avoid jerky movement).</li>
  <li> The duckiebot gradually slows down at turns, while increasing the omega gain (to make nice sharp turns).</li>
  <li> A second order degree polynomial is used for changing the velocity/omega gain. So, after a turn the robot speeds up slowly, giving it enough time to correct its position before going fast. At turns, the robot will slow down faster to ensure safe navigation of the turn.</li>
</ul>
<h3>Modified Lane Filter</h3>
<ul>
  <li>The lane filter was modified so that at each update step, it computes how much time has passed since the last update, and based on that scales the variance of the gaussian that we use for smoothing our belief. This is especially useful if there is too much variance in the FPS and in those cases it helped us get better filtered line segments at turns (when the state suddenly changes).</li>
</ul>
<h2 align="center">Lane Following with Vehicles</h2>
<h3>Object Detection</h3>
We trained a deep learning model for object detection trained on real logs, however since we also needed an object detector in simulation, we created another object detector using image processing operators.
<ol>
<li><h3>Object Detection using Deep Learning</h3>
TODO. Information about our captured dataset can be found <a href="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/ObjectDetectionDataset.md">here</a>.
</li>
<li><h3>Object Detection using Image Processing</h3>
  <p align="center">
    <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/sim_detection_duckiebot.gif"/>
  </p>
<ul><li>We use HSV filtering and then find the bounding boxes around the contours. We then filter out bounding boxes with a small area.</li></ul></li>
</ol>
<h3>Modified Ground Projections</h3>
<h3>Vehicle Avoidance</h3>
<!-- <p float="left"> -->
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short1.gif" alt="Vehicle Avoidance Behind" style="width:100%">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/vehicle_avoidance_short2.gif" alt="Vehicle Avoidance Head-on" style="width:100%">
</p>
