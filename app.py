from ShowMe import inference

import streamlit as st
from PIL import Image


# render page with streamlit
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Predicting Instagrammable Images ")
st.write("")
file_up = st.file_uploader("Upload an image", type=["png", "jpg"] )

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    score = inference(file_up)
    st.write("Score: ", score)
