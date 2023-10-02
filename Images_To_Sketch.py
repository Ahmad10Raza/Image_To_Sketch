import streamlit as st #   used for creating web apps
from PIL import Image #   used for loading images
from io import BytesIO #   used for reading images
import numpy as np #   used for numerical analysis
import cv2 #   used for computer vision


# Write the function to convert an image to a water color sketch
def convert_to_waterColorSketch(input_img):
    #  edgePreservingFilter() is used to reduce noise in the image
    img_1 = cv2.edgePreservingFilter(input_img, flags=2, sigma_s=50, sigma_r=0.8) 
    # stylization() is used to apply water color sketching effect
    img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return(img_water_color) #  return the water color sketch



# Write the function to convert an image to a pencil sketch

def convert_to_pencilSketch(input_img):
    # pencilSketch() is used to apply pencil sketching effect
    img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch(input_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
    return(img_pencil_sketch) #  return the pencil sketch


# Write the function to load an image
def load_an_image(image):
    img = Image.open(image)
    return img #  return the image



# Write the main function which has the code for the web application

def main():
    
    # basics interface for web app
    st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH') #  title of the web app
    st.write("This is an application developed for converting your ***image*** to a ***Water Color Sketch*** OR ***Pencil Sketch***") #  description of the web app
    st.subheader("Please Upload your image") #  subheader of the web app
    
    
    # uploading the image
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"]) #  file uploader
    
    
    # now images is uploded time for action
    
    # if image is uploaded then execute these lines of code
    if image_file is not None:
        
        # creating options box for choosing between water color / pencil sketch
        option = st.selectbox('How would you like to convert the image',
                              ('Convert to water color sketch', 'Convert to pencil sketch'))
        
        # if water color sketch is selected then execute these lines of code
        if option =='Convert to water color sketch':
            image = Image.open(image_file)
            final_sketch = convert_to_waterColorSketch(np.array(image)) # calling the function to convert the image to water color sketch
            im_pil = Image.fromarray(final_sketch) # converting the image to array
            
            # two columns to display the original image and the image after applying water color sketching effect
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)
            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil, width=250) #  displaying the water color sketch
                buf = BytesIO() #  reading the image
                img = im_pil #  storing the image
                img.save(buf, format='PNG') #  saving the image
                byte_im = buf.getvalue()
                st.download_button(label="Download",
                                   data=byte_im,
                                   file_name="Output_Sketch.png",
                                   mime="image/png") #  download button for downloading the water color sketch
                
                
                
        # if pencil sketch is selected then execute these lines of code
        if option =='Convert to pencil sketch':
            image = Image.open(image_file)
            final_sketch = convert_to_pencilSketch(np.array(image))  # calling the function to convert the image to pencil sketch
            im_pil = Image.fromarray(final_sketch)
            
            # two columns to display the original image and the image after applying pencil sketching effect
            col1, col2 = st.columns(2)
            
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)
                
            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format='PNG')
                byte_im = buf.getvalue()
                st.download_button(label="Download",
                                   data=byte_im,
                                   file_name="Output_Sketch.png",
                                   mime="image/png")
                
                
                
if __name__ == "__main__":
    main()
                
            