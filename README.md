Nama: Ridya Azizah Khayyira Mumtaz
NPM: 2306245895
Kelas: A

Link deploy pws: http://ridya-azizah-breezy.pbp.cs.ui.ac.id
Link pws: https://pbp.cs.ui.ac.id/web/project/ridya.azizah/breezy

## :pushpin: TUGAS 2
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

## :pushpin: TUGAS 3

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah hal yang penting saat membuat sebuah platform, dan ada beberapa alasan kenapa hal ini harus diperhatikan. Pertama, soal aksesibilitas. Kita perlu memastikan data bisa diakses oleh siapa saja yang membutuhkan, termasuk sistem lain. Misalnya, di aplikasi e-commerce, data tentang produk harus selalu tersedia agar pengguna bisa melihat dan membeli produk dengan mudah. Lalu, ada juga soal konsistensi dan integritas data. Kita harus memastikan data tetap aman dan tidak rusak saat dikirimkan. Keamanan juga jadi faktor penting untuk melindungi data dari akses yang tidak sah selama proses pengiriman. Selain itu, data delivery juga penting untuk memastikan pengiriman data berjalan lancar dan aplikasi tetap responsif. Hal ini juga berkaitan dengan skalabilitas, karena platform harus siap menangani lebih banyak pengguna dan data seiring waktu. Terakhir, pengiriman data yang tepat waktu dan relevan sangat mempengaruhi pengalaman pengguna, membuat mereka lebih puas dan nyaman saat berinteraksi dengan platform.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik daripada XML. JSON juga lebih populer karena JSON memiliki beberapa kelebihan. JSON cenderung lebih ringkas dan mudah dibaca oleh manusia karena menggunakan key-value tanpa tag yang berlebihan. JSON juga lebih cepat saat parsing dibandingkan dengan XML karena struktur datanya lebih sederhana. Selain itu, JSON memiliki dukungan yang luas oleh banyak API dan layanan web, sehingga JSON menjadi pilihan bagi para web developer. Terakhir, JSON juga lebih mudah digunakan dan dipahami terutama bagi developer yang sudah familiar dengan JavaScript.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() berguna untuk mencegah input yang tidak valid atau berbahaya. Selain itu, is_valid() juga berguna untuk memastikan bahwa data yang disimpan di database adalah data yang benar dan sesuai dengan aturan yang ditentukan. Selain itu, is_valid() juga bermanfaat untuk memberikan umpan balik langsung kepada pengguna jika ada kesalahan dalam input mereka, sehingga bisa diperbaiki oleh pengguna sebelum data dikirim.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Form) adalah jenis serangan di mana penyerang mencoba membuat pengguna yang sudah terautentikasi melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka. csrf_token adalah mekanisme keamanan yang digunakan untuk melindungi aplikasi Django dari serangan ini. csrf_token berguna untuk mencegah serangan csrf dengan memastikan permintaan yang dikirim ke server berasal dari pengguna yang sah, bukan dari situs jahat. Selain itu, csrf_token juga bermanfaat dalam validasi permintaan. Server akan memeriksa token CSRF yang dikirim bersama permintaan POST untuk memastikan bahwa permintaan tersebut sah. Jika token tidak cocok atau tidak ada, permintaan akan ditolak.

Jika tidak menambahkan csrf_token, web akan menjadi rentan terhadap serangan CSRF. Penyerang dapat membuat pengguna yang sudah login melakukan tindakan yang tidak diinginkan, contohnya seperti mengubah kata sandi atau melakukan transaksi tanpa sepengetahuan pengguna. Data pengguna juga dapat terancam karena penyerang dapat memanfaatkan pengguna untuk melakukan tindakan berbahaya.

