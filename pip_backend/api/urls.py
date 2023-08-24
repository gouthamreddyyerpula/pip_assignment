from django.urls import path
from . import views
urlpatterns = [

    path('signup', views.signup),
    path('getting_all_users', views.getting_all_users),

]
