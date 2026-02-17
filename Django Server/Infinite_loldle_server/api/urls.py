from django.urls import path
from .views import test_api, register_user, login_user, get_champ, get_species_desc, get_region_desc, update_user_points

urlpatterns = [
    path("test/", test_api),
    path("register_user/", register_user),
    path("login_user/", login_user),
    path("get_champ/", get_champ),
    path("get_species_desc/", get_species_desc),
    path("get_region_desc/", get_region_desc),
    path("update_user_points/", update_user_points)
]