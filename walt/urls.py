from django.urls import path

from . import views

app_name = 'walt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:show>/<int:season>/', views.index, name='index'),
    path('<int:episode_id>/', views.edetail, name='edetail'),
    path('search/', views.search, name='search'),
    path('<str:character>/', views.cdetail, name='cdetail')
]