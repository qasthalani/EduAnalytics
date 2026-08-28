# Proyek Akhir Data Science: Prediksi Mahasiswa Dropout - Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu perguruan tinggi yang berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berkualitas. Meskipun demikian, institusi ini menghadapi masalah serius terkait tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikannya (*dropout*). Tingginya angka *dropout* ini berdampak negatif pada reputasi institusi, kerugian finansial, serta efisiensi alokasi sumber daya akademis.

### Permasalahan Bisnis (Problem Statements)
1. Berapa persentase dan bagaimana karakteristik mahasiswa yang mengalami *dropout* di Jaya Jaya Institut?
2. Faktor-faktor utama (*key drivers*) apa saja yang paling memicu terjadinya keputusan mahasiswa untuk *dropout*?
3. Bagaimana membangun sistem peringatan dini (*early warning system*) berbasis Machine Learning yang dapat memprediksi risiko *dropout* mahasiswa secara presisi?
4. Langkah strategis dan *action items* apa saja yang dapat diterapkan oleh manajemen Jaya Jaya Institut untuk menekan angka *dropout*?

### Tujuan Proyek (Goals)
1. Mengidentifikasi pola dan tren historis mahasiswa *dropout* melalui eksplorasi data (*EDA*) dan dashboard interaktif.
2. Membangun model klasifikasi Machine Learning dengan akurasi optimal untuk mendeteksi risiko *dropout* sedini mungkin (sebelum semester 2 berakhir).
3. Menyediakan aplikasi simulator prediksi berbasis web (*Streamlit*) yang siap digunakan oleh dosen pembimbing dan pihak manajemen kampus.
4. Memberikan rekomendasi intervensi akademis dan operasional yang berbasis data (*data-driven recommendations*).

---

## Data Understanding

Dataset yang digunakan berisi 4.424 data mahasiswa dengan 38 fitur yang mencakup informasi demografi, kualifikasi masuk, status finansial, serta performa akademis semester 1 dan semester 2.

### Ringkasan Variabel Utama
* **Status (Target):** Kategori kelulusan mahasiswa (`Dropout`, `Graduate`, `Enrolled`).
* **Curricular_units_1st_sem_approved & 2nd_sem_approved:** Jumlah SKS/unit mata kuliah yang lulus di semester 1 dan 2.
* **Curricular_units_1st_sem_grade & 2nd_sem_grade:** Rata-rata nilai akademis semester 1 dan 2.
* **Tuition_fees_up_to_date & Debtor:** Status pembayaran UKT/SPP dan status tunggakan finansial.
* **Scholarship_holder:** Status penerima beasiswa.
* **Age_at_enrollment & Admission_grade:** Usia saat mendaftar dan nilai ujian masuk.

### Temuan Utama Eksplorasi Data (EDA)
* **Distribusi Target:** Dari total 4.424 mahasiswa, sebanyak **1.421 mahasiswa (32.1%) mengalami *Dropout***, 2.209 mahasiswa (49.9%) berhasil *Graduate*, dan 794 mahasiswa (18.0%) masih *Enrolled*.
* **Pengaruh Performa Semester Awal:** Mahasiswa yang meluluskan SKS $< 3$ unit pada Semester 1 & 2 memiliki probabilitas *dropout* melebihi **75%**.
* **Faktor Finansial:** Mahasiswa dengan status menunggak UKT (*Debtor = 1* atau *Tuition fees not up to date*) menunjukkan tingkat *dropout* signifikan lebih tinggi dibandingkan penerima beasiswa.

---

## Data Preparation

Tahapan pemrosesan data yang dilakukan meliputi:
1. **Data Cleaning:** Penanganan tipe data, pembersihan nilai yang tidak konsisten, serta pemeriksaan *missing values*.
2. **Feature Engineering:** 
   * Pembentukan fitur `Risk_Level` berbasis kombinasi performa akademis dan status tunggakan finansial.
   * Seleksi 10 fitur utama (*Top 10 Important Features*) paling relevan untuk menyederhanakan input pengguna tanpa mengorbankan akurasi model.
