<h1>The Duckietown Object Detection Dataset</h1>
This dataset can be found <a href="https://drive.google.com/drive/folders/1cTBoKrXJb0kajBGxhuBxJpbKaotHPX7O">here</a>. We provide annotations and a sample script to load the annotations.


| Number of images  | 1956  |
| Number of object categories  | 3  |
| Number of objects annotated  | 5068  |


Total number of images: 1956
Number of object categories: 3
Number of objects annotated: 5068

Category details: 
Duckies:
Category name: duckie
Number of instances: 2570
Category id: 2


Cones: 
Category name: cone
Number of instances: 372
Category id: 1


Duckiebots:
Category name: duckiebot
Number of instances: 2126
Category id: 3
Number of older Duckiebot instances: 1419
Number of newer Duckiebot instances: 707

In this work, we first identify most prominent objects. In the duckietown, we see duckies, duckiebots and cones on the road. To achieve this, we find useful logs containing all these obstacles. We preprocess these logs to get diverse set of frames with multiple obstacles. 

