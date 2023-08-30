"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Demenia.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    gender = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    edu = st.slider("Education Years", int(df["Edu"].min()), int(df["Edu"].max()))
    ses = st.slider("SES", int(df["SES"].min()), int(df["SES"].max()))
    mmse = st.slider("MMSE", int(df["MMSE"].min()), int(df["MMSE"].max()))
    cdr = st.slider("CDR", float(df["CDR"].min()), float(df["CDR"].max()))
    etiv = st.slider("eTIV", float(df["eTIV"].min()), float(df["eTIV"].max()))
    nwbv = st.slider("nWBV", float(df["nWBV"].min()), float(df["nWBV"].max()))
    asf = st.slider("ASF", float(df["ASF"].min()), float(df["ASF"].max()))
    # Create a list to store all the features
    features = [gender, age, edu, ses, mmse, cdr, etiv, nwbv, asf]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score#correction factor
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.error("The person has dementia")
        else:
            st.success("The person has no dementia")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", round((score*100)), "%")
        