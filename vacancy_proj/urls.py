"""vacancy_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from vacancy_app.views import main_view, vacancy_view, vacancies_view, vacancies_cat_view, company_view
from vacancy_app.views import custom_handler404, custom_handler500


handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:category_name>/', vacancies_cat_view, name='vacancies_cat'),
    path('companies/<int:company_id>/', company_view, name='company'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
]
