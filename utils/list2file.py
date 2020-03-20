# USAGE
# python train.py --dataset Sports-Type-Classifier/data --model model/ activity.model --label_bin model/lb.pickle --epochs 50
# set the matplotlib backend so figures can be saved in the background

# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import cv2
import os

# construct the argument parser and parse the arguments
parse = argparse.ArgumentParser()
parse.add_argument("-d", "--data", required=True,
	help="path to input dataset")
args = parse.parse_args()

# initialize the set of labels from the spots activity dataset we are
# going to train our network on
LABELS = {"cooking", "drinking"}

# grab the list of images in our dataset directory, then initialize
# the list of data (i.e., images) and class images
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args.data))

data = []
labels = []
# loop over the image paths
for imagePath in imagePaths:
	# extract the class label from the filename
	label = imagePath.split(os.path.sep)[-2]

	# if the label of the current image is not part of of the labels
	# are interested in, then ignore the image
	if label not in LABELS:
		continue
    
	# load the image, convert it to RGB channel ordering, and resize
	# it to be a fixed 224x224 pixels, ignoring aspect ratio
	image = cv2.imread(imagePath)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, (224, 224))
	# update the data and labels lists, respectively
	data.append(image)
	labels.append(label)
# convert the data and labels to NumPy arrays
data = np.array(data)
labels = np.array(labels)



print('writing to the data file...')
with open('data.txt', 'w') as f:
    for item in data:
        f.write('%s\n' % item)
print('writing to the labels file...')
with open('labels.txt', 'w') as l:
    for label in labels:
        l.write('%s\n' % label)
