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
    AGE = st.number_input("Age","Type a Number")
    GENDER = st.selectbox("Gender", ("Male", "Female"))
    TENURE = st.number_input("Tenure(in years)","Type a Number")
    BALANCE = st.number_input("Balance","Type a Number")
    SURNAME = st.text_input("Last Name","Type Here")
    GEOGRAPHY = st.selectbox("Country", ("Germany","Spain","France"))
    HASCRCARD = st.selectbox("Has a Credit Card",("Yes","No"))
    if HASCRCARD == "Yes":
        HASCRCARD = 1
    else:
        HASCRCARD = 0
    CUSTOMERID = st.number_input("Customer ID", "Type a Number")
    CREDITSCORE = st.number_input("Credit Score", "Type a Number")
    NUMOFPRODUCTS = st.number_input("Number of Products", "Type a Number")
    ISACTIVEMEMBER = st.selectbox("Is An Active Member",("Yes","No"))
    if ISACTIVEMEMBER == "Yes":
        ISACTIVEMEMBER = 1
    else:
        ISACTIVEMEMBER = 0
    ESTIMATEDSALARY = st.number_input("Estimated Salary","Type a Number")

    df = pd.DataFrame({'CustomerId' : CUSTOMERID,
                 'Surname' : SURNAME,
                 'CreditScore' : CREDITSCORE,
                 'Geography', : GEOGRPAHY,
                 'Gender', : GENDER,
                 'Age', : AGE,
                 'Tenure': TENURE,
                 'Balance': BALANCE,
                 'NumOfProducts': NUMOFPRODUCTS,
                 'HasCrCard': HASCRCARD,
                 'IsActiveMember': ISACTIVEMEMBER,
                 'EstimatedSalary': ESTIMATEDSALARY })
    df.drop(['Surname', 'CustomerId', 'Balance', 'EstimatedSalary', 'CreditScore'], axis=1, inplace=True)
    df = pd.get_dummies(df, columns=['Geography', 'Gender'])
    result=0
    
    if st.button("Predict"):
        result=ChurnPredictor(df)
    st.success('the output is {}'.format(result))
    if st.button("About"):
        st.text("Project Done by Elvin and Johan")

if __name__=='__main__':
    main()


