from django.urls import path
from .views import test_api, register_user, login_user, get_random_champ, get_species_desc, get_region_desc, update_user_points, get_champ_info, get_random_quote, get_random_ability, check_existing_champ, get_leaderboard_info

urlpatterns = [
    path("test/", test_api),
    path("register_user/", register_user),
    path("login_user/", login_user),
    path("get_random_champ/", get_random_champ),
    path("get_species_desc/", get_species_desc),
    path("get_region_desc/", get_region_desc),
    path("update_user_points/", update_user_points),
    path("get_champ_info/", get_champ_info),
    path("get_random_quote/", get_random_quote),
    path("get_random_ability/", get_random_ability),
    path("check_existing_champ/", check_existing_champ),
    path("get_leaderboard_info/", get_leaderboard_info),
]