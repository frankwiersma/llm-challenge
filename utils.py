import streamlit as st
import base64

def display_instructions():
    # Markdown with some basic CSS styles for the box
    box_css = """
    <style>
        .instructions-box {
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
        }
    </style>
    """

    st.sidebar.markdown(box_css, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
    <div class="instructions-box">
        
    ### Instructions
    You can exploit this ReAct-based assistant via prompt 
    injection to get two flags:

    - **First Flag**: Access the documents of user with ID 2.
    - **Second Flag**: Retrieve the admin's password.

    To help you finish the challenge, we suggest you familiarize yourself with prompt injection techniques.

    </div>

    You'll also find the database schema to be useful:

    """
        ,
        unsafe_allow_html=True,
    )

    if st.sidebar.button('Show database schema', use_container_width=True):
        st.sidebar.info('Users(userId, username, password)\n\nDocuments(documentId, userId, title, content, confidential_level)')

# Function to convert image to base64
def get_image_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

def display_logo():
    # Convert your image
    image_base64 = get_image_base64("static/logo.png")

    # URL of the company website
    url = 'https://example.com/'

    # HTML for centered image with hyperlink
    html_string = f"""
    <div style="display:flex; justify-content:center;">
        <a href="{url}" target="_blank">
        <img src="data:image/png;base64,{image_base64}" width="150px">
        </a>
    </div>
    """
    # Display the HTML in the sidebar
    st.sidebar.markdown(html_string, unsafe_allow_html=True)