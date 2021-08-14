# CNG Scooter Detection
Custom Data Source: `/src/data/Computer Vision Dataset/dataset.zip`

## How to Use

 * Clone YOLOv5 from [here](https://github.com/ultralytics/yolov5).

 * To train again with the CNG Scooter dataset follow the [Notebook](https://github.com/OmdenaAI/omdena-bangladesh-roadsafety/blob/main/src/deliverables/computer_vision_modelling/CNG%20Scooter%20Detection/CNG_SCOOTER_Detection.ipynb).
  
 * To utilise the trained model, copy the `best.pt` weights file from `computer_vision_modelling` folder  to `yolov5\runs\train\exp\weights\best.pt` 
  
*  Model can be loaded with pretrained load by following line: 
  
   `model = torch.hub.load('yolov5', 'custom', path=r'yolov5\runs\train\exp\weights\best.pt', source='local')`


# Vechile Detection & Relative Velocity Measurement

##Relative velocity measurement:

  * Clone this github repository for using deepSORT object tracker: https://github.com/theAIGuysCode/yolov4-deepsort.git
  * Replace the object_tracker.py file in the parent directory with this one: src/deliverables/computer_vision_modelling/Vehicle detection and relative velocity/object_tracker.py
  * Create a new environment in anaconda named "yolov4-gpu" using: conda create -n yolov4-gpu
  * To use tensorflow with GPU, setup required versions of CUDA, CUDNN, Visual studio according to your tensorflow version:
    *To setup CUDA, CUDNN and VS follow: https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781
    *To check which version of CUDA, CUDNN is required for your specific tensorflow version check here: https://www.tensorflow.org/install/source#gpu
    *Please also check and make sure that your GPU's compute compatibility is >= 3.5    
  *  Activate your newly created environment: conda activate yolov4-gpu
  * save yolov4-tiny as tensorflow model (Use the trained weights on the 9 classes of vehicles): python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --model yolov4 --tiny
  * Run yolov4-tiny object tracker (Change the directory of the input and output video according to your need): python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ./data/video/test.mp4 --output ./outputs/tiny.avi --tiny
  
