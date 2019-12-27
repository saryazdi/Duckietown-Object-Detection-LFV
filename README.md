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
