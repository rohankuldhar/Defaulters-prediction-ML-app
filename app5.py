
import streamlit as st
import sklearn
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()


#Load the trained model
pickle_in=open("xgb_clf5.pkl","rb")
classifier=pickle.load(pickle_in)

@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs


def prediction(loan_amnt, term, int_rate, installment, annual_inc, dti, open_acc, pub_rec, revol_bal,
           revol_util, total_acc, mort_acc, pub_rec_bankruptcies, sub_grade_A2, sub_grade_A3, sub_grade_A4,
           sub_grade_A5, sub_grade_B1, sub_grade_B2, sub_grade_B3, sub_grade_B4, sub_grade_B5, sub_grade_C1,
           sub_grade_C2, sub_grade_C3, sub_grade_C4, sub_grade_C5, sub_grade_D1, sub_grade_D2, sub_grade_D3,
           sub_grade_D4, sub_grade_D5, sub_grade_E1, sub_grade_E2, sub_grade_E3, sub_grade_E4, sub_grade_E5,
           sub_grade_F1, sub_grade_F2, sub_grade_F3, sub_grade_F4, sub_grade_F5, sub_grade_G1, sub_grade_G2,
           sub_grade_G3, sub_grade_G4, sub_grade_G5, verification_status_Source_Verified,
           verification_status_Verified, purpose_credit_card, purpose_debt_consolidation,
           purpose_educational, purpose_home_improvement, purpose_house, purpose_major_purchase, purpose_medical,
           purpose_moving, purpose_other, purpose_renewable_energy, purpose_small_business, purpose_vacation,
           purpose_wedding, initial_list_status_w, application_type_INDIVIDUAL, application_type_JOINT,
           home_ownership_MORTGAGE, home_ownership_NONE, home_ownership_OTHER, home_ownership_OWN,
           home_ownership_RENT, zipcode_05113, zipcode_11650, zipcode_22690, zipcode_29597, zipcode_30723,
           zipcode_48052, zipcode_70466, zipcode_86630, zipcode_93700):
    
    # pre processing user input
        

    user_input=[[loan_amnt, term, int_rate, installment, annual_inc, dti, open_acc, pub_rec, revol_bal,
           revol_util, total_acc, mort_acc, pub_rec_bankruptcies, sub_grade_A2, sub_grade_A3, sub_grade_A4,
           sub_grade_A5, sub_grade_B1, sub_grade_B2, sub_grade_B3, sub_grade_B4, sub_grade_B5, sub_grade_C1,
           sub_grade_C2, sub_grade_C3, sub_grade_C4, sub_grade_C5, sub_grade_D1, sub_grade_D2, sub_grade_D3,
           sub_grade_D4, sub_grade_D5, sub_grade_E1, sub_grade_E2, sub_grade_E3, sub_grade_E4, sub_grade_E5,
           sub_grade_F1, sub_grade_F2, sub_grade_F3, sub_grade_F4, sub_grade_F5, sub_grade_G1, sub_grade_G2,
           sub_grade_G3, sub_grade_G4, sub_grade_G5, verification_status_Source_Verified,
           verification_status_Verified, purpose_credit_card, purpose_debt_consolidation,
           purpose_educational, purpose_home_improvement, purpose_house, purpose_major_purchase, purpose_medical,
           purpose_moving, purpose_other, purpose_renewable_energy, purpose_small_business, purpose_vacation,
           purpose_wedding, initial_list_status_w, application_type_INDIVIDUAL, application_type_JOINT,
           home_ownership_MORTGAGE, home_ownership_NONE, home_ownership_OTHER, home_ownership_OWN,
           home_ownership_RENT, zipcode_05113, zipcode_11650, zipcode_22690, zipcode_29597, zipcode_30723,
           zipcode_48052, zipcode_70466, zipcode_86630, zipcode_93700]]
    
    user_input=scaler.fit_transform(user_input)
    prediction = classifier.predict(user_input)
    
    if prediction == 1:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

