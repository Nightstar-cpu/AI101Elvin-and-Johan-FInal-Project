#Streamlit application
import boto3
import streamlit as st
import numpy as np
import pandas as pd
import pickle

AWS_ACCESS_KEY_ID = 'AKIAXYKJQIA5RQJH2XWZ' # Change it with actual value of your AWS account.
AWS_SECRET_ACCESS_KEY = 'Rg3PX4kY7rLhrQvGsXHydZYIuFiGpr/XBlFqaAcx' # Change it with actual value of your AWS account.


session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

s3 = session.resource('s3')

bucket = "ai101"
key = 'johan/churn_model.pkl'

ChurnFinder = pickle.loads(s3.Bucket(bucket).Object(key).get()['Body'].read())

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def ChurnPredictor(AGE, EXITED, GENDER, TENURE, BALANCE, SURNAME, GEOGRAPHY, HASCRCARD, CUSTOMERID, CREDITSCORE, NUMOFPRODUCTS, ISACTIVEMEMBER, ESTIMATEDSALARY):
    
    prediction = ChurnFinder.predict([[AGE, EXITED, GENDER, TENURE, BALANCE, SURNAME, GEOGRAPHY, HASCRCARD, CUSTOMERID, CREDITSCORE, NUMOFPRODUCTS, ISACTIVEMEMBER, ESTIMATEDSALARY]])
    print(prediction)
    return prediction

def main():
    st.title("Churn Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Churn Prediction ML
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    AGE = st.text_input("Age","Type Here")
    EXITED = st.selectbox("Exited",("Yes","No"))
    if EXITED == "Yes":
        EXITED = 1
    else:
        EXITED = 0
    GENDER = st.selectbox("Gender", ("Male", "Female"))
    TENURE = st.text_input("Tenure(in years)","Type Here")
    BALANCE = st.text_input("Balance","Type Here")
    SURNAME = st.text_input("Last Name","Type Here")
    GEOGRAPHY = st.selectbox("Country", ("Germany","Spain","France"))
    HASCRCARD = st.selectbox("Has a Credit Card",("Yes","No"))
    if HASCRCARD == "Yes":
        HASCRCARD = 1
    else:
        HASCRCARD = 0
    CUSTOMERID = st.text_input("Customer ID", "Type Here")
    CREDITSCORE = st.text_input("Credit Score", "Type Here")
    NUMOFPRODUCTS = st.text_input("Number of Products", "Type Here")
    ISACTIVEMEMBER = st.selectbox("Is An Active Member",("Yes","No"))
    if ISACTIVEMEMBER == "Yes":
        ISACTIVEMEMBER = 1
    else:
        ISACTIVEMEMBER = 0
    ESTIMATEDSALARY = st.text_input("Estimated Salary","Type Here")

    result=0
    if st.button("Predict"):
        result=ChurnPredictor(AGE, EXITED, GENDER, TENURE, BALANCE, SURNAME, GEOGRAPHY, HASCRCARD, CUSTOMERID, CREDITSCORE, NUMOFPRODUCTS, ISACTIVEMEMBER, ESTIMATEDSALARY)
    st.success('the output is {}'.format(result))
    if st.button("About"):
        st.text("Project Done by Elvin and Johan")

if __name__=='__main__':
    main()


