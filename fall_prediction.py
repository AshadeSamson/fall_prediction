import os
import pickle
import streamlit as st

file_path = "svm_classifier.pkl"
classifier = None 


if os.path.exists(file_path):
    try:
        with open(file_path, 'rb') as pickle_in:
            classifier = pickle.load(pickle_in)
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.error(f"Model file not found: {file_path}")
    st.stop()




def predict_fall(distance,pressure,hrv,sugarlevel,spO2,accelerometer):
   
    prediction = classifier.predict([[distance,pressure,hrv,sugarlevel,spO2,accelerometer]])
    print(prediction)
    return prediction[0]





def main():
    st.title("Elderly Fall Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Elderly Fall Predictor App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    _distance = st.number_input("Distance", 0)
    distance = float(_distance)
    _pressure = st.selectbox("Pressure", options=[0, 1, 2])
    pressure = float(_pressure)
    _hrv = st.number_input("HRV Level", 0)
    hrv = float(_hrv)
    _sugarLevel = st.number_input("Sugar Level", 0)
    sugarLevel = float(_sugarLevel)
    _sp02 = st.number_input("spO2", 0)
    sp02 = float(_sp02)
    _accelerometer = st.selectbox("Accelerometer Reading", options=[0, 1])
    accelerometer = float(_accelerometer)
    result=""
    if st.button("Predict"):
        prediction = predict_fall(distance,pressure,hrv,sugarLevel,sp02,accelerometer)
        if prediction == 0:
            result = "No fall"
        elif prediction == 1:
            result = "fair fall"
        else:
            result = "Fall"    
    st.success('The Decision is "{}"'.format(result))


if __name__=='__main__':
    main()