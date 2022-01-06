from django.urls import path
from .views import create_custom_user,render_pdf_view

urlpatterns = [
    path('create-user/', create_custom_user, name="create-user" ),
    path('create-pdf/<str:pk>/', render_pdf_view, name="create-pdf" ),

]
