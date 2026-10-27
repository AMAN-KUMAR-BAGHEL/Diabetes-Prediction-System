# -*- coding: utf-8 -*-
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open('Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))
lungs_disease_model = pickle.load(open('Models/lungs_disease_model.sav', 'rb'))
Thyroid_model = pickle.load(open('Models/Thyroid_model.sav','rb'))

# Page Layout
st.markdown("""
    <style>
    .main { background-color: #F0F2F6; }
    .stButton>button { background-color: #4CAF50; color: white; }
    .stTabs>div>div { border-bottom: 4px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# Tab Navigation
tabs = st.tabs(["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction","Lung Cancer Prediction","Hypo-Thyroid Prediction"])

# Diabetes Prediction Page
with tabs[0]:
    st.title('Diabetes Prediction Using ML')
    st.write("Select the following details to predict Diabetes:")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)    
    Pregnancies = col1.slider('Number of Pregnancies', 0, 20, 0)
    Glucose = col2.slider('Glucose Level', 0, 120, 120)
    BloodPressure = col3.slider('Blood Pressure value', 0, 200, 80)
    SkinThickness = col1.slider('Skin Thickness value', 0, 100, 20)
    Insulin = col2.slider('Insulin Level', 0, 900, 30)
    BMI = col3.slider('BMI value', 0.0, 70.0, 25.0)
    DiabetesPedigreeFunction = col1.slider('Diabetes Pedigree Function value', 0.0, 2.5, 0.5)
    Age = col2.slider('Age of the Person', 1, 100, 25)
    
    # backend logic
    diab_diagnosis = ''

    # Creation of a button
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
with tabs[1]:
    st.title('Heart Disease Prediction Using ML')
    st.write("Select the following details to predict Heart Disease:")
   
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = col1.slider('Age', 1, 100, 50)
    with col2:
        sex = col2.radio('Sex', ['Male', 'Female'])
    with col3:
        cp = col3.selectbox('Chest Pain types', ['Type 1', 'Type 2', 'Type 3', 'Type 4'])
    with col1:
        trestbps = col1.slider('Resting Blood Pressure', 0, 200, 120)
    with col2:
        chol = col2.slider('Serum Cholestoral in mg/dl', 100, 600, 200)
    with col3:
        fbs = col3.radio('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    with col1:
        restecg = col1.radio('Resting Electrocardiographic results', ['Normal', 'Abnormal'])
    with col2:
        thalach = col2.slider('Maximum Heart Rate achieved', 50, 220, 150)
    with col3:
        exang = col3.radio('Exercise Induced Angina', ['Yes', 'No'])
    with col1:
        oldpeak = col1.slider('ST depression induced by exercise', 0.0, 10.0, 1.0)
    with col2:
        slope = col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
    with col3:
        ca = col3.slider('Major vessels colored by fluoroscopy', 0, 4, 0)
    with col1:
        thal = col1.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])
    
    # Convert categorical variables to numeric values
    sex_numeric = 1 if sex == 'Male' else 0
    fbs_numeric = 1 if fbs == 'Yes' else 0
    exang_numeric = 1 if exang == 'Yes' else 0
    restecg_numeric = 1 if restecg == 'Abnormal' else 0
    slope_numeric = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}.get(slope, 0)
    thal_numeric = {'Normal': 1, 'Fixed Defect': 2, 'Reversable Defect': 3}.get(thal, 0)
    cp_numeric = {'Type 1': 1, 'Type 2': 2, 'Type 3': 3, 'Type 4': 4}.get(cp, 0)  # Added conversion for cp
    
    # Backend logics
    Heart_diagnosis = ''
    
    # Creation of a button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach, exang_numeric, oldpeak, slope_numeric, ca, thal_numeric]
        Heart_Prediction = heart_disease_model.predict([user_input])
        Heart_diagnosis = 'The person is having Heart disease' if Heart_Prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(Heart_diagnosis)

# Parkinsons Prediction Page
with tabs[2]:
    st.title("Parkinson's Disease Prediction Using ML")
    st.write("Select the following details to predict Parkinson's disease:")
    
    # Getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    
    fo = col1.slider('MDVP:Fo(Hz)', 0, 300, 150)
    
    fhi = col2.slider('MDVP:Fhi(Hz)', 0, 600, 300)
    
    flo = col3.slider('MDVP:Flo(Hz)', 0, 250, 125)

    Jitter_percent = col4.slider('MDVP:Jitter(%)', 0.0, 0.5, 0.25)

    Jitter_Abs = col5.slider('MDVP:Jitter(Abs)', 0.0, 0.5, 0.25)

    RAP = col1.slider('MDVP:RAP', 0.0, 0.5, 0.25)

    PPQ = col2.slider('MDVP:PPQ', 0.0, 0.5, 0.25)

    DDP = col3.slider('Jitter:DDP', 0.0, 0.5, 0.25)

    Shimmer = col4.slider('MDVP:Shimmer', 0.0, 0.5, 0.25)

    Shimmer_dB = col5.slider('MDVP:Shimmer(dB)', 0.0, 1.5, 0.75)

    APQ3 = col1.slider('Shimmer:APQ3', 0.0, 0.5, 0.25)

    APQ5 = col2.slider('Shimmer:APQ5', 0.0, 0.5, 0.25)

    APQ = col3.slider('MDVP:APQ', 0.0, 0.5, 0.25)

    DDA = col4.slider('Shimmer:DDA', 0.0, 0.5, 0.25)

    NHR = col5.slider('NHR', 0.0, 0.5, 0.25)

    HNR = col1.slider('HNR', 0, 35, 20)

    RPDE = col2.slider('RPDE', 0.0, 1.5, 0.75)

    DFA = col3.slider('DFA', 0.0, 1.5, 0.75)

    spread1 = col4.slider('spread1', -8, -2, -5)

    spread2 = col5.slider('spread2', 0.0, 0.5, 0.25)

    D2 = col1.slider('D2', 1, 4, 2)

    PPE = col2.slider('PPE', 0.0, 1.0, 0.5)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
with tabs[3]:    
    st.title("Lung Cancer Prediction Using ML")
    st.write("Select the following details to predict lung cancer:")
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        GENDER = col1.radio('Select gender of the person',['Male', 'Female'])
    with col2:
        AGE = col2.slider('Select age of the person', 1, 100, 75)
    with col3:
        SMOKING = col3.radio('Select if the person smokes',['Yes', 'No'])
    with col1:
        YELLOW_FINGERS = col1.radio('Select if the person has yellow fingers',['Yes', 'No'])
    with col2:
        ANXIETY = col2.radio('Select if the person has anxiety',['Yes', 'No'])
    with col3:
        PEER_PRESSURE = col3.radio('Select if the person is under peer pressure',['Yes', 'No'])
    with col1:
        CHRONIC_DISEASE = col1.radio('Select if the person has a chronic disease',['Yes', 'No'])
    with col2:
        FATIGUE = col2.radio('Select if the person experiences fatigue',['Yes', 'No'])
    with col3:
        ALLERGY = col3.radio('Select if the person has allergies',['Yes', 'No'])
    with col1:
        WHEEZING = col1.radio('Select if the person experiences wheezing',['Yes', 'No'])
    with col2:
        ALCOHOL_CONSUMING = col2.radio('Select if the person consumes alcohol',['Yes', 'No'])
    with col3:
        COUGHING = col3.radio('Select if the person experiences coughing',['Yes', 'No'])
    with col1:
        SHORTNESS_OF_BREATH = col1.radio('Select if the person experiences shortness of breath',['Yes', 'No'])
    with col2:
        SWALLOWING_DIFFICULTY = col2.radio('Select if the person has difficulty swallowing',['Yes', 'No'])
    with col3:
        CHEST_PAIN = col3.radio('Select if the person experiences chest pain',['Yes', 'No'])

    # Convert categorical variables to numeric values
    gender_numeric = 1 if GENDER == 'Male' else 0
    smoking_numeric = 1 if SMOKING == 'Yes' else 0
    yellow_fingers_numeric = 1 if YELLOW_FINGERS == 'Yes' else 0
    anxiety_numeric = 1 if ANXIETY == 'Yes' else 0
    peer_pressure_numeric = 1 if PEER_PRESSURE == 'Yes' else 0
    chronic_disease_numeric = 1 if CHRONIC_DISEASE == 'Yes' else 0
    fatigue_numeric = 1 if FATIGUE == 'Yes' else 0
    allergy_numeric = 1 if ALLERGY == 'Yes' else 0
    wheezing_numeric = 1 if WHEEZING == 'Yes' else 0
    alcohol_consuming_numeric = 1 if ALCOHOL_CONSUMING == 'Yes' else 0
    coughing_numeric = 1 if COUGHING == 'Yes' else 0
    shortness_of_breath_numeric = 1 if SHORTNESS_OF_BREATH == 'Yes' else 0
    swallowing_difficulty_numeric = 1 if SWALLOWING_DIFFICULTY == 'Yes' else 0
    chest_pain_numeric = 1 if CHEST_PAIN == 'Yes' else 0
    
    # Backend logics
    lungs_diagnosis = ''
    
    # creating a button for Prediction
    if st.button("Lung Cancer Test Result"):
        
        user_input = [gender_numeric, AGE, smoking_numeric, yellow_fingers_numeric, anxiety_numeric, peer_pressure_numeric, chronic_disease_numeric, fatigue_numeric, allergy_numeric, wheezing_numeric, alcohol_consuming_numeric, coughing_numeric, shortness_of_breath_numeric, swallowing_difficulty_numeric, chest_pain_numeric]
        
        user_input = [float(x) for x in user_input]

        lungs_prediction = lungs_disease_model.predict([user_input])

        if lungs_prediction[0] == 1:
            lungs_diagnosis = "The person has lung cancer disease"
        else:
            lungs_diagnosis = "The person does not have lung cancer disease"

        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
with tabs[4]:   
    st.title("Hypo-Thyroid Prediction Using ML")
    st.write("Select the following details to predict hypo-thyroid disease:")
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = col1.slider('Select age of the person', 1, 100, 40)
    with col2:
        sex = col2.radio('Select sex of the person',['Male', 'Female'])
    with col3:
        on_thyroxine = col3.radio('Select if the person is on thyroxine',['Yes', 'No'])
    with col1:
        tsh = col1.slider('Select TSH level', 0, 530, 265)
    with col2:
        t3_measured = col2.radio('Select if T3 was measured',['Yes', 'No'])
    with col3:
        t3 = col3.slider('Select T3 level', 0, 12, 6)
    with col1:
        tt4 = col1.slider('Select TT4 level', 0, 430, 215)

    # Convert categorical variables to numeric values
    sex_numeric = 1 if GENDER == 'Male' else 0
    on_thyroxine_numeric = 1 if on_thyroxine == 'Yes' else 0
    t3_measured_numeric = 1 if on_thyroxine == 'Yes' else 0
    
    # Backend Logics
    thyroid_diagnosis = ''
    
    # creating a button for Prediction        
    if st.button("Thyroid Test Result"):
        
        user_input = [age, sex_numeric, on_thyroxine_numeric, tsh, t3_measured_numeric, t3, tt4]
        
        user_input = [float(x) for x in user_input]

        thyroid_prediction = Thyroid_model.predict([user_input])

        if thyroid_prediction[0] == 1:
            thyroid_diagnosis = "The person has Hypo-Thyroid disease"
        else:
            thyroid_diagnosis = "The person does not have Hypo-Thyroid disease"

        st.success(thyroid_diagnosis)