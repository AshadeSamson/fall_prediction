import pickle
import streamlit as st



pickle_in = open("random_forest.pkl","rb")
classifier = pickle.load(pickle_in)



def predict_fall(distance,pressure,hrv,sugarlevel,spO2,accelerometer):
   
    prediction = classifier.predict([[distance,pressure,hrv,sugarlevel,spO2,accelerometer]])
    print(prediction)
    return prediction





def main():
    st.title("Elderly Fall Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Elderly Fall Predictor App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    distance = st.text_input("Distance","Type Here")
    pressure = st.text_input("Pressure","Type Here")
    hrv = st.text_input("HRV Level","Type Here")
    sugarLevel = st.text_input("Sugar Level","Type Here")
    sp02 = st.text_input("spO2","Type Here")
    accelerometer = st.text_input("Accelerometer Reading","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_fall(distance,pressure,hrv,sugarLevel,sp02,accelerometer)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()