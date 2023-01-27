import pickle
import streamlit as st
#import tensorflow as tf
#from tensorflow import keras
print("Welcome to the web app")
model = pickle.load(open('ann_model.pkl', 'rb'))

def main():
    st.title('Student Performance Prediction System')

    #input variables
    gender = st.selectbox(
      """gender
      0: female, 1: male""",    
      ('0', '1'))
    place_of_residence = st.selectbox(
      """Place of Residence
      0: Hostel, 1: Off Campus""",    
      ('0', '1'))
    parent_marital_status = st.selectbox(
      """Parental Marital Status
      0: Divorced, 1: Together""",    
      ('0', '1'))
    family_size = st.selectbox(
      """Family Size
      0: Large, 1: Medium, 2: Small""",    
      ('0', '1', '2'))
    mode_of_transportation = st.selectbox(
      """Mode of Transportation
      0: bus, 1: vehicle ownership, 2: walking""",    
      ('0', '1', '2'))
    elementary_education = st.selectbox(
      """Elementary education type
      0: Government, 1: Private""",    
      ('0', '1'))
    higher_institution_location = st.text_input(
    """Higher insitution location
      0: Rural, 1: Urban""",    
      ('0', '1'))


    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[gender, place_of_residence, parent_marital_status, family_size, mode_of_transportation, elementary_education, higher_institution_location]])
        output = round(makeprediction[0],0)
        if output == 0:
            st.success('You are likely to get an A')
        elif output == 1.0:
            st.success('You are likely to get an F')


if __name__ =='__main__':
    main()
