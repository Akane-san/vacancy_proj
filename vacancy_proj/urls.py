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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from vacancy_app.views import main_view, vacancy_view, vacancies_view, vacancies_cat_view, company_view
from vacancy_app.views import *
from vacancy_app.views import custom_handler404, custom_handler500


handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<slug:category_name>/', vacancies_cat_view, name='vacancies_cat'),
    path('companies/<int:company_id>/', company_view, name='company'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
    path('vacancies/<int:vacancy_id>/send', vacancy_send_view, name='vacancy_send'),
    path('mycompany/letsstart/', mycompany_letsstart_view, name='mycompany_letsstart'),
    path('mycompany/create/', mycompany_create_view, name='mycompany_create'),
    path('mycompany/vacancies/', mycompany_vacancies_view, name='mycompany_vacancies'),
    path('mycompany/vacancies/create/', mycompany_vacancies_create_view, name='mycompany_vacancies_create'),
    path('mycompany/vacancies/<int:vacancy_id>/', mycompany_vacancy_view, name='mycompany_vacancy'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('/search?s=<query>', search_view, name='search'),
    path('/myresume/letsstart/', myresume_letsstart_view, name='myresume_letsstart'),
    path('/myresume/create/', myresume_create_view, name='myresume_create'),
    path('/myresume/', myresume_view, name='myresume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
                          