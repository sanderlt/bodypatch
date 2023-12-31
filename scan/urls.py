from django.urls import path
from scan import views


urlpatterns = [
   #path('', views.home_view, name='index')
   path('', views.upload_canvas, name='upload-canvas'),

]