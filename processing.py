# Create the prediction pipeline to combine the 2 best models.
# import libraries
import pandas as pd
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import shutil
from PIL import Image
import os
from models import buildClassifer
from models import buildSegmentation

def segment_tumor_mask(X):
  '''
  Predition Pipeline
  Reads: Original Images
  Classifier predicts the presence of a tumor, if present the Segmentation model predicts the mask.
  Original Image, and corresponding predicted mask printed.
  Returns: Tumor Label, Predicted Mask.
  '''
  direc = os.getcwd()+'\\'
  label = True
  clfmodel = buildClassifer()
  segmodel = buildSegmentation()

  # Load test image and standardize it
  img = Image.open(X)
  img = np.array(img)
  img = cv2.resize(img,(256,256))
  img = img * 1.0/255.0
  img = np.expand_dims(img,axis=0)

  pred = clfmodel.predict(img, verbose=0) # Predict tumor status
  if pred[0][0] < 0.5: # Predict labels from the probability values
    predStatus = 0    
  else:
    predStatus = 1

  #original image
  image = Image.open(X)
  image = np.array(image)
  image = cv2.resize(image, (256,256))
  # plot  
  plt.figure(figsize=(10,6))
  plt.subplot(121)
  plt.axis("off")
  plt.title("Original Image")
  plt.imshow(image)
  plt.savefig(direc+'orgImage.tif')  
  if(predStatus==0): # Check classifier prediction label    
    label = False
    prediction = cv2.imread(direc+'orgImage.tif')
  else:
    #predicted segmentation map
    p = image
    p = p/255
    p = np.expand_dims(p,axis=0)
    pred_mask = segmodel.predict(p,verbose=0) # Predict Mask
    pred_mask = np.argmax(pred_mask[0],axis=-1)
    plt.subplot(122)
    plt.axis("off")
    plt.title("Predicted Mask")
    plt.imshow(pred_mask)
    plt.savefig(direc+'predicted_mask.tif')
    prediction = cv2.imread(direc+'predicted_mask.tif')
  plt.show()
  return label, prediction