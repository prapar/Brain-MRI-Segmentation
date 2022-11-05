from tensorflow.keras.models import model_from_json
import os

direc = os.getcwd()+'\\'

def buildClassifer():
    # Load saved models and best weights
    # Classifier Model
    json_file = open(direc+r"model_save\Xception_Classifier.json", 'r')
    clfmodel_json = json_file.read()
    json_file.close()
    clfmodel = model_from_json(clfmodel_json)
    # load weights into new model
    clfmodel.load_weights(direc+r"model_save\Xception_Classifier.hdf5")
    return clfmodel

def buildSegmentation():
    # Load saved models and best weights
    # Segmentation Model
    json_file = open(direc+r"model_save\Unet.json", 'r')
    segmodel_json = json_file.read()
    json_file.close()
    segmodel = model_from_json(segmodel_json)
    # load weights into new model
    segmodel.load_weights(direc+r"model_save\Unet.hdf5")
    return segmodel