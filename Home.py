import streamlit as st

# 1. Konfigurasi Halaman (Wajib di baris paling atas)
st.set_page_config(
    page_title="EduAnalytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Header & Penjelasan
    st.title("EduAnalytics: Student Dropout Prediction")
    st.markdown("""
    Welcome To **EduAnalytics: Executive Dashboard & Prediction System**. 
    This Application is designed to help campus management and academic advisors identify students who have a high risk of **Dropout (Leaving College)** as early as possible based on their academic history.
    """)
    st.divider()

    # Tampilan KPI Dummy (Bisa dihubungkan dengan data asli nantinya)
    st.subheader("Historical Key Performance Indicators (KPI)")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    with kpi1:
        st.metric(label="Total Students", value="4,424", delta="Data 2023")
    with kpi2:
        st.metric(label="Historical Dropout Rate", value="32.1%", delta="-1.2% from last year", delta_color="normal")
    with kpi3:
        st.metric(label="AI Model Accuracy", value="81.5%", delta="Random Forest Optimized")

    st.divider()

    # Panduan Penggunaan
    st.subheader("How to Use the Application")
    st.info("""
    Please refer to the menu in the **left sidebar**:
    - **Home:** This page, displaying a summary of metrics.
    - **Prediction:** Click this menu to access the Machine Learning prediction simulator. You can enter student metrics to view the probability of dropout.
    """)

if __name__ == "__main__":
    main()