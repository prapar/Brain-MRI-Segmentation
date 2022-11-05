import streamlit as st
import numpy as np
import pandas as pd
from processing import *

flag = False

st.title('Brain Tumor MRI Segmentation')
st.subheader('Upload the brain MRI scan image(s)  in .tif/.png/.jpg format')

with st.form("my-form", clear_on_submit=True):
        uploaded_file = st.file_uploader(' ',accept_multiple_files = True)
        submitted = st.form_submit_button("Submit")

if len(uploaded_file) != 0:
    st.write("Upload Successful...")
else:
    st.write("No file uploaded!")
st.markdown("*"*50)

# Check file format
for i in range(len(uploaded_file)):
    if(not any([uploaded_file[i].name.endswith('.tif'), uploaded_file[i].name.endswith('.jpg'), uploaded_file[i].name.endswith('.png')])):
        st.write("Incompatible file format: ",uploaded_file[i].name)
        flag = True
    
if(not flag):    
    for i in range(len(uploaded_file)):        
        label, prediction = segment_tumor_mask(uploaded_file[i])
        if (not label):
            st.write("NO TUMOR DETECTED IN THE BELOW IMAGE: ",uploaded_file[i].name)
            st.image(prediction)
        else:
            st.write("TUMOR DETECTED IN THE BELOW IMAGE: ",uploaded_file[i].name)
            st.image(prediction)      

else:
    uploaded_file = st.empty()
    st.runtime.legacy_caching.clear_cache() 
    st.write("Try uploading again...")

 