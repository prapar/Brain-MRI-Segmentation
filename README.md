# Brain-MRI-Segmentation

Overview

The problem statement is to identify tumors in the brain based on MRI scan
images of a patient. This will enable doctors/ medical professionals to delve
deeper into a patient’s condition based on the presence of tumor in their MRI
scan.
The data set we would use for this problem was obtained from TCIA – The
Cancer Imaging Archive. This data set can be sourced from Kaggle:
https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation
The dataset contains MRI scan images and their corresponding segmentation
masks, indicating the tumor status. This information will be used to train our
model. These images of 110 patients are collated in the dataset. There are
110 folders – one per patient and these have the images and masks in them.
There are 7858 images comprising of 3929 MRI Scan Images and 3929
corresponding Mask Images.

An example of an image and its mask are shown below. 
Each folder contains MRI images with the following naming convention: 
`TCGA_<institutioncode>_<patient-id>_<slice-number>.tif`. 
Corresponding masks have a `_mask` suffix.

Apart from these images we have patient data in medical terms related to
the tumor clusters. This information is not directly related to the image
segmentation problem itself, but gives us an idea about the tumor, its
location, age of patient, death event etc.

1 Patient
2 RNASeqCluster
3 MethylationCluster
4 miRNACluster
5 CNCluster
6 RPPACluster
7 OncosignCluster
8 COCCluster
9 histological_type
10 neoplasm_histologic_grade
11 tumor_tissue_site
12 laterality
13 tumor_location
14 gender
15 age_at_initial_pathologic
16 race
17 ethnicity
18 death01

Based on the images and mask information we will have to predict
segmentation masks to isolate tumors in the MRI scan images of patients,
enabling medical professionals to use the information like presence, shape,
location of the tumor from the segmentation masks predicted.
