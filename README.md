Nama: Ridya Azizah Khayyira Mumtaz
NPM: 2306245895
Kelas: A


## 1. Cara saya mengimplementasikan checklist secara step-by-step 
1) Membuat sebuah proyek Django baru
- Membuat direktori lokal baru dengan nama "breezy" untuk menyimpan proyek Git
- Mengonfigurasi awal Git dengan menginisiasi repositori baru yang akan membuat repositori Git kosong di dalam direktori lokal dengan perintah git init, git config user.name <user_name>, dan git config user.email <user_email>
- Membuat repositori github baru yang bernama "breezy"
- Membuat branch utama main, dan menghubungkan repositori lokal dengan repositori GitHub dengan perintah git branch -M main, git remote add origin https://github.com/ridyaazizahkm/breezy.git, dan git push -u origin main
- Menjalankan danm engaktifkan virtual environment melalui command prompt dengan perintah python -m venv env dan env\Scripts\activate agar dapat mengelola dependensi proyek secara terpisah dan memastikan konsistensi lingkungan pengembangan
- Membuat berkas requirements.txt untuk menambahkan dependencies yang kemudian diinstall dengan perintah pip install -r requirements.txt, dan membuat proyek Django bernama breezy
- Mendaftarkan local host sebagai host yang diizinkan untuk mengakses aplikasi web pada file settings.py di bagian ALLOWED_HOST
- Membuat file .gitignore untuk menentukan berkas dan direktori yang harus diabaikan oleh Git
- Lakukan add, commit, push dari direktori repositori lokal

2) Membuat aplikasi dengan nama main pada proyek tersebut
- Membuat app main pada direktori proyek breezy dengan perintah python manage.py startapp main
- Tambahkan 'main' ke INSTALLED_APPS di dalam file settings.py
- Membuat dan mengisi berkas main.html pada direktori baru yaitu templates, yang berisi nama aplikasi, nama, dan kelas

3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Mengonfigurasi routing URL proyek melalui urls.py "from django.urls import path, include" dan pada variable urlpatters tambahkan path('', include('main.urls')).
- Jalankan proyek Django dengan perintah python manage.py runserver dan buka http://localhost:8000/ untuk melihat halaman yang sudah dibuat

4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name
price
description
- Mengubah berkas models.py yang berada dalam aplikasi main, mengisi dengan atribut yang diperlukan. Di sini, saya menggunakan 9 atribut.
- Membuat dan mengaplikasikan migrasi model ke dalam basis data lokal, untuk melacak perubahan pada model basis data

5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
- Menghubungkan views dengan templates, dengan menambahkan fungsi show_main dengan isi nama dan kelas
- Memodifikasi template pada main.html dengan mengubah struktur kode Django untuk menampilkan data, yaitu mengganti sintaks Django yaitu {{ nama }} dan {{ kelas }}

6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- Membuat berkas urls.py di direktori main untuk mengatur rute URL yang terkait dengan aplikasi main menggunakan fungsi show_main sebagai tampilan yang akan ditampilkan ketika URL terkait diakses

7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Dalam command prompt, lakukan push untuk update repositori github yang berisi kode terbaru, dengan perintah git add ., git commit -m "pesan commit", dan git push -u origin main
- Untuk deploy ke PWS, akses halaman PWS, login, dan create new project yang bernama breezy 
- Pada settings.py proyek Django, tambahkan ALLOWED_HOST dengan URL deployment PWS "ridya-azizah-breezy.pbp.cs.ui.ac.id"
- Jalankan perintah yang ada pada informasi project command

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/ridyaazizahkm/breezy/blob/main/RidyaAzizah_bagantugas2pbp.jpg)
Client mengirim permintaan ke internet yang kemudian dialihkan ke Python/Django, lalu dialihkan ke urls.py untuk menentukan routing, yang selanjutnya diteruskan ke views.py untuk mengolah URL. Di sini, views.py melakukan operasi baca/tulis data dari dan ke models.py serta basis data. Setelah itu, data tersebut diintegrasikan ke dalam templates untuk menyiapkan file HTML, yang selanjutnya dikembalikan ke internet dan akhirnya ditampilkan pada perangkat client.

## 3. Fungsi git dalam pengembangan perangkat lunak
1. Efektif untuk kolaborasi tim dalam mengembangkan proyek yang sama tanpa mengganggu pekerjaan orang lain, dengan menerapkan branch terpisah, dan menggabungkannya kembali ke dalam branch utama dengan merge setelah proyek selesai
2. Memungkinkan pengembang untuk melacak dan mengelola perubahan pada kode sumber yang disimpan dalam git dengan commit untuk mencatat perubahannya. Ini dapat terlihat siapa yang membuat perubahan tertentu dan kapan perubahan dibuat
3. Memungkinkan tim pengembang untuk memelihara berbagai versi dari sebuah produk, yang berguna untuk mengelola rilis produk yang berbeda dan juga eksperimen fitur baru tanpa mengganggu basis kode utama
4. Pengembang dapat memiliki salinan lengkap dari repository termasuk sejarahnya, memungkinkan pengembangan berlanjut walaupun tidak terhubung ke server pusat

## 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
1. Struktur dari Django terorganisir, dengan mengikuti pola Model-View-Template yang memberikan struktur jelas untuk aplikasi web. Hal ini membantu pemula untuk memahami bagaimana data dihandle, halaman web disajikan, dan logika aplikasi diatur.
2. Django memiliki dokumentasi yang luas yang membuat framework ini merupakan framework open source terbaik, sehingga pemula dapat lebih mudah untuk mempelajari framework ini karena panduannya yang terperinci
3. Fitur-fitur pada Django sangat banyak dan beragam, membantu pengembang untuk membangun aplikasi web yang aman dan berfitur lengkap dengan lebih cepat.

## 5. Mengapa model pada Django disebut sebagai ORM?
ORM (Object-Relational Mapping) adalah teknik pemrograman yang digunakan untuk mengonversi data antara sistem basis data dan objek pemrograman. Model pada Django dianggap sebagai ORM karena ia menyediakan lapisan abstraksi yang memungkinkan pengembang untuk berinteraksi dengan database melalui objek Python tanpa harus menulis query SQL secara langsung. Django juga bekerja dengan berbagai jenis sistem database seperti MySQL, PostgreSQL, dll. tanpa perlu mengubah kode aplikasi secara substansial. Django juga dilengkapi dengan sistem migrasi yang memudahkan pengembangan dan perubahan skema database seiring dengan berjalannya waktu.