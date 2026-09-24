import joblib
import pandas as pd
import streamlit as st

# Setup Halaman
st.set_page_config(page_title="Restaurant Tip Predictor", layout="centered")

st.title("🍽️ Smart Tip Predictor")
st.markdown(
    "Aplikasi prediksi estimasi tip pelayan restoran menggunakan siklus **CRISP-DM**."
)


# Load Model
@st.cache_resource
def load_model():
  return joblib.load("best_tip_model.pkl")


try:
  model = load_model()
except FileNotFoundError:
  st.error("File 'best_tip_model.pkl' tidak ditemukan. Jalankan notebook dulu!")
  st.stop()

# Form Input Data Tamu
st.subheader("Detail Reservasi & Meja")

col1, col2 = st.columns(2)
with col1:
  total_bill = st.number_input(
      "Total Tagihan ($)", min_value=1.0, max_value=200.0, value=25.0, step=0.5
  )
  size = st.slider(
      "Jumlah Orang (Size)", min_value=1, max_value=10, value=2, step=1
  )
  sex = st.selectbox("Jenis Kelamin Pembayar", ["Male", "Female"])

with col2:
  day = st.selectbox("Hari", ["Thur", "Fri", "Sat", "Sun"])
  time = st.selectbox("Waktu Makan", ["Lunch", "Dinner"])
  smoker = st.radio("Ada Area Merokok?", ["No", "Yes"], horizontal=True)

# Tombol Prediksi
if st.button("Hitung Estimasi Tip", type="primary"):
  # Buat fitur turunan sesuai tahap preparation di notebook
  bill_per_person = total_bill / size

  # Siapkan dataframe input
  input_data = pd.DataFrame([{
      "total_bill": total_bill,
      "sex": sex,
      "smoker": smoker,
      "day": day,
      "time": time,
      "size": size,
      "bill_per_person": bill_per_person,
  }])

  # Prediksi
  prediction = model.predict(input_data)[0]
  tip_percentage = (prediction / total_bill) * 100

  # Output Metrik
  st.markdown("---")
  st.subheader("Hasil Prediksi:")
  res_col1, res_col2 = st.columns(2)
  res_col1.metric(label="Estimasi Tip", value=f"${prediction:.2f}")
  res_col2.metric(label="Persentase Tip", value=f"{tip_percentage:.1f}%")

  if tip_percentage >= 15:
    st.success("Prediksi tip di atas rata-rata industri restoran (15%+).")
  else:
    st.info("Prediksi tip berada di kisaran standar normal.")