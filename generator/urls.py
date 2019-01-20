from django.urls import path

from generator import views

app_name = 'generator'
# ルーティングの設定
urlpatterns = [path('', views.index, name='index'),
path('ajax/category/', views.get_category, name='get_category'),
path('ajax/sub_category/', views.get_sub_category, name='get_sub_category'),
path('ajax/silhouette/', views.get_silhouette, name='get_silhouette'),
path('ajax/design/', views.get_design, name='get_design'),
path('ajax/neck/', views.get_neck, name='get_neck'),
path('ajax/coller/', views.get_coller, name='get_coller'),
path('ajax/zip_button/', views.get_zip_button, name='get_zip_button'),
path('ajax/length/', views.get_length, name='get_length'),
path('ajax/leg/', views.get_leg, name='get_leg'),
path('ajax/effect/', views.get_effect, name='get_effect'),
]
