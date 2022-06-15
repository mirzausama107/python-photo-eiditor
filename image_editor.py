from ssl import Options
import streamlit as st
import io
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

st.set_page_config(
    page_title="Python Image Editor",
    page_icon=":tada:"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.write("# Python Image Editor")


image_file = st.file_uploader(
    "Upload an image", type=['png', 'jpg', 'jpeg'])
# for uploaded_file in uploaded_files:

options = ''
if image_file is not None:
    bytes_data = image_file.read()
    st.write("Original Image", alignment='center')
    stream = io.BytesIO(bytes_data)
    image = Image.open(stream)
    st.image(image, width = 400)

    with st.sidebar:
        # st.write("Choose Filter:")
        options = st.radio(
            "Choose Filter:",
            ('Original Image', 'GrayScale Image', 'Blurred Image', 'Black and White', 'Pencil Sketch', 'Detect Edges', 'Smoothened Image', 'Sharpened Image'))

if options == 'GrayScale Image':
    gray = image.convert('L')
    #gray = image.filter(EMBOSS)
    st.write("GrayScale Image")
    st.image(gray, width = 400)
# threshold 
elif options == 'Black and White':
    thresh_img = image.filter(FIND_EDGES)
    st.write("Black and White")
    st.image(thresh_img, width = 400)

elif options == 'Pencil Sketch':
    pencil_sketch = image.filter(CONTOUR)
    st.write("Pencil Sketch")
    st.image(pencil_sketch, width = 400)

elif options == 'Blurred Image':
    blur = image.filter(ImageFilter.BLUR)
    st.write("Blurred Image")
    st.image(blur, width = 400)
elif options == 'Detect Edges':
    imageWithEdges = image.filter(ImageFilter.FIND_EDGES)
    st.write("Edges Detected Image")
    st.image(imageWithEdges, width = 400)
elif options == 'Smoothened Image':
    smoothenedImage = image.filter(ImageFilter.SMOOTH)
    st.write("Smoothened Image")
    st.image(smoothenedImage, width = 400)
elif options == 'Sharpened Image':
    sharpened_img = image.filter(ImageFilter.SHARPEN)
    st.write("Edges Detected Image")
    st.image(sharpened_img, width = 400)