Penyerang dapat memanfaatkan ketiadaan csrf_token dengan beberapa cara. Penyerang dapat mengirim permintaan palsu dengan membuat halaman web yang mengirim permintaan POST ke aplikasi target menggunakan kredensial pengguna yang sudah login. Penyerang juga dapat memanfaatkan sesi pengguna untuk melakukan tindakan yang menguntungkan mereka dan mengambil alih akun, seperti mengubah informasi akun, dan lainnya.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial
1) Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Membuat direktori bernama templates di direktori utama dan membuat sebuah berkas HTML baru bernama base.html untuk menjadi template dasar yang bisa digunakan sebagai kerangka umum untuk halaman-halaman web lainnya dalam proyek
- Isi base.html dengan kode berikut
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Menambahkan ‘templates’ pada baris TEMPLATES di file settings.py yang terletak di dalam direktori proyek agar berkas base.html terdeteksi sebagai berkas template, seperti ini:   
```
'DIRS': [BASE_DIR / 'templates']
```
- Pada subdirektori templates yang ada di direktori main, ubah kode di dalam file main.html untuk menggunakan base.html sebagai template utama dengan menambahkan kode
```
{% extends 'base.html' %}
{% block content %}
…
{% endblock content %}
```
- Menghapus berkas basis data db.sqlite3
- Menambahkan kode import uuid di paling atas file models.py pada subdirektori main.
- Melakukan migrasi model dengan menjalankan 
```
python manage.py makemigrations
python manage.py migrate
```
- Membuat berkas baru pada direktori main bernama forms.py agar dapat menerima data product entry baru dengan menambahkan kode
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "ukuran", "aroma", "top_notes", "middle_notes", "base_notes"]
```
- Menambahkan beberapa import di paling atas file views.py yang ada di direktori main
```
from django.shortcuts import render, redirect 
from main.forms import ProductEntryForm
from main.models import ProductEntry
```
- Membuat fungsi baru di file yang sama bernama create_product_entry yang menerima parameter request dengan isi fungsi sebagai berikut
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)


    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')


    context = {'form': form}
    return render(request, "create_product_entry.html", context)
 ```
