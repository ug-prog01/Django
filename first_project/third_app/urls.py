from django.conf.urls import url
from third_app import views
from django.urls import path

app_name = 'third_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('baka/', views.baka, name='baka'),
    path('', views.linking, name='template_inheritance'),
]