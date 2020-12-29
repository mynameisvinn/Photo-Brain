import streamlit as st
from PIL import Image
from ShowMe import inference

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("ShowMe! Finding Instagrammable Images ")
st.write("")

file_up = st.file_uploader("Upload an image", type=["png", "jpg"] )

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")

    score = inference(file_up)
    st.write("Score: ", score)
    
