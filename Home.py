import streamlit as st
import pandas as pd
import os

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
        # Fallback ke dataset mentah jika dataset bersih tidak ditemukan
        data_path = 'student-data.csv'
        
    df = pd.read_csv(data_path)
    return df

# Memuat data
df = load_data()

# ==========================================
# 2. PERHITUNGAN METRIK SECARA DINAMIS
# ==========================================
# Total Mahasiswa
total_students = len(df)

# Hitung Mahasiswa Dropout & Persentasenya
dropout_count = (df['Status'] == 'Dropout').sum()
dropout_rate = (dropout_count / total_students) * 100 if total_students > 0 else 0.0

# ==========================================
# 3. TAMPILKAN KPI CARDS
# ==========================================
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
    # Akurasi model adalah nilai konstan hasil evaluasi test-set saat training ML
    st.metric(
        label="AI Model Accuracy", 
        value="76.3%%", 
        delta="Random Forest Optimized"
    )

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
