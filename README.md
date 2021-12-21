# Cell_tracking

**This repository allows you to view the execution process of the project in the form of an ipynb file and easily see the results.  
For more detailed code information, go to the https://github.com/krec7748/yolov4-deepsort.**  

![tracking_result_02](https://user-images.githubusercontent.com/86844420/146902101-7ed9906e-35e4-4423-adad-5f1d2cf9682b.gif)

## Process
### 1. Dataset Download
 - Glioblastoma-astrocytoma U373 cells on a polyacrylamide substrate  
   Dr. S. Kumar. Department of Bioengineering, University of California at Berkeley, Berkeley CA (USA)  
   Training dataset: http://data.celltrackingchallenge.net/training-datasets/PhC-C2DH-U373.zip (40 MB)  
   Challenge dataset: http://data.celltrackingchallenge.net/challenge-datasets/PhC-C2DH-U373.zip (38 MB)  
   - Reference: http://celltrackingchallenge.net/2d-datasets/


### 2. Resizing & Labeling image
* img_resize.py, rename_txt.py (Local)  
* labelImg.py  
   * Reference: https://github.com/tzutalin/labelImg  
    

### 3. Training custom yolo-v4 model
* Train_yolov4_custom_object_detector.ipynb (Colab, GPU)
* Reference: https://github.com/AlexeyAB/darknet


### 4. Running DeepSort
* Running_DeepSort.ipynb (Colab, GPU)  
* Reference: https://github.com/krec7748/yolov4-deepsort 
* Reference: https://github.com/theAIGuysCode/yolov4-deepsort
