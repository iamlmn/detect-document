# Detect-document

Instance segementation using MaskRCNN for localization of document (object) images.

### Usage instructions.

*  clone this repo 

*  To use pretrained coco weights, download h5 file from [here](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)

##### Install the required packaged

* `pip3 install -r requirements.txt`

* `cd samples\My_docs` 

##### To train the model with pretrained coco weights.

* `python3 doc.py train --dataset=/path/to/doc/dataset --weights=coco`

##### The model generates bounding boxes and segmentation masks for each instance of an object in the image

* run 'Inspect_docs_model.ipynb' where masked outputs are tested.

We can get the masked output from this ipynb.

##### Click [here] to go to annotation tool link 
1 Choose file directory

2 Annotate all the files with labels & polygons.

3 Export as Json and store it in train & val

##### Detecting border/corners using OpenCV

### Others simple choices:
###### Canny Edge Detection

> Converts to gray scale and reduces noise using bilateral filter , smoothening color preserving the edges though!
Uses adaptiveThreshold to calculate optimal threshold for small regions & to control lights.
Median filter for removing sall details.


> Edge detection doesn’t count with sides of the image, therefore in case that page touching a side of the image, the algorithm won’t produce a continuous, closed edge. 

 
> To prevent that we have to add small border, border 5 pixels wide works just fine. Finally, we can use Canny Edge Detection where we have to specify values of so called hysteresis thresholding, 
which separates edges into three groups: definitely an edge, definitely not an edge and something between.



##### GrabCut

> Getting foreground images with contour