# front end elements of the web page
def main():
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction App using Streamlit by Rohan Kuldhar</h1> 
    </div> 
    """
           
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # For dummy variables
    zipcode = st.selectbox('Zip Code',('zipcode_05113', 'zipcode_11650', 'zipcode_22690', 'zipcode_29597',
       'zipcode_30723', 'zipcode_48052', 'zipcode_70466', 'zipcode_86630',
       'zipcode_93700'))
    home_ownership = st.selectbox('Home Ownership',('home_ownership_MORTGAGE', 'home_ownership_NONE',
       'home_ownership_OTHER', 'home_ownership_OWN', 'home_ownership_RENT'))
    application_type = st.selectbox('Application Type',('application_type_INDIVIDUAL', 'application_type_JOINT'))
    initial_list_status = st.checkbox('initial_list_status_w')
    purpose = st.selectbox('Purpose',('purpose_credit_card', 'purpose_debt_consolidation',
       'purpose_educational', 'purpose_home_improvement', 'purpose_house',
       'purpose_major_purchase', 'purpose_medical', 'purpose_moving',
       'purpose_other', 'purpose_renewable_energy', 'purpose_small_business',
       'purpose_vacation', 'purpose_wedding'))
    verification_status=st.selectbox('Verification Status',('verification_status_Source_Verified', 'verification_status_Verified'))
    subgrade= st.selectbox('Subgrade Type',('sub_grade_A2', 'sub_grade_A3',
       'sub_grade_A4', 'sub_grade_A5', 'sub_grade_B1', 'sub_grade_B2',
       'sub_grade_B3', 'sub_grade_B4', 'sub_grade_B5', 'sub_grade_C1',
       'sub_grade_C2', 'sub_grade_C3', 'sub_grade_C4', 'sub_grade_C5',
       'sub_grade_D1', 'sub_grade_D2', 'sub_grade_D3', 'sub_grade_D4',
       'sub_grade_D5', 'sub_grade_E1', 'sub_grade_E2', 'sub_grade_E3',
       'sub_grade_E4', 'sub_grade_E5', 'sub_grade_F1', 'sub_grade_F2',
       'sub_grade_F3', 'sub_grade_F4', 'sub_grade_F5', 'sub_grade_G1',
       'sub_grade_G2', 'sub_grade_G3', 'sub_grade_G4', 'sub_grade_G5'))
    
    if subgrade=='sub_grade_A2':
        sub_grade_A2 = 1
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_A3':
        sub_grade_A2 = 0
        sub_grade_A3 = 1
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_A4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 4
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_A5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 1
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_B1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 1
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_B2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 1
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_B3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 1
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_B4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 1
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_B5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 1
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_C1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 1
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_C2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 1
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_C3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 1
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_C4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 1
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_C5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 1
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_D1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 1
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_D2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 1
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_D3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 1
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_D4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 1
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_D5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 1
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 1
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 1
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 1
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 1
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 1
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_E5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 1
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_F1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 1
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_F2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 1
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_F3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 1
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_F4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 1
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_F5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 1
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G1':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 1
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 1
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G2':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 1
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G3':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 1
        sub_grade_G4 = 0
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G4':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 1
        sub_grade_G5 = 0

    elif subgrade=='sub_grade_G5':
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 1

    else:
        sub_grade_A2 = 0
        sub_grade_A3 = 0
        sub_grade_A4 = 0
        sub_grade_A5 = 0
        sub_grade_B1 = 0
        sub_grade_B2 = 0
        sub_grade_B3 = 0
        sub_grade_B4 = 0
        sub_grade_B5 = 0
        sub_grade_C1 = 0
        sub_grade_C2 = 0
        sub_grade_C3 = 0
        sub_grade_C4 = 0
        sub_grade_C5 = 0
        sub_grade_D1 = 0
        sub_grade_D2 = 0
        sub_grade_D3 = 0
        sub_grade_D4 = 0
        sub_grade_D5 = 0
        sub_grade_E1 = 0
        sub_grade_E2 = 0
        sub_grade_E3 = 0
        sub_grade_E4 = 0
        sub_grade_E5 = 0
        sub_grade_F1 = 0
        sub_grade_F2 = 0
        sub_grade_F3 = 0
        sub_grade_F4 = 0
        sub_grade_F5 = 0
        sub_grade_G1 = 0
        sub_grade_G2 = 0
        sub_grade_G3 = 0
        sub_grade_G4 = 0
        sub_grade_G5 = 0


    if verification_status == 'verification_status_Source_Verified':
        verification_status_Source_Verified=1
        verification_status_Verified=0

    elif verification_status == 'verification_status_Verified':
        verification_status_Source_Verified=0
        verification_status_Verified=1

    else:
        verification_status_Source_Verified=0
        verification_status_Verified=0


    if purpose == 'purpose_credit_card':
        purpose_credit_card=1
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_debt_consolidation':
        purpose_credit_card=0
        purpose_debt_consolidation=1
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0   

    elif purpose == 'purpose_educational':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=1
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0    

    elif purpose == 'purpose_home_improvement':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=1
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_house':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=1
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_major_purchase':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=1
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_medical':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=1
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_moving':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=1
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_other':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=1
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_renewable_energy':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=1
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_small_business':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=1
        purpose_vacation=0
        purpose_wedding=0

    elif purpose == 'purpose_vacation':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=1
        purpose_wedding=0

    elif purpose == 'purpose_wedding':
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=1

    else:
        purpose_credit_card=0
        purpose_debt_consolidation=0
        purpose_educational=0
        purpose_home_improvement=0
        purpose_house=0
        purpose_major_purchase=0
        purpose_medical=0
        purpose_moving=0
        purpose_other=0
        purpose_renewable_energy=0
        purpose_small_business=0
        purpose_vacation=0
        purpose_wedding=0


    if initial_list_status== 'initial_list_status_w':
        initial_list_status_w=1

    else:
        initial_list_status_w=0


    if application_type== 'application_type_INDIVIDUAL':
        application_type_INDIVIDUAL=1
        application_type_JOINT=0


    elif application_type== 'application_type_INDIVIDUAL':
        application_type_INDIVIDUAL=0
        application_type_JOINT=1

    else:
        application_type_INDIVIDUAL=0
        application_type_JOINT=0


    if home_ownership=='home_ownership_MORTGAGE':
        home_ownership_MORTGAGE=1
        home_ownership_NONE=0
        home_ownership_OTHER=0
        home_ownership_OWN=0
        home_ownership_RENT=0

    elif home_ownership=='home_ownership_NONE':
        home_ownership_MORTGAGE=0
        home_ownership_NONE=1
        home_ownership_OTHER=0
        home_ownership_OWN=0
        home_ownership_RENT=0

    elif home_ownership=='home_ownership_OTHER':
        home_ownership_MORTGAGE=0
        home_ownership_NONE=0
        home_ownership_OTHER=1
        home_ownership_OWN=0
        home_ownership_RENT=0

    elif home_ownership=='home_ownership_OWN':
        home_ownership_MORTGAGE=0
        home_ownership_NONE=0
        home_ownership_OTHER=0
        home_ownership_OWN=1
        home_ownership_RENT=0

    elif home_ownership=='home_ownership_RENT':
        home_ownership_MORTGAGE=0
        home_ownership_NONE=0
        home_ownership_OTHER=0
        home_ownership_OWN=0
        home_ownership_RENT=1

    else:
        home_ownership_MORTGAGE=0
        home_ownership_NONE=0
        home_ownership_OTHER=0
        home_ownership_OWN=0
        home_ownership_RENT=0


    if zipcode=='zipcode_05113':
        zipcode_05113=1
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_11650':
        zipcode_05113=0
        zipcode_11650=1
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_22690':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=1
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_29597':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=1
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0   

    elif zipcode=='zipcode_30723':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=1
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_48052':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=1
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_70466':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=1
        zipcode_86630=0
        zipcode_93700=0

    elif zipcode=='zipcode_86630':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=1
        zipcode_93700=0

    elif zipcode=='zipcode_93700':
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=1

    else:
        zipcode_05113=0
        zipcode_11650=0
        zipcode_22690=0
        zipcode_29597=0
        zipcode_30723=0
        zipcode_48052=0
        zipcode_70466=0
        zipcode_86630=0
        zipcode_93700=0

    
    # following lines create boxes in which user can enter data required to make prediction
    loan_amnt=st.number_input('loan amount (Rs.)')
    term=st.radio("Select term: ", ('36', '60'))
    int_rate =st.number_input('Interest rate)')
    installment=st.number_input('Installment')
    annual_inc = st.number_input('Annual Income')
    dti=st.number_input('DTI')
    open_acc = st.number_input('Open accounts')
    pub_rec= st.number_input('Public Records')
    revol_bal = st.number_input('Revolving balance')
    revol_util = st.number_input('Revolving balance utilisation')
    total_acc = st.number_input('Total Accounts')
    mort_acc = st.number_input('Mortgage Accounts')
    pub_rec_bankruptcies = st.number_input('Public Recorded bankruptcies')
    result=""


    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(loan_amnt, term, int_rate, installment, annual_inc, dti, open_acc, pub_rec, revol_bal,
           revol_util, total_acc, mort_acc, pub_rec_bankruptcies, sub_grade_A2, sub_grade_A3, sub_grade_A4,
           sub_grade_A5, sub_grade_B1, sub_grade_B2, sub_grade_B3, sub_grade_B4, sub_grade_B5, sub_grade_C1,
           sub_grade_C2, sub_grade_C3, sub_grade_C4, sub_grade_C5, sub_grade_D1, sub_grade_D2, sub_grade_D3,
           sub_grade_D4, sub_grade_D5, sub_grade_E1, sub_grade_E2, sub_grade_E3, sub_grade_E4, sub_grade_E5,
           sub_grade_F1, sub_grade_F2, sub_grade_F3, sub_grade_F4, sub_grade_F5, sub_grade_G1, sub_grade_G2,
           sub_grade_G3, sub_grade_G4, sub_grade_G5, verification_status_Source_Verified,
           verification_status_Verified, purpose_credit_card, purpose_debt_consolidation,
           purpose_educational, purpose_home_improvement, purpose_house, purpose_major_purchase, purpose_medical,
           purpose_moving, purpose_other, purpose_renewable_energy, purpose_small_business, purpose_vacation,
           purpose_wedding, initial_list_status_w, application_type_INDIVIDUAL, application_type_JOINT,
           home_ownership_MORTGAGE, home_ownership_NONE, home_ownership_OTHER, home_ownership_OWN,
           home_ownership_RENT, zipcode_05113, zipcode_11650, zipcode_22690, zipcode_29597, zipcode_30723,
           zipcode_48052, zipcode_70466, zipcode_86630, zipcode_93700) 
        st.success('Your loan is {}'.format(result))
        print(loan_amnt)
st.write("Find me at  [link] (https://linkedin.com/in/rohan-kuldhar-89386114b)")
        
if __name__=='__main__': 
    main()
