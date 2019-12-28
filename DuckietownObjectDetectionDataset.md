# The Duckietown Object Detection Dataset

## Table of Contents
<p align="right">
  <a href="https://www.duckietown.org/"><img align="right" src="https://www.duckietown.org/wp-content/uploads/2018/05/duckie2-300x270.png" alt="Duckietown Logo" width="150"></a>
</p>
<ul>
      <li><a href="#download">Download</a></li>
      <li><a href="#overview">Overview</a></li>
      <li><a href="#categories">Category Details</a></li>
      <ol>
            <li><a href="#cones">Traffic Cones</a></li>
            <li><a href="#duckies">Duckies</a></li>
            <li><a href="#duckiebots">Duckiebots</a></li>
      </ol>
      <li><a href="#collection">Data Collection Procedure</a></li>
      <li><a href="#annotation">Data Annotation Procedure</a></li>
</ul>


<a name="download"/>

## Download
The dataset can be found <a href="https://drive.google.com/drive/folders/1cTBoKrXJb0kajBGxhuBxJpbKaotHPX7O">here</a>. We provide annotations and a sample script to load the annotations.

<a name="overview"/>

## Overview
This dataset consists of 3 categories: traffic cones, duckies, and duckiebots. All of the dataset images were captured with duckiebot cameras. We use a combination of images from the <a href="http://logs.duckietown.org/">duckietown logs</a> and our own captured logs. Images were captured in different lighting conditions, with different versions of duckiebot models, and on different duckietown maps. Below are some statistics of our dataset:
<table>
      <tr><td>Number of images</td><td>1956</td></tr>
      <tr><td>Number of object categories</td><td>3</td></tr>
      <tr><td>Number of objects annotated</td><td>5068</td></tr>
</table>

<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/dataset/6.png" alt="Detection Dataset Sample" width="400">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/dataset/5.png" alt="Detection Dataset Sample" width="400">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/dataset/4.png" alt="Detection Dataset Sample" width="400">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/images/dataset/3.png" alt="Detection Dataset Sample" width="400">
</p>

<a name="categories"/>

## Category Details
<ol>
<a name="cones"/>
<li><h3>Traffic Cones</h3>
<table>
      <tr><td>Category name</td><td>cone</td></tr>
      <tr><td>Number of instances</td><td>372</td></tr>
      <tr><td>Category id</td><td>1</td></tr>
</table></li>

<a name="duckies"/>
<li><h3>Duckies</h3>
<table>
      <tr><td>Category name</td><td>duckie</td></tr>
      <tr><td>Number of instances</td><td>2570</td></tr>
      <tr><td>Category id</td><td>2</td></tr>
</table></li>

<a name="duckiebots"/>
<li><h3>Duckiebots</h3>
<table>
      <tr><td>Category name</td><td>duckiebot</td></tr>
      <tr><td>Number of instances</td><td>2126</td></tr>
      <tr><td>Category id</td><td>3</td></tr>
      <tr><td>Number of old Duckiebot instances</td><td>1419</td></tr>
      <tr><td>Number of new Duckiebot instances</td><td>707</td></tr>
</table></li>
</ol>
<a name="collection"/>

## Data Collection Procedure

In this work, we first identify the most prominent objects that we see on the roads of Duckietown: duckies, duckiebots and traffic cones. To begin our data collection procedure, we first identify all useful logs from <a href="http://logs.duckietown.org/">the Duckietown Logs Database</a> which contain the objects of interest. We then download and trim these logs so that the videos consist only of frames containing our objects of interest. Finally, we convert our videos to images (frames) while skipping some number of frames between each image to ensure that we get a diverse set of images. 

In these logs, there are videos of older versions of duckiebots with lots of wirings on them. However, new duckiebots are much cleaner with only the battery visible. To ensure robust detections, we needed to capture this intra-class variation. Thus we collected our own logs containing the new duckiebots. In the final dataset, we have merged old and new duckiebots to ensure that we can detect both variations. 

<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/datacollection.gif" alt="data collection">
</p>

<a name="annotation"/>

## Data Annotation Procedure
We used OpenCV's free <a href="https://github.com/opencv/cvat">CVAT</a> tool to annotate the dataset.
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/cvat_annotating.gif" alt="CVAT annotations">
</p>
