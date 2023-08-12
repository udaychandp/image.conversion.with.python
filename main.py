import streamlit as st
from PIL import Image
import io



# here we just initiated the website icon with the website name 
# used icon package is https://quickref.me/emoji.html
st.set_page_config(page_title = 'Pic Convertor',page_icon =":sunny:" , layout = "wide")

#----  HEADER -----
st.header("PNG to JPG convertor :fire:")

# file handlers
upload_image = st.file_uploader("Upload the PNG", type = ["png"])
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
            

        
    
convertor()





















