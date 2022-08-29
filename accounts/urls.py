from django.urls import path
from vacancy_app.views import login_view, logout_view, register_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', logout_view, name='register'),
]
