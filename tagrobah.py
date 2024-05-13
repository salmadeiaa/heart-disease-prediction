import streamlit as st 
import pickle
import pandas as pd


st.title('Heart Disease Prediction app')
st.info('Application for Heart Disease Predection')
st.sidebar.header('Feature Selection')

Age=st.text_input('age')
Sex=st.text_input('sex')
RBP=st.text_input('resting blood pressure')
Serum_Cholesterol=st.text_input('serum cholestoral')
Thallium=st.text_input('thal')
Chest_pain_type=st.text_input('chest pain type')
EKG_results=st.text_input('resting electrocardiographic results')
FBS=st.text_input('fasting blood sugar')
Max_HR=st.text_input('max heart rate')
Exercise_angina=st.text_input('exercise induced angina')
ST_segment=st.text_input('ST segment')
major_vessels=st.text_input('major vessels')
Oldpeak=st.text_input('oldpeak')


df=pd.DataFrame({'age':[Age],'sex':[Sex],
'resting blood pressure':[RBP], 'serum cholestoral':[Serum_Cholesterol],
'thal':[Thallium],'Chest pain type':[Chest_pain_type],'EKG results':[EKG_results],
'fasting blood sugar':[FBS],'max heart rate':[Max_HR],'exercise induced angina':[Exercise_angina],'ST segment':[ST_segment],
'major vessels':[major_vessels],'oldpeak':[Oldpeak],
},index=[0])

model=pickle.load(open(r'D:\Education\university\6 term\machine learning\dataset_heart.sav','rb'))
Con=st.sidebar.button('confirm')
if Con:
    result=model.predict(df)
    st.write(result)
