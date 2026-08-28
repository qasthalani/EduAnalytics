import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ==========================================
# 1. LOAD MODEL & SCALER
# ==========================================
@st.cache_resource
def load_artifacts():
    """
    Memuat model dan scaler. 
    Path disesuaikan agar menunjuk ke dalam folder 'model/'.
    """
    # PERBAIKAN PATH: Arahkan ke folder model/
    model_path = 'model/model (1).pkl'
    scaler_path = 'model/scaler.pkl'
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error(f"File model tidak ditemukan! Pastikan '{model_path}' ada.")
        return None, None
        
    with open(model_path, 'rb') as f_model:
        model = pickle.load(f_model)
        
    with open(scaler_path, 'rb') as f_scaler:
        scaler = pickle.load(f_scaler)
        
    return model, scaler

# ==========================================
# 2. MAIN PREDICTION PAGE
# ==========================================
st.title("Predict Dropout Potential")
st.markdown("""
Use the form below to simulate student data. 
The system will process these 10 indicators using the *Random Forest* model to predict the probability of dropout.
""")
st.divider()

# Load model
model, scaler = load_artifacts()

if model is not None and scaler is not None:
    # ==========================================
    # 3. UI FORM INPUT (LAYOUT 2 KOLOM)
    # ==========================================
    with st.form(key="prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Semester 1 Performance")
            cu_1st_approved = st.number_input("Semester 1 Approved Credits", min_value=0, max_value=30, value=5)
            cu_1st_grade = st.number_input("Semester 1 Average Grade", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
            cu_1st_evaluations = st.number_input("Semester 1 Number of Evaluations", min_value=0, max_value=30, value=6)

            st.subheader("Demographic & Enrollment Data")
            age_at_enrollment = st.number_input("Age at Enrollment", min_value=15, max_value=70, value=20)
            admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=130.0, step=0.5)

        with col2:
            st.subheader("Semester 2 Performance")
            cu_2nd_approved = st.number_input("Semester 2 Approved Credits", min_value=0, max_value=30, value=5)
            cu_2nd_grade = st.number_input("Semester 2 Average Grade", min_value=0.0, max_value=20.0, value=12.5, step=0.1)
            cu_2nd_evaluations = st.number_input("Semester 2 Number of Evaluations", min_value=0, max_value=30, value=6)

            st.subheader("Qualification & Risk")
            prev_qual_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, value=120.0, step=0.5)
            risk_level = st.selectbox(
                "Tingkat Risiko Awal", 
                options=[0, 1, 2], 
                format_func=lambda x: {0: "Low", 1: "Medium", 2: "High"}[x]
            )

        submit_button = st.form_submit_button(label="Run Prediction", use_container_width=True)

    # ==========================================
    # 4. PROCESS PREDICTION & DISPLAY RESULTS
    # ==========================================
    if submit_button:
        # Susun dictionary persis sesuai urutan fitur model
        input_dict = {
            'Curricular_units_2nd_sem_approved': [cu_2nd_approved],
            'Curricular_units_2nd_sem_grade': [cu_2nd_grade],
            'Risk_Level': [risk_level],
            'Curricular_units_1st_sem_approved': [cu_1st_approved],
            'Curricular_units_1st_sem_grade': [cu_1st_grade],
            'Curricular_units_2nd_sem_evaluations': [cu_2nd_evaluations],
            'Admission_grade': [admission_grade],
            'Previous_qualification_grade': [prev_qual_grade],
            'Curricular_units_1st_sem_evaluations': [cu_1st_evaluations],
            'Age_at_enrollment': [age_at_enrollment]
        }
        
        input_df = pd.DataFrame(input_dict)

        try:
            # Standarisasi data input
            scaled_input = scaler.transform(input_df)
            
            # Lakukan prediksi sungguhan!
            prediction = model.predict(scaled_input)[0]
            probabilities = model.predict_proba(scaled_input)[0]
            
            st.markdown("###AI Prediction Results")
            
            # Asumsi Kelas: 0 untuk Dropout, 1 untuk Enrolled/Graduate (Cek label encodermu jika berbeda)
            prob_class_0 = probabilities[0] * 100
            
            if prediction == 0:
                st.error("**PREDICTION: HIGH RISK OF DROPOUT**")
                st.metric("Model Confidence (Dropout Probability)", f"{prob_class_0:.1f}%")
                st.warning("Action: Schedule academic counseling to discuss performance and credit status.")
            else:
                st.success("**PREDICTION: STUDENT IS SAFE (GRADUATE / ENROLLED)**")
                # Jika prediksinya kelas 1 atau 2, ambil probabilitas kelas yang menang
                winning_prob = probabilities[prediction] * 100
                st.metric("Model Confidence (Safe Status)", f"{winning_prob:.1f}%")
                st.info("Action: Maintain academic performance in the upcoming semester.")
                
        except Exception as e:
            st.error(f"An technical error occurred in the model: {e}")