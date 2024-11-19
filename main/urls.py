from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, create_product_flutter

from main.views import register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'), # Kembalikan data dalam bentuk XML
    path('json/', show_json, name='show_json'), # Kembalikan data dalam bentuk JSON
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'), # Kembalikan dalam bentuk XML berdasarkan ID
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), # Kembalikan dalam bentuk JSON berdasarkan ID
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('create-flutter/', create_product_flutter, name='create_mood_flutter'),
] 

