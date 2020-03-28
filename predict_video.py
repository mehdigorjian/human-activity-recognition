# USAGE
# python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/drink1.mp4 --output output/drink1_128avg.avi --action drinking --size 128

# import the necessary packages
from keras.models import load_model
from collections import deque
from utils.json_export import to_json_file
from utils.fig_export import fig_plot
import numpy as np
import argparse
import pickle
import json
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained serialized model")
ap.add_argument("-l", "--label-bin", required=True,
	help="path to  label binarizer")
ap.add_argument("-i", "--input", required=True,
	help="path to our input video")
ap.add_argument("-o", "--output", required=True,
	help="path to our output video")
ap.add_argument("-s", "--size", type=int, default=128,
	help="size of queue for averaging")
ap.add_argument("-a", "--action", required=True, help="choose a predictive action from the list [drinking, cooking]")
args = ap.parse_args()

# load the trained model and label binarizer from disk
print("[INFO] loading model and label binarizer...")
model = load_model(args.model)
lb = pickle.loads(open(args.label_bin, "rb").read())

# initialize the image mean for mean subtraction along with the
# predictions queue
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
Q = deque(maxlen=args.size)

# initialize the video stream, pointer to output video file, and
# frame dimensions
vs = cv2.VideoCapture(args.input)
writer = None
(W, H) = (None, None)


# list of lists [time(milsec), binary_label]
timeStamps = []
# loop over frames from the video file stream
while True:
	# read the next frame from the file
	(grabbed, frame) = vs.read()

	# if the frame was not grabbed, then we have reached the end
	# of the stream
	if not grabbed:
		break

	# if the frame dimensions are empty, grab them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# clone the output frame, then convert it from BGR to RGB
	# ordering, resize the frame to a fixed 224x224, and then
	# perform mean subtraction
	output = frame.copy()
	# output = cv2.resize(frame.copy(), (244,244))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.resize(frame, (224, 224)).astype("float32")
	frame -= mean
	
	# make predictions on the frame and then update the predictions
	# queue
	preds = model.predict(np.expand_dims(frame, axis=0))[0]
	Q.append(preds)

	# perform prediction averaging over the current history of
	# previous predictions
	results = np.array(Q).mean(axis=0)
	i = np.argmax(results)
	label = lb.classes_[i]

	if label == args.action:
		# get the frame time
		ts = round(vs.get(cv2.CAP_PROP_POS_MSEC), 15)
		# appending time, label to the list
		timeStamps.append([round(ts, 16), round(max(results), 5)])

	# draw the activity on the output frame
		text = "activity: {}".format(label)
		cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 255, 0), 2)
	else:
		cv2.putText(output, 'computing...', (10, 25), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
	# cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,
		# 1.25, (0, 255, 0), 2)

	# check if the video writer is None
	if writer is None:
		# initialize our video writer
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args.output, fourcc, 30,
			(W, H), True)

	# write the output frame to disk
	writer.write(output)

	# show the output image
	cv2.imshow("Output", output)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# release the file pointers
print("[INFO] labled video saved to the folder...")
writer.release()
vs.release()

# creating json file as: timeLabel.json
print("[INFO] writing json time-label...")
to_json_file(args.action, timeStamps)

print("[INFO] saving time-label figure to the folder...")
x_p = [item[0] for item in timeStamps]
y_p = [item[1] for item in timeStamps]
x_np_param = np.array(x_p)
y_np_param = np.array(y_p)

fig_plot(x_np_param, y_np_param, args.action)

print("[INFO] DONE...")





# python predict_video.py --model model/model_v5/activity.model --label-bin model/model_v5/lb.pickle --input example_clips/v5/cook5.mp4 --output output/output_v5/c5_v5.avi --action cooking --size 128