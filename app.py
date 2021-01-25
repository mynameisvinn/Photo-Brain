from ShowMe import inference

import streamlit as st
from PIL import Image
import time


# render page with streamlit
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Casting Coin Photo Brain ")
st.write("")
file_up = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"] )

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    with st.spinner('Computing...'):
        time.sleep(1)
    score = inference(file_up)
    st.write("Score: ", score)
