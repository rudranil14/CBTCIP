from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),

    path('logout/', views.logout_view, name='logout'),

    path('about/', views.about, name='about'),

    path('faq/', views.faq, name='faq'),

]