3. **Feature Scaling:** Menggunakan `StandardScaler` dari `scikit-learn` untuk menormalisasi skala variabel kontinu seperti nilai ujian masuk dan rata-rata IPK semester.

---

## Modeling & Evaluation

Model prediksi dikembangkan menggunakan algoritma **Random Forest Classifier** yang dioptimasi untuk menangani dataset multi-fitur.

### Evaluasi Model
* **Akurasi Model:** **76.27%** pada data pengujian (*test set*).
* **Fokus Metrik:** Optimasi *Recall* pada kelas *Dropout* (Kelas 0) untuk meminimalkan *False Negative* (mencegah mahasiswa berisiko tinggi lolos dari pemantauan).

---

## Dashboard Monitoring & Business Intelligence

Untuk membantu pihak manajemen Jaya Jaya Institut memantau performa mahasiswa secara real-time, telah dibangun dashboard interaktif.

* **Link Dashboard:** [https://public.tableau.com/views/StudentDropoutDashboard_17879055073590/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]
* **Komponen Utama Dashboard:**
  * **KPI Cards:** Total Student (4.424), Dropout Count (1.421 / 32.1%), Graduate Rate (61%), Average GPA (2.16), Overdue Tuition Fee (528 students).
  * **Semester Performance Analysis:** Trend kelulusan SKS vs Rata-rata nilai Semester 1 & 2.
  * **Demographics & Scholarship Breakdown:** Distribusi status penerima beasiswa dan jenis kelamin.
  * **Student Risk List Table:** Daftar mahasiswa berisiko tinggi beserta status pembayaran UKT.

---

## Prototype Machine Learning (Streamlit Web App)

Sistem prediksi telah diintegrasikan ke dalam aplikasi web berbasis Streamlit dan di-deploy ke cloud agar dapat diakses oleh civitas akademika Jaya Jaya Institut.

* **Link Aplikasi Streamlit Cloud:** [Isi dengan Link Streamlit Cloud Kamu di sini]
* **Cara Menjalankan Secara Lokal:**
  1. *Clone* repositori ini: `git clone <URL_REPOSITORI_GITHUB>`
  2. Masuk ke direktori proyek: `cd student-dropout-project`
  3. Install seluruh *dependencies*: `pip install -r requirements.txt`
  4. Jalankan aplikasi Streamlit: `streamlit run student-dropout-app.py`

---

## Conclusion

1. Masalah *dropout* di Jaya Jaya Institut berada pada angka yang tergolong tinggi (**32.1%**), dengan pemicu utama kegagalan meluluskan SKS pada dua semester pertama dan kendala pembayaran UKT.
2. Model Machine Learning *Random Forest* berhasil memprediksi potensi *dropout* dengan akurasi **76.27%** berbasis 10 indikator utama.
3. Integrasi Dashboard BI dan Simulator Streamlit memberikan visibilitas penuh bagi dosen pembimbing untuk melakukan intervensi proaktif sebelum mahasiswa mengambil keputusan berhenti kuliah.

---

## Action Items (Rekomendasi Strategis untuk Jaya Jaya Institut)

1. **Penerapan Early Warning System (Sistem Peringatan Dini):**
   * Mewajibkan dosen wali/pembimbing akademis menggunakan simulator prediksi Streamlit setiap akhir Semester 1 untuk mengidentifikasi mahasiswa dengan status *High Risk*.
2. **Program Pendampingan & Mentoring Akademis Khusus:**
   * Membentuk program *Peer Tutoring* (tutor sebaya) dan klinik akademik bagi mahasiswa yang mengumpulkan SKS lulus $< 4$ unit di Semester 1.
3. **Skema Bantuan Finansial & Cicilan UKT Fleksibel:**
   * Menyediakan opsi perpanjangan waktu atau cicilan pembayaran UKT bagi mahasiswa berstatus *Debtor* sebelum memasuki masa pendaftaran ulang semester baru, guna mencegah *dropout* yang disebabkan alasan ekonomi.
4. **Monitoring Beasiswa Tepat Sasaran:**
   * Melakukan evaluasi berkala terhadap penerima beasiswa agar dapat mempertahankan Indeks Prestasi Kumulatif (IPK) dan tidak kehilangan hak beasiswa di semester berikutnya.
