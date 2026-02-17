from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .services import create_user, check_user, random_champ, species_desc, region_desc, update_points
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
        except:
            return JsonResponse({"message": "User was not successfully registered"})

        return JsonResponse({"message": "User successfully registered"})
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        databaseResponse = check_user(username, password)[0][0]

        if databaseResponse == username:
            return JsonResponse({"message": "User logged in successfully"})
        return JsonResponse({"message": "User did not log in successfully"})
    return JsonResponse({"error": "Invalid request method"})


def get_champ(request):
    if request.method == "GET":
        champion = random_champ()
        return JsonResponse({"message": champion})
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
        points = data['points']
    
        try:
            update_points(username, points)
            return JsonResponse({"message": "Points successfully updated"})
        except:
            return JsonResponse({"message": "Points not successfully updated"})
    return JsonResponse({"error": "Invalid request method"}, status=405)


