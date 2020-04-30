# Activity Recognition
Action Recognition Deep Learning Project

### Requirements

`pip install -r requirements.txt`

### Arguments

- `"m", "--model" :` path to trained serialized model
- `"-l", "--label-bin":` path to  label binarizer
- `"-i", "--input":` path to our input video (e.g. `example_clips/video.mp4`)
- `"-o", "--output":` path to our output video (e.g. `output/myVideo.avi`)
- `"-s", "--size":` size of queue for averaging (e.g. 128)
- `"-a", "--action":` choose a predictive action from this list (`drinking, cooking`). This name will be used in labeling the JSON file and the output figure y_label.
***

### Instruction Video: [LINK](https://youtu.be/Dvp9Gt67u_0)

***

### Video Samples

Download these two video samples and place them in 'example_clips' folder.

|Drinking Video Sample                 |Cooking Video Sample                 |
|:------------------------------------:|:-----------------------------------:|
|[drinking sample video](https://drive.google.com/file/d/1NPF8moT1vHqpVVUDzWF9w4tPk8pa6xOg/view?usp=sharing)|[cooking sample video](https://drive.google.com/file/d/1gdkGiOgwjlw4SL0z_nYG2kZo8CZcONyI/view?usp=sharing)|

### Pre-Runing Instruction

- Create a folder called `model`, download the **pre-trained model** [>>download link<<](https://drive.google.com/file/d/1V68ezH27WmSU0uAoITzemTNqE8tvM0h8/view?usp=sharing) and the **binarized Labels** [>>download link<<](https://drive.google.com/file/d/1VCa4NoTFjHTefBIzsx5RYOCVVHrBz2JM/view?usp=sharing) add place them into the **model** folder.
- Create a folder called `output` for the code output.
- Create a folder called `example_clips` and put the above 'video samples' together with your test videos in it.

#### Running Drinking Activity
`python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/` **VIDEO-NAME** `--output output/output_video.avi --action drinking --size 128`

#### Running Cooking Activity
`python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/` **VIDEO-NAME** `--output output/output_video.avi --action cooking --size 128`
***
<!---
### Previous Projects

- #### Report: 1. [drinking](https://drive.google.com/file/d/1YqWGvZUGXuv7tw1MbpSnm9rByBTuu8Ob/view?usp=sharing) 2. [cooking](https://drive.google.com/file/d/1vGiTdP4TwbFTYxhbpMdxjYWJG0ZPDahq/view?usp=sharing)

|Drinking Video Samples                |Cooking Video Samples                |
|:------------------------------------:|:-----------------------------------:|
|[drink1](https://youtu.be/epeNAmsSaT8)|[cook1](https://youtu.be/fcBFr5MDm-Y)|
|[drink2](https://youtu.be/Me9ukITLTfk)|[cook2](https://youtu.be/oiKxjYLTDHA)|
|[drink3](https://youtu.be/E8W2hXuCivw)|[cook3](https://youtu.be/0Cac3yVfR7E)|
|[drink4](https://youtu.be/JCjt7vHeY_U)|[cook4](https://youtu.be/jElkBPTWpSU)|
|[drink5](https://youtu.be/LGWF0j00oMI)|[cook5](https://youtu.be/2DGt6KwJVSQ)|

***


- #### Report: [drinking-cooking](https://drive.google.com/file/d/1IEA0TS9BO23_ImJfQxWgsdUvnWLZsXSJ/view?usp=sharing)

|Drinking Video Samples                |Cooking Video Samples                |
|:------------------------------------:|:-----------------------------------:|
|[drinking sample videos folder](https://drive.google.com/drive/folders/1Ia1E0FSuP2wjPI6v4mkWy1F-L9kGGTGL?usp=sharing)|[cooking sample videos folder](https://drive.google.com/drive/folders/1HUQXfsD-nGB3kqrDES26gJfrShpygTfn?usp=sharing)|

If you want to check the labeled videos (saved after running the prediction), I have put the link here:

|Labeled Drinking Video Samples        |Labeled Cooking Video Samples        |
|:------------------------------------:|:-----------------------------------:|
|[drinking labeled videos folder](https://drive.google.com/drive/folders/1jdfmDKWDQyEzrk9WoRg5HnojnJgxibMy?usp=sharing)|[cooking labeled videos folder](https://drive.google.com/drive/folders/11xIB3F6CTnzxgs_yk8IiTPVukiS2nzQN?usp=sharing)|

***

### Final Project


|Drinking Video Sample                 |Cooking Video Sample                 |
|:------------------------------------:|:-----------------------------------:|
|[drinking sample video](https://drive.google.com/file/d/1NPF8moT1vHqpVVUDzWF9w4tPk8pa6xOg/view?usp=sharing)|[cooking sample video](https://drive.google.com/file/d/1gdkGiOgwjlw4SL0z_nYG2kZo8CZcONyI/view?usp=sharing)|

If you want to check the labeled videos (saved after running the prediction), I have put the link here:

|Labeled Drinking Video Samples        |Labeled Cooking Video Samples        |
|:------------------------------------:|:-----------------------------------:|
|[drinking labeled videos folder](https://drive.google.com/drive/folders/1X9EyKr7c5asKmPLM-SbXKEfGpD3Qwbt3?usp=sharing)|[cooking labeled videos folder](https://drive.google.com/drive/folders/1LnQMSKGpw0MqJDFMml6gS4RfB5ZzgTJX?usp=sharing)|
-->

