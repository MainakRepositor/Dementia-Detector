"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Demenia Prediction System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            The dementia detection system employing a Random Forest Classifier demonstrates a promising approach in identifying and classifying dementia-related cognitive decline. Leveraging this machine learning technique, the system can efficiently analyze a diverse range of input variables, such as neuropsychological test results, brain imaging data, and demographic information. The Random Forest Classifier excels in handling complex, high-dimensional datasets and capturing intricate patterns that might be indicative of early stages of dementia. Through a process of ensemble learning, where multiple decision trees collaborate to make a robust prediction, the system enhances accuracy and minimizes overfitting. By continuously refining its model through training and validation, this technology holds the potential to aid clinicians in diagnosing dementia at an earlier stage, thus enabling timely interventions and improved patient care.
        </p>
    """, unsafe_allow_html=True)
