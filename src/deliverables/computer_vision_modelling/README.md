# CNG Scooter Detection
Custom Data Source: `/src/data/Computer Vision Dataset/dataset.zip`

## How to Use

 * Clone YOLOv5 from [here](https://github.com/ultralytics/yolov5).

 * To train again with the CNG Scooter dataset follow the [Notebook]().
  
 * To utilise the trained model, copy the `best.pt` weights file from `computer_vision_modelling` folder  to `yolov5\runs\train\exp\weights\best.pt` 
  
*  Model can be loaded with pretrained load by following line: 
  
   `model = torch.hub.load('yolov5', 'custom', path=r'yolov5\runs\train\exp\weights\best.pt', source='local')`


# Vechile Detection & Relative Velocity Measurement