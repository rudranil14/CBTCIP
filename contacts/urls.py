from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('list/', views.list_contacts, name='list_contacts'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
    path('users/', include('users.urls')),

    # AI
    path('assistant/', views.assistant, name='assistant'),

    # Emergency
    path('emergency/', views.emergency, name='emergency'),
    path(
        'emergency/<str:service>/',
        views.emergency_location,
        name='emergency_location'
    ),
    path(
        'emergency/<str:service>/results/',
        views.emergency_results,
        name='emergency_results'
    ),
]