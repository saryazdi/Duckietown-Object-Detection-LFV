import random
import os
import glob 
import cv2
import numpy as np
import json
from detectron2.structures import BoxMode
import itertools
import sys
# import some common detectron2 utilities
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import torch
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from contextlib import redirect_stdout
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-name", "--experiment_comment", required = True, help="Comments for the experiment")

args = vars(ap.parse_args())

dir_name = args['experiment_comment']

class_list = ['cone','duckie','duckiebot']

# write a function that loads the dataset into detectron2's standard format
def get_duckietown_dicts(root_dir):
    
    
    annotation_file = root_dir + 'annotation/final_anns.json'
    frame_path = root_dir + 'frames/'

    with open(annotation_file) as f: 
        data = json.load(f) 

    record = {}
    dataset_dicts = []

    
    class_label = {}
    ## giving labels to the classes
    for idx,class_val in enumerate(class_list):
        class_label[class_val] = idx 

    for name in data.keys():
        # print(name)
        image_name = frame_path + name
        record = {}
        # import pdb; pdb.set_trace()
        height, width = cv2.imread(image_name).shape[:2]

        record["file_name"] = image_name
        record["height"] = height
        record["width"] = width
        
        objs = []

        for annotation in data[name]:
            
            ob_list = []
            obj_ann = {
                            "bbox": [annotation['bbox'][0], annotation['bbox'][1], annotation['bbox'][0] + annotation['bbox'][2], annotation['bbox'][1] + annotation['bbox'][3]],
                            "bbox_mode": BoxMode.XYXY_ABS,                    
                            "category_id": annotation['cat_id'] - 1,
                            "iscrowd": 0
                        }
            objs.append(obj_ann)

        record["annotations"] = objs
        dataset_dicts.append(record)

    return dataset_dicts


from detectron2.data import DatasetCatalog, MetadataCatalog

## Directory containing dataset
root_dir = '/path/to/root/dir/'

for d in ["train", "test"]:
    DatasetCatalog.register("duckietown/" + d, lambda d=d: get_duckietown_dicts(root_dir))
    MetadataCatalog.get('duckietown/' + d).set(thing_classes=class_list)

duckietown_metadata = MetadataCatalog.get('duckietown/train')

# print("data loading")
# dataset_dicts = get_duckietown_dicts(root_dir)


from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg

cfg = get_cfg()
cfg.merge_from_file("/path/to/faster_rcnn_R_50_FPN_3x.yaml")
cfg.DATASETS.TRAIN = ("duckietown/train",)
cfg.DATASETS.TEST = ()   # no metrics implemented for this dataset
cfg.DATALOADER.NUM_WORKERS = 2
# cfg.MODEL.WEIGHTS = root_dir + 'model_final.pkl'  # initialize from model zoo
# cfg.MODEL.WEIGHTS = "/network/tmp1/bhattdha/detectron2_kitti/model_0014999.pth"  # initialize fron deterministic model
cfg.SOLVER.IMS_PER_BATCH = 12
cfg.SOLVER.BASE_LR = 0.015
# cfg.SOLVER.BASE_LR = 0.0003  
cfg.SOLVER.MAX_ITER =  15000  
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128   # faster, and good enough for this toy dataset
cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(class_list)  #  (kitti)
cfg.OUTPUT_DIR = root_dir + dir_name

# import ipdb; ipdb.set_trace()
os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
### At this point, we will save the config as it becomes vital for testing in future
torch.save({'cfg': cfg}, cfg.OUTPUT_DIR + '/' + dir_name + '_cfg.final')

trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=True)
print("start training")
trainer.train()


