# Activity Recognition
Action Recognition Deep Learning Project (recognizing drinking and cooking)

### Requirements

`pip install -r requirements.txt`

### Arguments

- `"m", "--model" :` path to trained serialized model
- `"-l", "--label-bin":` path to  label binarizer
- `"-i", "--input":` path to our input video (e.g. `example_clips/video.mp4`)
- `"-o", "--output":` path to our output video (e.g. `output/myVideo.avi`)
- `"-s", "--size":` size of queue for averaging (e.g. 128)
- `"-a", "--action":` choose a predictive action from this list (`drinking, cooking`). This name will be used in labeling the JSON file and the output figure y_label.
- `"-f", "--fig":` fig name
- `"-j", "--json":` JSON file name
***

### Instruction Video: [YOUTUBE LINK](https://youtu.be/Dvp9Gt67u_0)

***

### **Video Samples**

Download these two video samples and place them in 'example_clips' folder.

|Drinking Video Sample                 |Cooking Video Sample                 |
|:------------------------------------:|:-----------------------------------:|
|[drinking sample video](https://drive.google.com/file/d/1NPF8moT1vHqpVVUDzWF9w4tPk8pa6xOg/view?usp=sharing)|[cooking sample video](https://drive.google.com/file/d/1gdkGiOgwjlw4SL0z_nYG2kZo8CZcONyI/view?usp=sharing)|

### **Pre-Runing Instruction**

- Create a folder called `model`, download the **pre-trained model** [>>download link<<](https://drive.google.com/file/d/1GRIbAtAXXNm6RIBFTiVsyDVhl4VhTQoX/view?usp=sharing) and the **binarized Labels** [>>download link<<](https://drive.google.com/file/d/1AXemNFTtLYiLy8fyQ9S102v4YkxhHPHB/view?usp=sharing) add place them into the **model** folder.
- Create a folder called `output` for the code output.
- Create a folder called `example_clips` and put the above 'video samples' together with your test videos in it.

#### **Running Drinking Activity**
`python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/` **VIDEO-NAME** `--output output/output_video.avi --fig TimeLabel --json TimeLabel --action drinking --size 128`

#### **Running Cooking Activity**
`python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/` **VIDEO-NAME** `--output output/output_video.avi --fig TimeLabel --json TimeLabel --action cooking --size 128`
***
