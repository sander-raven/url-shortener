from django.urls import path

from shortener import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:short_code>', views.redirect_view, name='redirect'),
]
