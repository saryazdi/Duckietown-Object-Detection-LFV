<h1>Duckietown-Object-Detection-LFV</h1>

<h2>Controller: Pure Pursuit (modified)</h2>
We use a modified version of pure pursuit controller for lane following. The pure pursuit algorithm works by taking the point on the path that is some predetermined lookahead distance ahead of the robot's current position and heading towards that target point by sending the appropriate wheel commands. We use the following modifications on pure pursuit:
<h3>Finding the Target Point</h3>
- One of the biggest challenges here is getting the path from our input image. We avoided finding the path by directly estimating our target point:
<ul>
  <li>We take the average of the points on the yellow lane, and with some offset to the right, we will have an estimate of our target point.</li>
  <li>If we are not seeing the yellow lane, we will take the average of the points on our white lane, and offset that point to the left to get an estimate of our target point.</li>
  <li>Additionally, the average direction of the points is also taken into consideration for computing the offset: E.g., if yellow line segments are perpendicular to us, then the target point would not just be to the right of the average of the yellow points, but also downwards (towards the robot).</li>
</ul>

<h3>Varying Speed and Omega Gain</h3>
Our robot detects turns and slows down at turns. Moreover, it detects straight paths and speeds up when on a straight path.
<ul>
  <li>Our robot can detect whether it is close to a left turn, a right turn or a straight path. Left and right turns are detected based on the mean of yellow/white points (e.g. at left turns the mean of the white points we see shifts to the left) and the standard deviation of the yellow/white points (e.g. at turns the ratio of the standard deviation of the points in the forward direction over the lateral direction would become smaller).</li>
  <li> The duckiebot speed increases gradually at straight paths, while the omega gain gets smaller so that the robot tries to correct less when moving straight with a high velocity.</li>
  <li> The duckiebot speed decreases gradually when at turns, while the omega gain gets larger so that the robot is able to make the sharp turn appropriately.</li>
  <li> While changing velocity/omega gain, we used a second order degree polynomial as opposed to a linear function, so that after a turn the robot speeds up more slowly, giving it enough time to correct its position before speeding up. Also, when close to a turn, the robot will slow down more quickly in order to ensure safe navigation of the turn.</li>
</ul>
