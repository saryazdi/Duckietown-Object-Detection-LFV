<h1>Duckietown LFV using Pure Pursuit and Object Detection</h1>
<h2>Controller: Pure Pursuit (modified)</h2>
We use a modified version of pure pursuit controller for lane following which can be found <a href="https://github.com/saryazdi/pp-navigation">here</a>. The pure pursuit algorithm works by taking the point on the path that is some predetermined lookahead distance ahead of the robot's current position and heading towards that target point by sending the appropriate wheel commands. We use the following modifications on pure pursuit:
<h3>Finding the Target Point</h3>
- One of the biggest challenges here is getting the path from our input image. We avoided finding the path by directly estimating our target point:
<ul>
  <li>We take the average of the points on the yellow lane, and with some offset to the right, we will have an estimate of our target point.</li>
  <li>If we are not seeing the yellow lane, we will take the average of the points on our white lane, and offset that point to the left to get an estimate of our target point.</li>
  <li>Additionally, the average direction of the points is also taken into consideration for computing the offset: E.g., if yellow line segments are perpendicular to us, then the target point would not just be to the right of the average of the yellow points, but also downwards (towards the robot).</li>
</ul>

<h3>Varying Speed and Omega Gain</h3>
<ul>
  <li>Our robot detects whether it is close to a left turn, a right turn or on a straight path. Turns are detected using statistics of detected lines.</li>
  <li> The duckiebot gradually speeds up on straight paths, while reducing the omega gain (so that the robot corrects less when moving fast to avoid jerky movement).</li>
  <li> The duckiebot gradually slows down at turns, while increasing the omega gain (to make nice sharp turns).</li>
  <li> A second order degree polynomial is used for changing velocity/omega gain. So, after a turn the robot speeds up slowly, giving it enough time to correct its position before going fast. At turns, the robot will slow down faster to ensure safe navigation of the turn.</li>
</ul>
