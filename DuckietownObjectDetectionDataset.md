# The Duckietown Object Detection Dataset
## Table of Contents
<p align="right">
  <a href="https://www.duckietown.org/"><img align="right" src="https://www.duckietown.org/wp-content/uploads/2018/05/duckie2-300x270.png" alt="Duckietown Logo" width="220"></a>
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
This dataset can be found <a href="https://drive.google.com/drive/folders/1cTBoKrXJb0kajBGxhuBxJpbKaotHPX7O">here</a>. We provide annotations and a sample script to load the annotations.

<a name="overview"/>

## Overview
This dataset consists of 3 categories: traffic cones, duckies, and duckiebots. All of the dataset images were captured with duckiebot cameras. Images were captured in different lighting conditions, with different versions of duckiebot models, and different locations. Below are some statistics of our dataset:
<table>
      <tr><td>Number of images</td><td>1956</td></tr>
      <tr><td>Number of object categories</td><td>3</td></tr>
      <tr><td>Number of objects annotated</td><td>5068</td></tr>
</table>

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
      <tr><td>Number of older Duckiebot instances</td><td>1419</td></tr>
      <tr><td>Number of newer Duckiebot instances</td><td>707</td></tr>
</table></li>
</ol>
<a name="collection"/>

## Data Collection Procedure

In duckietown, we see various different objects. In this work, we first identify most prominent objects. In the duckietown, we see duckies, duckiebots and cones on the road. To achieve this, we find useful logs containing all these obstacles. We preprocess these logs to get diverse set of frames with multiple obstacles. 

In these logs, there are older duckiebots with a lot of wiring around it. While new duckiebots are much cleaner with only battery visible. This made these both duckiebots visually very different from each other. Hence, to ensure robust detections, we additionally collect dataset for new duckiebots as well. In the final dataset, we have merged old and new duckiebots to ensure that we can detect both of them. 


<a name="annotation"/>

## Data Annotation Procedure
We used OpenCV's free <a href="https://github.com/opencv/cvat">CVAT</a> tool to annotate the dataset.
<p align="center">
  <img src="https://github.com/saryazdi/Duckietown-Object-Detection-LFV/blob/master/gifs/cvat_annotating.gif" alt="CVAT annotations">
</p>
