from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .services import create_user, check_user, random_champ, species_desc, region_desc, update_points, selected_champ, random_quoute, random_ability, check_name, leaderboard_info

# Create your views here.
def test_api(request):
    return JsonResponse({
        "message": "Backend connected successfully!"
    })

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']

        try:
            create_user(username, password, email)
            return JsonResponse({"message": "User successfully registered"})
        except:
            return JsonResponse({"message": "There is already an existing user with that username or email"})
        
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        try:
            databaseResponse = check_user(username, password)[0][0]
            if databaseResponse == username:
                return JsonResponse({"message": "User logged in successfully"})
        except:
            return JsonResponse({"message": "User did not log in successfully"})
    return JsonResponse({"error": "Invalid request method"})


def get_random_champ(request):
    if request.method == "GET":
        try:
            champ_name = random_champ()
            champ_info = selected_champ(champ_name)
            return JsonResponse({"message": champ_info})
        except:

            return JsonResponse({"message": None})
    return JsonResponse({"error": "Invalid request method"})


def get_species_desc(request):
    if request.method == "GET":
        name = request.GET.get("name")
        description = species_desc(name)
        return JsonResponse({"message": description})
    return JsonResponse({"error": "Invalid request method"})


def get_region_desc(request):
    if request.method == "GET":
        name = request.GET.get("name")
        description = region_desc(name)
        return JsonResponse({"message": description})
    return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def update_user_points(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        points = data['resPoints']
    
        try:
            update_points(username, points)
            return JsonResponse({"message": "Points successfully updated"})
        except:
            return JsonResponse({"message": "Points not successfully updated"})
    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_champ_info(request):
    if request.method == "GET":
        name = request.GET.get("name")

        try:
            info = selected_champ(name)
            return JsonResponse({"message": info})
        except:
            return JsonResponse({"message": None})
    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_random_quote(request):
    if request.method == "GET":
        try:
            quote = random_quoute()
            return JsonResponse({"message": quote})
        except:
            return JsonResponse({"message": None})
    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_random_ability(request):
    if request.method == "GET":
        try:
            ability = random_ability()
            return JsonResponse({"message": ability})
        except:
            return JsonResponse({"message": None})
    return JsonResponse({"error": "Invalid request method"}, status=405)


def check_existing_champ(request):
    if request.method == "GET":
        name = request.GET.get("name")

        existing = check_name(name)
        return JsonResponse({"message": existing})

        
    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_leaderboard_info(request):
    if request.method == "GET":

        info = leaderboard_info()
        return JsonResponse({"message": info})

        
    return JsonResponse({"error": "Invalid request method"}, status=405)