# Klasifikasi Jenis Restoran dengan Pohon Keputusan

## Gambaran Umum
Program ini merupakan implementasi dari algoritma Decision Tree yang digunakan untuk mengklasifikasikan jenis-jenis restoran berdasarkan beberapa atribut: rate (out of 5), num of rating, avg cost (two people), online_order, dan table booking.

## Detail Langkah-Langkah Kerja
1. **Membaca Data dari Excel**:
   Program membaca data restoran dari file Excel menggunakan pandas dan mengubahnya menjadi list of dictionaries (baris data).

2. **Pra-pemrosesan Data**:
   Mengonversi nilai atribut online_order dan table booking dari format teks ("Ya"/"Tidak") menjadi biner (1/0).

3. **Menghitung Gini Impurity**:
   Gini impurity digunakan untuk mengukur heterogenitas dari suatu node. Nilai impurity rendah berarti node lebih homogen. Fungsi gini_impurity menghitung impurity dari suatu kumpulan baris data.

4. **Membagi Dataset**:
   Fungsi split_dataset membagi dataset menjadi dua subset berdasarkan nilai atribut tertentu. Subset pertama berisi baris dengan nilai atribut >= nilai tertentu, dan subset kedua berisi baris dengan nilai atribut < nilai tersebut.

5. **Menemukan Pembagian Terbaik**:
   Fungsi find_best_split mencari atribut dan nilai terbaik yang memberikan pembagian dataset dengan gain tertinggi. Gain adalah pengurangan impurity dari pembagian dataset.

6. **Membangun Pohon Keputusan**:
   Fungsi build_tree membangun Decision Tree secara rekursif dengan memilih pembagian terbaik di setiap langkah. Node keputusan (DecisionNode) dibuat untuk setiap pembagian, dan node daun (Leaf) dibuat ketika tidak ada lagi gain yang bisa diperoleh.

7. **Klasifikasi**:
   Fungsi classify mengklasifikasikan sebuah baris data baru berdasarkan Decision Tree yang sudah dibangun. Jika node adalah daun, ia mengembalikan prediksi berdasarkan mayoritas jenis restoran di daun tersebut.

8. **Pengambilan Input dari Pengguna**:
   Fungsi get_user_input meminta pengguna memasukkan atribut restoran baru yang ingin diprediksi jenisnya.

9. **Prediksi**:
   Fungsi predict mengklasifikasikan input dari pengguna dengan menggunakan Decision Tree yang sudah dibangun dan mengembalikan jenis restoran yang diprediksi.

## Alasan Menggunakan Pendekatan Ini
- **Decision Tree**: Algoritma ini mudah dipahami dan diinterpretasikan. Ia bekerja baik pada data dengan banyak fitur kategorikal dan numerik. Selain itu, tidak memerlukan pra-pemrosesan data yang ekstensif.
- **Gini Impurity**: Digunakan sebagai metrik pemilihan terbaik karena mudah dihitung dan umum digunakan dalam pohon keputusan.
- **Rekursif**: Pendekatan rekursif memudahkan pembentukan pohon keputusan yang dapat terus membagi dataset hingga mendapatkan hasil yang optimal.

## Persyaratan
### Python:
- Instalasi Python versi 3.x
### Pandas:
- Digunakan untuk membaca dan memproses data dari file Excel.
  - Instalasi: `pip install pandas`
### OpenPyXL:
- Digunakan oleh pandas untuk membaca file Excel.
  - Instalasi: `pip install openpyxl`
### Program Python (Kode):
- Program ini membutuhkan akses ke file Excel yang berisi data restoran. Anda perlu memastikan file Excel berada di lokasi yang benar dan memiliki format kolom yang sesuai.
