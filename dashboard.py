import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    return pd.read_csv("main.csv")

df = load_data()

# Sidebar
st.sidebar.image("c.png", width=320)
st.sidebar.title("Bike Sharing Dashboard")
visualization_choice = st.sidebar.selectbox("Select One", 
                                            ["Pola Penyewaan Sepeda Berdasarkan Cuaca", 
                                             "Korelasi Antara Kecepatan Angin dan Jumlah Penyewaan Sepeda",
                                             "Pola Perubahan Penyewaan Sepeda sepanjang Tahun 2011 dan 2012",
                                             "Perbedaan Pola Penyewaan Sepeda Antara Musim Panas dan Musim Dingin berdasarkan Jam Tertentu"])

# Visualizations
st.header("Bike Sharing Dashboard 🚲")

if visualization_choice == "Pola Penyewaan Sepeda Berdasarkan Cuaca":
    st.subheader("Pola Penyewaan Sepeda Berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='weathersit', y='cnt', data=df, ax=ax)
    plt.xlabel("Cuaca")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    st.write("Hasil diatas menunjukkan bahwa terdapat pola dalam penyewaan atau penggunaan sepeda berdasarkan kondisi cuaca. Cuaca yang lebih baik, seperti yang digambarkan oleh kategori cuaca 1, memiliki jumlah penyewaan sepeda yang lebih tinggi dan lebih konsisten dibandingkan dengan cuaca yang buruk, yang tercatat dalam kategori cuaca 3. Hal ini menunjukkan bahwa kebanyakan orang cenderung lebih memilih untuk menggunakan sepeda saat cuaca sedang baik daripada saat cuaca buruk.")

elif visualization_choice == "Korelasi Antara Kecepatan Angin dan Jumlah Penyewaan Sepeda":
    st.subheader("Hubungan Antara Kecepatan Angin dan Jumlah Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x='windspeed', y='cnt', data=df, ax=ax)
    plt.xlabel("Kecepatan Angin")
    plt.ylabel("Jumlah Penyewaan ")
    st.pyplot(fig)
    st.write("Tidak ditemukan korelasi yang signifikan antara kecepatan angin (windspeed) dengan jumlah penyewaan sepeda. Ini menunjukkan bahwa kecepatan angin mungkin bukan faktor yang signifikan dalam menentukan jumlah penyewaan sepeda.")

elif visualization_choice == "Pola Perubahan Penyewaan Sepeda sepanjang Tahun 2011 dan 2012":
    st.subheader("Penyewaan Sepeda Sepanjang Tahun 2011")
    df_2011 = df[df['yr'] == 0]  # Filter data for year 2011
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='mnth', y='cnt', data=df_2011, ci=None, ax=ax)
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

    st.subheader("Penyewaan Sepeda Sepanjang Tahun 2012")
    df_2012 = df[df['yr'] == 1]  # Filter data for year 2012
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='mnth', y='cnt', data=df_2012, ci=None, ax=ax)
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    st.write("Pola penyewaan sepeda pada tahun 2011 dan 2012 menunjukkan adanya tren yang serupa. Kedua tahun tersebut memiliki rata-rata tertinggi dalam jumlah penyewaan sepeda selama musim panas, yang biasanya berlangsung dari bulan Mei hingga September. Sebaliknya, jumlah penyewaan cenderung menurun selama musim dingin, terutama pada bulan-bulan antara November hingga Maret. Hal ini mencerminkan pola umum penggunaan sepeda yang dipengaruhi oleh perubahan musim, dengan kondisi cuaca yang lebih hangat di musim panas cenderung mendorong lebih banyak orang untuk menggunakan sepeda, sementara cuaca yang lebih dingin dan kondisi jalan yang kurang bersahabat selama musim dingin cenderung mengurangi jumlah penyewaan sepeda.")

elif visualization_choice == "Perbedaan Pola Penyewaan Sepeda Antara Musim Panas dan Musim Dingin berdasarkan Jam Tertentu":
    st.subheader("Pola Penyewaan Sepeda Antara Musim Panas dan Musim Dingin pada Jam Tertentu")
    summer_winter = df[(df['season'] == 2) | (df['season'] == 4)].groupby(['season', 'hr'])['cnt'].agg(['max', 'min', 'mean', 'median', 'std']).sort_values(by='mean', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5))
    palette = {2: 'orange', 4: 'blue'}  # Definisi warna untuk setiap musim
    sns.lineplot(x='hr', y='mean', data=summer_winter, hue='season', palette=palette, ax=ax)
    plt.xlabel('Jam')  # Keterangan sumbu x
    plt.ylabel('Rata-rata Penyewaan')  # Keterangan sumbu y
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=['Musim Panas', 'Musim Dingin'])  # Mengatur legenda
    st.pyplot(fig)
    st.write("Hasil menunjukkan bahwa terdapat jam-jam tertentu di mana penyewaan sepeda lebih tinggi pada musim panas dibandingkan dengan musim dingin. Misalnya, pada jam 17, rata-rata jumlah penyewaan sepeda pada musim panas lebih tinggi dibandingkan musim dingin. Hal ini menunjukkan bahwa faktor musim juga dapat mempengaruhi pola penyewaan sepeda pada jam-jam tertentu.")