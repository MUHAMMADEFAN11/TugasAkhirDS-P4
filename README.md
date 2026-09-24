# Restaurant Tip Prediction App (CRISP-DM)

Proyek ini merupakan implementasi Machine Learning end-to-end berbasis metodologi **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*) untuk memprediksi besaran tip restoran berdasarkan faktor tagihan, demografi pengunjung, waktu kunjungan, dan ukuran rombongan.

## 📊 Sumber Dataset

Dataset yang digunakan dalam proyek ini adalah **Tips Dataset**, salah satu dataset klasik dalam analisis data dan statistika bisnis.

* **Sumber Asal / Sitasi:** 
  > Bryant, P. G., & Smith, M. (1995). *Practical Data Analysis: Case Studies in Business Statistics*. Homewood, IL: Richard D. Irwin Publishing.
* **Penyedia / Repositori:** Pustaka visualisasi data Python [Seaborn Data Repository](https://github.com/mwaskom/seaborn-data).
* **URL File Langsung:** [tips.csv (GitHub Raw)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)
* **Konteks Data:** Dicatat oleh seorang pelayan restoran selama beberapa bulan kerja. Berisi 244 baris data transaksi yang mencakup total tagihan (`total_bill`), jumlah tip (`tip`), jenis kelamin pembayar (`sex`), status area merokok (`smoker`), hari (`day`), waktu makan (`time`), dan jumlah tamu (`size`).

Aplikasi ini dibangun menggunakan **Streamlit** dan siap dijalankan secara lokal maupun di-deploy ke cloud (seperti Streamlit Community Cloud).

---

## 📌 Metodologi CRISP-DM

1. **Business Understanding**: Mengidentifikasi variabel yang paling memengaruhi pemberian tip dan membantu pengelola restoran memperkirakan tip rata-rata staf pelayanan.
2. **Data Understanding**: Eksplorasi dataset restoran (*Tips dataset*) mencakup total tagihan (`total_bill`), tip (`tip`), jenis kelamin (`sex`), status merokok (`smoker`), hari (`day`), waktu makan (`time`), dan jumlah tamu (`size`).
3. **Data Preparation**: Preprocessing data, encoding fitur kategorikal, standarisasi fitur numerik, serta pemisahan data train-test.
4. **Modeling**: Pelatihan beberapa algoritma regresi (Linear Regression, Random Forest Regressor, Gradient Boosting) untuk menemukan performa terbaik.
5. **Evaluation**: Evaluasi model menggunakan metrik regresi seperti MAE (*Mean Absolute Error*), RMSE (*Root Mean Squared Error*), dan $R^2$ Score. Model terbaik diekspor ke format serialisasi (`best_tip_model.pkl`).
6. **Deployment**: Pembuatan antarmuka web interaktif menggunakan Streamlit (`app.py`).

---

## 📂 Struktur File Repositori

```text
├── p4-projek.ipynb  # Notebook eksplorasi data, preprocessing, & training model
├── best_tip_model.pkl          # Model terlatih terbaik yang siap digunakan untuk inferensi
├── app.py                      # Aplikasi dashboard interaktif berbasis Streamlit
├── requirements.txt            # Daftar pustaka / dependensi Python
└── README.md                   # Dokumentasi proyek
```

---

## Panduan Menjalankan Aplikasi di Lokal

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di PC Masing - masing:

### 1. Clone Repositori
```bash
git clone https://github.com/MUHAMMADEFAN11/TugasAkhirDS-P4
cd TugasAkhirDS-P4
```

### 2. Buat & Aktifkan Virtual Environment (Disarankan)
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi Streamlit
```bash
streamlit run app.py
```

Setelah perintah dijalankan, browser Anda akan otomatis terbuka ke alamat `http://localhost:8501`.

---

## 🛠️ Tech & Library

* **Bahasa**: Python
* **Data Processing & Modeling**: Pandas, NumPy, Scikit-Learn
* **Visualisasi**: Matplotlib, Seaborn
* **Aplikasi Web**: Streamlit
* **Penyimpanan Model**: Pickle / Joblib

---