- Ubah fungsi show_main yang sudah ada di file views.py menjadi
```
def show_main(request):
    product_entries = Product.objects.all()


    context = {
        'nama' : 'Ridya Azizah Khayyira Mumtaz',
        'kelas' : 'PBP-A',
        'product_entries' : product_entries
    }


    return render(request, "main.html", context)
```
- Menambahkan import create_product_entry pada file urls.py yang terletak di direktori main
- menambahkan path URL ke dalam variabel urlpatterns di file yang sama dengan kode ini
```
 path('create-product-entry', create_product_entry, name='create_product_entry')
```
- Membuat file baru bernama create_product_entry.html pada direktori main/templates, lalu mengisinya dengan kode:
```
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
- Menambahkan kode pada file main.html di dalam {% block content %} untuk menampilkan data ke dalam bentuk tabel dan menambahkan tombol Add New Product Entry yang akan redirect ke form
```
{% if not product_entries %}
<p>Belum ada product pada breezy.</p>
{% else %}
<table>
  <tr>
    <th>Name</th>
    <th>Price</th>
    <th>Ukuran</th>
    <th>Aroma</th>
    <th>Top Notes</th>
    <th>Middle Notes</th>
    <th>Base Notes</th>
    <th>Description</th>
  </tr>


  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini
  {% endcomment %}
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.ukuran}}</td>
    <td>{{product_entry.aroma}}</td>
    <td>{{product_entry.top_notes}}</td>
    <td>{{product_entry.middle_notes}}</td>
    <td>{{product_entry.base_notes}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>

{% endblock content %}
```
- Menjalankan proyek Django dengan perintah python manage.py runserver dan buka  http://localhost:8000/ 
- Menambahkan beberapa data product dan lihat form data yang sudah ditambahkan pada halaman utama 

2) Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

- Menambahkan import HttpResponse dan Serializer di dalam file views.py
- Membuat 4 fungsi baru yang menerima parameter request dengan nama show_xml, show_json, show_xml_by_id, dan show_json_by_id. Kodenya seperti berikut
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
- Membuka file urls.py yang ada pada direktori main dan mengimpor 4 fungsi yang sudah dibuat
```
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
- Menambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor
```
    path('xml/', show_xml, name='show_xml'), # Kembalikan data dalam bentuk XML
    path('json/', show_json, name='show_json'), # Kembalikan data dalam bentuk JSON
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), # Kembalikan dalam bentuk XML berdasarkan ID
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), # Kembalikan dalam bentuk JSON berdasarkan ID
```
- Menjalankan python manage.py runserver dan membuka http://localhost:8000/xml/ untuk melihat hasil dalam bentuk XML, http://localhost:8000/json/  untuk melihat hasil dalam bentuk JSON, http://localhost:8000/xml/[id]/ untuk melihat hasil berdasarkan ID dalam bentuk XML, dan http://localhost:8000/json/[id]/ untuk  melihat hasil berdasarkan ID dalam bentuk JSON. [id] diganti dengan id dari suatu produk

## 6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- Menjalankan python manage.py runserver
- Download Postman, lalu membuat request baru dengan method GET kemudian masukkan http://localhost:8000/xml/ atau http://localhost:8000/json/. Klik tombol send
- Melihat hasil response untuk mengecek apakah data sudah terkirim dengan baik dengan format XML atau JSON
- Mengecek url http://localhost:8000/xml/[id]/ dan juga http://localhost:8000/json/[id]/ untuk melihat hasil berdasarkan ID dalam bentuk XML atau JSON. [id] diganti dengan id dari suatu produk. Berikut adalah hasil screenshot dari Postman
![](https://github.com/ridyaazizahkm/breezy/blob/main/RidyaAzizah_Tugas3%20XML.png)
![](https://github.com/ridyaazizahkm/breezy/blob/main/RidyaAzizah_Tugas3%20JSON.png)
![](https://github.com/ridyaazizahkm/breezy/blob/main/RidyaAzizah_Tugas3%20XML%20by%20ID.png)
![](https://github.com/ridyaazizahkm/breezy/blob/main/RidyaAzizah_Tugas3%20JSON%20by%20ID.png)

## :pushpin: TUGAS 4

## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Dalam Django, HttpResponseRedirect dan redirect digunakan untuk mengarahkan pengguna ke URL lain. Berikut ini perbedaannya.
a. HttpResponseRedirect()
- Subclass ini merupakan cara manual untuk mengirimkan respons HTTP dengan status kode 302 (Found) atau 301 (Moved Permanently), yang memberitahu browser untuk mengunjungi URL yang berbeda
- Memerlukan URL lengkap atau penggunaan fungsi reverse untuk mendapatkan URL dari nama view.

b. redirect()
- Merupakan fungsi shortcut yang lebih sederhana dan fleksibel untuk mengarahkan pengguna ke URL lain
- Lebih mudah digunakan karena dapat menerima berbagai jenis argumen, seperti URL, nama view, objek model

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
- Setiap produk yang dibuat oleh pengguna harus terhubung dengan pengguna tersebut. Hal ini dapat dilakukan dengan menggunakan konsep ForeignKey yang menciptakan relasi antara model Product dan User. ForeignKey berguna agar setiap produk dapat diketahui siapa pembuatnya
- Ketika pengguna membuat produk baru, web tidak hanya menyimpan informasi produk, tetapi juga menyimpan siapa pengguna yang membuat produk tersebut. Informasi pengguna ini diambil dari pengguna yang sedang login di dalam web. Hal ini dilakukan dengan memodifikasi kode pada file views.py, yaitu dengan menambahkan request.user
- Setelah produk terhubung dengan pengguna, web dapat menampilkan produk yang hanya dibuat oleh pegguna yang sedang login. Hal ini dilakukan dengan mengubah isi product_entries menjadi Product.objects.filter(user=request.user) serta menampilkan request.user.username di dalam context yang terletak di dalam fungsi show_main pada file views.py
- Setelah menambahkan field user pada model, lakukan proses migrasi model. Jika terdapat data entri lama, Django akan meminta untuk menetapkan pengguna default untuk entri lama tersebut. 
- Setelah model terhubung dengan pengguna, tambahkan import os dan menonaktifkan mode debug untuk aplikasi pada file settings.py


## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Perbedaan antara authentication dan authorization:
1. Authentication
- Proses untuk memverifikasi saat pengguna login, dengan mengecek identitas pengguna yang biasanya melibatkan pengecekan apakah kredensial pengguna (seperti username dan password) itu cocok dengan yang ada di sistem
- Untuk memastikan bahwa orang yang mengakses sistem adalah orang yang 'benar' atau yang sudah terdata pada sistem
- Implementasi pada Django: Ketika pengguna ingin login, DJango memverifikasi identitas mereka dengan menggunakan fungsi seperti authenticate() dan login(). Jika sukses, Django akan membuat session untuk pengguna tersebut 

2. Authorization
- Proses untuk menentukan hak dan izin yang dimiliki pengguna yang sudah terverifikasi. Setelah autentikassi berhasil, sistem akan menentukan apa saja yang boleh dilakukan oleh pengguna tersebut, seperti mengakses halaman tertentu, dan lainnya.
- Untuk mengontrol apa yang dapat dilakukan pengguna dan mengatur bagian sistem yang dapat mereka akses
- Implementasi pada Django: Dalam Django, kita bisa memanfaatkan login_required decorator untuk membatasi akses suatu halaman, contohnya di sini adalah membatasi akses halaman main. Saat pengguna mencoba untuk mengakses halaman yang dilindungi @login_required, Django memeriksa apakah pengguna sudah login. Jika sudah, pengguna diizinkan mengakses halaman tersebut. 

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan session yang disimpan dalam cookies. Saat pengguna berhasil login, Django akan membuat session untuk mereka dan menyimpan session ID dalam cookie di browser pengguna. Setiap pengguna mengirim request ke server (misalnya membuka halaman lain), cookie ini dikirim kembali ke server, memungkinkan Django untuk mengenali penggua tersebut dan mengingat bahwa mereka sudah login. 

Selain mengingat pengguna yang sudah login, kegunaan lain dari cookies adalah untuk menyimpan preferensi pengguna, contohnya seperti ukuran font yang disesuaikan, tema yang dipilih, dan lainnya. Selain itu, cookies juga dapat digunakan untuk melacak perilaku pengguna di situs web, seperti halaman yang dikunjungi atau durasi pengguna mengunjungi suatu halaman, dan informasi ini biasanya digunakan untuk analisis serta peningkatan pengalaman pengguna. Cookies juga dapat digunakan untuk personalisasi iklan berdasarkan informasi tentang preferensi dan perilaku pengguna.

Walaupun cookies memiliki banyak kegunaan, namun tidak semua cookies dianggap aman untuk digunakan. Cookies yang tidak diatur dengan benar atau menyimpan data sensitif dapat membuat aplikasi rentan terhadap serangan, seperti session hijacking atau cross-site scripting (XSS). Kemudian, cookies yang diatur oleh domain pihak ketiga (third-party cookies) yang biasanya digunakan untuk keperluan iklan, sering kali melacak aktivitas pengguna di berbagai situs web. Hal ini bisa menjadi masalah privasi karena pengguna tidak selalu menyadari bahwa mereka sedang dilacak oleh cookies.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1) Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
a. Membuat fungsi register
- Mengaktifkan virtual environment kemudian membuka views.py yang ada pada direktori main untuk menambahkan import UserCreationForm dan messages untuk memudahkan pembuatan form register
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
- Menambahkan fungsi register pada file views.py untuk membuat formulir registerasi secara otomatis
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- Membuat file register.html pada direktori main/templates yang berisi kode sebagai berikut
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
- Membuka urls.py yang ada pada subdirektori main lalu import fungsi register
```
from main.views import register
```
- Menambahkan path url ke urlpatterns 
```
path('register/', register, name='register'),
```

b. Membuat fungsi login
- Mengimport authenticate, login, dan AuthenticationForm pada views.py yang ada pada subdirektori main
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```
- Menambahkan fungsi login_user di dalam file views.py untuk mengautentikasi pengguna yang ingin login. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- Membuat file login.html pada direktori main/templates yang berisi kode sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
- Mengimpor fungsi login_user pada file urls.py yang terletak pada subdirektori main
```
from main.views import login_user
```

- Menambahkan path url login_user ke urlpatterns
```
path('login/', login_user, name='login'),
```
c. Membuat fungsi logout
- Mengimport logout pada views.py yang ada pada subdirektori main
- Menambahkan fungsi login_user di dalam file views.py untuk melakukan logout, kemudian mengarahkan pengguna ke halaman login
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- Menambahkan tombol logout pada berkas main.html yang ada pada direktori main/templates, setelah hyperlink tag untuk Add New Product Entry
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
- Mengimport fungsi logout_user di urls.py yang ada pada subdirektori main
```
from main.views import logout_user
```
- Menambahkan path logout_user ke urlpatterns
```
path('logout/', logout_user, name='logout'),
```

2) Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

- Menjalankan proyek Django dengan perintah `python manage.py runserver` dan buka http://localhost:8000/
- Melakukan registrasi untuk dua akun dengan nama 'salwa' dan 'bernanda', lalu saya membuat password untuk akun tersebut.
- Melakukan login untuk masing-masing akun dan saya membuat masing-masing tiga produk berbeda untuk dua user tersebut

3) Menghubungkan model Product dengan User.
- Mengimport model pada models.py yang terletak pada subdirektori main 
```
from django.contrib.auth.models import User
```
- Menambahkan kode user untuk menghubungkan satu product entry dengan satu user pada model Product menggunakan ForeignKey
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
- Mengubah kode pada fungsi create_product_entry pada file views.py yang terletak pada subdirektori main
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
- Mengubah value product_entries dan mengganti context di bagian nama untuk menampilkan nama user yang sedang login
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'nama' : request.user.username,
```
- Menyimpan semua perubahan dengan melakukan `python manage.py makemigrations`
- Saat muncul error untuk melakukan migrate, pilih 1 untuk menetapkan default value untuk field user pada semua row yang sudah dibuat pada database
- Ketik angka 1 untuk menetapkan user dengan ID 1
- Melakukan `python manage.py migrate` untuk mengaplikasikan migrasi
- Menambahkan `import os` pada file settings.py yang terletak pada subdirektori breezy, dan mengganti variabel DEBUG seperti kode ini
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
- Menjalankan proyek Django dengan `python manage.py runserver` lalu membuka http://localhost:8000/ 

4) Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
- Melakukan logout, dan menambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas file views.py yang terletak pada subdirektori main
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- Menambah 'last_login' pada fungsi login_user 
``` 
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
```
- Menambahkan `'last_login': request.COOKIES['last_login']` pada fungsi show_main ke dalam variabel context
- Mengubah isi fungsi logout_user 
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- Menambahkan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` untuk menampilkan data last login di dalam file main.html
- Merefresh halaman login, kemudian login dan data login akan muncul di halaman main

5) Melakukan add-commit-push ke GitHub.
- Melakukan add commit push ke GitHub dengan perintah berikut
git add .
git commit -m "isi commit"
git push -u origin main

## :pushpin: TUGAS 5
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika ada properti CSS yang saling menimpa satu sama lain, selector yang paling spesifik akan memiliki prioritas tertinggi dan  diterapkan. Aturan ke-spesifik-an CSS dihitung menggunakan formula 4 digit. Berikut ini urutannya berdasarkan prioritas terendah hingga tertinggi:
- Element/Tag selector
Contoh: p, div
Nilai: 0,0,0,1
- Class, Attribute, Pseudo-class selector
Contoh: .kelas, [type="text"], :hover
Nilai: 0,0,1,0
- ID Selector
Contoh: #id
Nilai: 0,1,0,0
- Inline Selector (langsung pada elemen)
Contoh: `<div style="color: red;">`
Nilai: 1,0,0,0
- Aturan dengan !important
Aturan yang ditandai !important akan mengesampingkan aturan lainnya, sehingga ini merupakan prioritas tertinggi

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
- Pengalaman pengguna yang konsisten
Dengan responsive design, situs web dapat berfungsi dengan baik serta dapat menyesuaikan tampilannya sesuai dengan ukuran layar perangkat yang digunakan, seperti desktop, tablet, atau smartphone.
- Navigasi yang mudah
Responsive design akan memudahkan pengguna untuk menavigasi situs web tanpa harus memperbesar dan memperkecil layar secara manual
- Peningkatan Search Engine Optimization
Dengan responsive design, situs web akan lebih mudah dicari dan ditemukan dalam situs pencarian seperti Google, karena Google 
Google lebih menyukai situs yang responsif agar memberikan pengalaman pengguna yang lebih baik.
- Meningkatkan jangkauan pasar
Dengan responsive design, situs web akan menjangkau audiens yang lebih luas karena dapat diakses dengan berbagai jenis perangkat
- Efisiensi pengembangan dan pemeliharaan
Dengan responsive design, web developer tidak perlu mengembangkan dan memelihara versi terpisah untuk versi desktop dan mobile, karena responsive design hanya menggunakan satu basis kode untuk semua perangkat

Contoh aplikasi yang sudah menerapkan responsive design:
- Netflix
- Twitter
- Linkedin
- Facebook
- Youtube

Contoh aplikasi yang belum menerapkan responsive design:
- Situs web pemerintah atau lembaga publik yang belum diupdate
- Situs web perusahaan tradisional
- Situs blog pribadi yang sudah lama

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah ruang di luar border elemen yang memisahkan elemen tersebut dengan elemen lainnya, fungsinya untuk mengatur jarak antar elemen serta memberikan ruang kosong di sekitar elemen

- Border adalah garis di sekitar padding dan konten elemen yang dapat diatur ketebalan, gaya, dan warnanya. Fungsinya untuk menyediakan batas visual di sekitar elemen

- Padding adalah ruang di dalam border, yaitu di antara konten elemen dan bordernya. Fungsinya untuk memberikan jarak agar konten tidak terlalu dekat dengan border

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox
Definisi: Modul untuk mengatur tata letak elemen di dalam satu dimensi, seperti di dalam satu baris atau kolom
Kegunaan: Menyusun tombol, menu, dan lainnya agar responsif dan mudah diatur dengan jarak yang diatur secara dinamis sesuai ukuran layar
- Grid Layout
Definisi: Modul untuk mengatur tata letak elemen dalam dua dimensi, baik baris maupun kolom secara bersamaan. 
Kegunaan: Mendukung pembuatan elemen lebih banyak, dan dapat mengatur tata letak yang lebih kompleks seperti situs web dengan header, footer, sidebar, dan konten

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Sebelum memulai, saya menambahkan Tailwind terlebih dahulu ke aplikasi
- Menambahkan tag `<meta name="viewport">` di dalam file base.html yang terletak di direktori templates
- Menambahkan script cdn tailwind di bagian head file base.html
```
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```
1) Implementasikan fungsi untuk menghapus dan mengedit product.

- Membuat fungsi delete_product yang menerima parameter request dan id di dalam file views.py untuk menghapus data product
```
def delete_product(request, id):
    # Get mood berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Import fungsi delete_product dan menambahkan path url untuk mengakses delete_product pada file urls.py
- Membuat fungsi edit_product yang menerima parameter request dan id di dalam file views.py untuk mengedit data product
```
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
- Menambahkan import pada file views.py yaitu `from django.shortcuts import .., reverse` dan `from django.http import .., HttpResponseRedirect`
- Membuat file edit_product.html pada subdirektori main/templates, yang berfungsi untuk mengedit product
- Import fungsi edit_product dan menambahkan path url untuk mengakses edit_product pada file urls.py
- Membuka main.html pada subdirektori main/templates lalu menambahkan kode agar button edit ada pada setiap tabel yang letaknya sejajar dengan elemen `<td>` terakhir 

2) Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
- Pertama saat membuat halaman login pada login.html, buat kontainer utama dengan shadow untuk log in, dan menambahkan logo "Breezy!" 
- Mengubah style input untuk isian username dan password
- Mengatur message jika sukses ataupun error saat login
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-[#B7C4CF] py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div class="rounded-3xl bg-[#EEEDEB] shadow-2xl p-9">
      <div class="text-center">

        <h1 class="text-5xl font-extrabold" style="color: #967E76;">Breezy!</h1>
        <h2 class="mt-2 text-xl font-semibold" style="color: #747264" >
          Login to your account
        </h2>
      </div>

      <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        
        <div class="rounded-lg shadow-sm mb-4">
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Username">
        </div>

        <div class="rounded-lg shadow-sm mb-4">
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Password">
        </div>

        <div>
          <button type="submit" 
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-lg text-white hover:bg-opacity-70 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" 
            style="background-color: #967E76;">
          Sign in
      </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
              <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% elif message.tags == "error" %}
              <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% else %}
              <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% endif %}
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" 
            class="font-medium hover:text-indigo-300" 
            style="color: #747264;">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```
- Selanjutnya untuk registrasi yang diatur pada register.html, tampilkan form register yang berisi username, password, password comfirmation
- Mengubah style warna button dan juga warna text
- Menampilkan pesan error jika password confirmation tidak sesuai dengan password, dengan code {% if field.errors%}
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-[#B7C4CF] py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-4xl font-extrabold text-[#3C3633]">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#967E76] hover:bg-[#967E76] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-[#747264] hover:text-[#747264]">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
- Selanjutnya untuk menambah product yang diatur pada file create_product.html 
- Menampilkan form untuk mengisi product baru
- Mengubah style warna button dan juga warna text 
```
{% extends 'base.html' %}
{% load static %}
{% include 'navbar.html' %}

{% block meta %}
<title>Create Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-[#3C3633]">Create Product Entry</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-[#967E76] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#967E76] transition duration-300 ease-in-out w-full">
            Create Product Entry
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

3) Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
- Mendownload foto berformat png dengan nama sedih-banget.png, dan diletakkan pada direktori static/image
- Meletakkan image sedih-banget.png pada file main.html jika belum ada produk, yaitu di dalam {% if not product_entries %}
```
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">Belum ada data product pada Breezy.</p>
    </div>
```

4) Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card
- Menampilkan nama dan kelas melalui card_info.html
```
<div class="bg-[#967E76] rounded-xl overflow-hidden shadow-lg"> <!-- Added shadow-lg for a larger shadow effect -->
    <div class="p-4 animate-shine">
      <h5 class="text-lg font-bold text-white">{{ title }}</h5>
      <p class="text-white font-semibold">{{ value }}</p>
    </div>
</div>
```
- Menampilkan daftar product melalui file card_product.html
- Melakukan styling warna dan membagi info produk menjadi nama & harga, details, dan notes
```
<div class="relative break-inside-avoid">
    <div class="relative top-5 bg-[#EEEDEB] shadow-xl rounded-t-lg rounded-b-xl mb-6 break-inside-avoid flex flex-col transform rotate-1 hover:rotate-0 transition-transform duration-300">
        <div class="bg-[#b2c4d4] text-white p-4 rounded-t-xl">
            <h3 class="font-bold text-2xl mb-2 text-white">{{ product_entry.name }}</h3>
            <p class="text-white">
                IDR <span class="border-b-2 border-[#EEE3CB] text-white">{{ product_entry.price }}</span>
            </p>
        </div>
        <p class="p-4 text-[#3C3633]">{{ product_entry.description }}</p>
        <div class="p-4">
            <p class="font-semibold text-lg mb-1 text-[#3C3633]">Details</p>
            <p class="text-[#3C3633] mb-1">Aroma: {{ product_entry.aroma }}</p>
            <p class="text-[#3C3633] mb-1">Ukuran: {{ product_entry.ukuran }}</p>
        </div>
        <div class="p-4">
            <p class="font-semibold text-lg mb-1 text-[#3C3633]">Notes</p>
            <p class="text-[#3C3633] mb-1">Top: {{ product_entry.top_notes }}</p>
            <p class="text-[#3C3633] mb-1">Middle: {{ product_entry.middle_notes }}</p>
            <p class="text-[#3C3633] mb-1">Base: {{ product_entry.base_notes }}</p>
        </div>
        <div class="flex p-4">
            <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-[#C7C8CC] hover:bg-[#C7C8CC] text-black font-bold flex-1 text-center py-2 mx-1 rounded">
                Edit
            </a>
            <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-[#C96868] hover:bg-[#B05555] text-white font-bold flex-1 text-center py-2 mx-1 rounded">
                Delete
            </a>
        </div>
    </div>
</div>
```

5) Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
- Memodifikasi tombol edit dan delete pada setiap card yang terletak di bagian bawah card, diatur pada file card_product.html. Tombol tersebut akan mengarahkan ke masing-masing halaman edit dan delete
```
<a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-[#C7C8CC] hover:bg-[#C7C8CC] text-black font-bold flex-1 text-center py-2 mx-1 rounded">
    Edit
</a>
```
```
<a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-[#C96868] hover:bg-[#B05555] text-white font-bold flex-1 text-center py-2 mx-1 rounded">
    Delete
</a>
```
- Tombol edit ditandai dengan "Edit" di sebelah kiri, dan tombol delete ditandai dengan "Delete" di sebelah kanan

6) Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- Meletakkan tautan navigasi (Home, Products, Categories, Cart) di kanan dalam elemen `<ul>`
- Menggunakan class hidden md:flex untuk menampilkan tautan hanya di layar medium ke atas
- Menggunakan class md:hidden untuk menampilkan tombol hamburger pada layar kecil
- Menambahkan ikon SVG tiga garis sebagai tombol hamburger
- Membuat menu mobile yang tersembunyi dengan class mobile-menu hidden md:hidden
- Menambahkan script untuk toggle class hidden ketika tombol hamburger ditekan, sehingga menu mobile muncul atau tersembunyi
```
<nav class="shadow-lg fixed top-0 left-0 z-40 w-screen" style="background-color: #3C3633;">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-3xl font-bold text-white">Breezy</h1>
        </div>
        <div class="hidden md:flex items-center">
          <ul class="flex space-x-7">
            <li><a href="#" class="text-gray-300 hover:text-white">Home</a></li>
            <li><a href="#" class="text-gray-300 hover:text-white">Products</a></li>
            <li><a href="#" class="text-gray-300 hover:text-white">Categories</a></li>
            <li><a href="#" class="text-gray-300 hover:text-white">Cart</a></li>
          </ul>
          {% if user.is_authenticated %}
            <span class="text-gray-300 mx-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="bg-[#EE4E4E] hover:bg-[#EE4E4E] text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
          {% else %}
            <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">Login</a>
            <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden px-4 w-full">
      <div class="pt-2 pb-3 space-y-1">
        <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
        <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
        <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
        <a href="#" class="block text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">Login</a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
        {% endif %}
      </div>
    </div>

    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
</nav>

```