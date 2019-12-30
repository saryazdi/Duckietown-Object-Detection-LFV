## How to run this?
## python load_annotations.py -im img_1569225768.833113908.png
## this will print annotation of a particular image and print it! 

import json
import argparse	

ap = argparse.ArgumentParser()
ap.add_argument("-im", "--imagename", required = True, help="give image name")
args = vars(ap.parse_args())
image_name = args["imagename"]

## loading all annotations
with open('final_anns.json') as f: 
	data = json.load(f)

## annotation of a particular image
image_anns = data[image_name]

## iterating through all the objects of a particular image
for annotation in image_anns:
	print("Category name is: ", annotation['cat_name'])
	print("Bounding box coordinates are: ", annotation['bbox'])

