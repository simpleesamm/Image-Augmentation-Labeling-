# Image-Augmentation-Labeling
Preparing your images in the right format - Image labels can take many formats depending on the model that you are training in. This repo is basically a collection of some codes I use to aid in my augmentation and image cleaning. 

**Files: **
1) AugmentFullPipeline.py 
Credits: https://github.com/mdbloice/Augmentor
This file is basically the main file to augment your images. The library provides a wide range of augmentations ranging from rotations, blurring, zoom and more. 

2) splitTestTrain.py
File to split your augmented files. You can specify the percentage split. Creates a new folder for train & test.

3) rename.py
Basic renaming of your image files to a more standardized format if needed. 

4) imageLabel.py this labeling is fairly naive. There are plenty other methods to label like Roboflow. This method just takes the dimensions of the image and converts it to a csv label. 

5) convertCSVtoDarknet.py once you have the CSV labels you can convert it to Darknet Labels if needed. 

6) change_xml_labels.ipynb in the case that you want to mass change your xml labels to another name. This code does it nicely. 

