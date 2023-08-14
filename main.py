import streamlit as st
from PIL import Image
import io
import requests
from streamlit_lottie import st_lottie
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Union, Literal



def lottie(link):
    r = requests.get(link)
    if r.status_code == 200:
        
        return r.json() 


# load components

vairable = lottie("https://lottie.host/86a21742-82b5-47da-a36c-4f89cbae1525/agtGuTis5S.json")
download_animation = lottie('https://lottie.host/3d340d8c-bd91-4255-ba2a-3d4bc4d2ce2b/EHqWcc2XHq.json')
about_me_animation = lottie('https://lottie.host/7268302e-fa89-439e-8ffd-56ca480c78c6/bDnpWrfZo0.json')
success = lottie('https://lottie.host/d97e591b-0be5-4427-9e48-fea710b23c99/IYIisUnkTu.json')

# here we just initiated the website icon with the website name 
# used icon package is https://quickref.me/emoji.html
st.set_page_config(page_title = 'Pic Convertor',page_icon =':sunny:' , layout = "wide")

#----  HEADER -----
st.header("PNG to JPG convertor :fire:")
st.write('----')

# file handlers
with st.container():
    left_sec,right_sec = st.columns(2)
    with left_sec:
        st.write('Simple and Easy way to convert the PNG file to JPG file is to upload and click on convert now and Download it')
        upload_image = st.file_uploader("Upload the PNG", type = ["png"])
    with right_sec:
        st_lottie(vairable,height=300)



download_image = st.button("Convert Image")


# -- main program --
def convertor():
    if upload_image is not None:
        image = Image.open(upload_image)
        st.image(image, caption='Uploaded Image')

        if download_image:

            new_image_RGBA = image.convert('RGB')
            buffer = io.BytesIO()
            new_image_RGBA.save(buffer,format='JPEG')

            st.download_button(
                label="download converted image",
                data = buffer.getvalue(),
                file_name = 'new_image.jpg',
                mime="image/jpeg"
            )
            st.success(f"Image converted as new_image.jpg")
            st_lottie(success,height=100)


convertor()


# about creator 
st.write('##')
st.write('---')
with st.container():
    left,right = st.columns(2)
    with left:
        st.subheader('ABOUT ME')
        st.write('Hello there! Iam an aspiring Full stack developer in python basically Ive embarked on an exciting journey to bring innovative ideas to life through code and im trying different ideas like this website. It is basic idea to play with python in web development and i explored a lot by creating this website through streamlit ')
        st.write('[Contact>](https://udaychandp.github.io/web.resume/)')

    with right:
        st_lottie(about_me_animation,height=300)

# here to get the section we use st.write('---)
# for leaving space we use st.write('##)