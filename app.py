import streamlit as st
import tensorflow as tf 
st.set_option('deprecation.showfileUploaderEncoding', False) #to ignore warnings
@st.cache(allow_output_mutation=True) #to save in cache memory

def load_model():
  model=tf.keras.models.load_model('/Users/apple/Desktop/Python/model_mobilenet.h5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Malaria Prediction
         """
         )
file = st.file_uploader("Please upload a blood sample image", type=["jpg", "png"])

import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    image=cv2.imread(image_path)
    image=cv2.resize(image, (100, 100))
    x=np.expand_dims(image, axis=0)
    x=preprocess_input(x)
    result=model.predict(x)
    if result[0][0]*100>result[0][1]*100:
        print('Infected with Malaria')
    else:
        print('Not Infected')
    
    return prediction
if file is None:
    st.text('please upload a blood sample for prediction')
else:
    image=Image.open(file)
    st.image(image, use_column_width=True)
    predictions=import_and_predict(image, model)
    string='You are' + predictions
    st.sucess(string)


    
