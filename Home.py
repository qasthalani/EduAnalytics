import streamlit as st
import pandas as pd
import os

# ==========================================
# 0. KONFIGURASI HALAMAN (Harus Paling Atas)
# ==========================================
st.set_page_config(
    page_title="EduAnalytics",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 1. LOAD DATASET DENGAN CACHING
# ==========================================
@st.cache_data
def load_data():
    """
    Memuat dataset mahasiswa dari file CSV.
    Menggunakan @st.cache_data agar dataset tidak di-reload setiap kali user berinteraksi.
    """
    data_path = 'student-data-clean.csv'
    if not os.path.exists(data_path):
        # Fallback ke folder data/ atau dataset mentah jika dataset bersih tidak ditemukan
        data_path = 'data/student-data-clean.csv' if os.path.exists('data/student-data-clean.csv') else 'student-data.csv'
        
    df = pd.read_csv(data_path)
    return df

# ==========================================
# 2. MAIN FUNCTION
# ==========================================
def main():
    # Header Utama
    st.title("EduAnalytics")
    st.markdown("""
    Welcome to **EduAnalytics: Executive Dashboard & Prediction System**. 
    This application helps management and academic advisors monitor student performance and identify dropout risks.
    """)
    st.divider()

    # Memuat data
    df = load_data()

    # Perhitungan Metrik Dinamis
    total_students = len(df)
    dropout_count = (df['Status'] == 'Dropout').sum()
    dropout_rate = (dropout_count / total_students) * 100 if total_students > 0 else 0.0

    # Tampilkan KPI Cards
    st.subheader("Historical Key Performance Indicators (KPI)")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            label="Total Students", 
            value=f"{total_students:,}", 
            delta="Live Dataset"
        )

    with kpi2:
        st.metric(
            label="Historical Dropout Rate", 
            value=f"{dropout_rate:.1f}%", 
            delta=f"{dropout_count:,} Students",
            delta_color="normal"
        )

    with kpi3:
        # Akurasi model hasil evaluasi test-set
        st.metric(
            label="AI Model Accuracy", 
            value="76.3%", 
            delta="Random Forest Optimized"
        )

    # --- OUTDENT (Keluar dari blok 'with kpi3:') ---
    # Elemen di bawah ini sekarang berada di tingkat utama (Full Width / Tengah)
    st.divider()

    st.subheader("How to Use the Application")
    st.info("""
    Please refer to the menu in the **left sidebar**:
    - **Home:** This page, displaying a summary of metrics.
    - **Prediction:** Click this menu to access the Machine Learning prediction simulator. You can enter student metrics to view the probability of dropout.
    """)

if __name__ == "__main__":
    main()
