from django.shortcuts import render, redirect, get_object_or_404
from .services import LaravelUserService
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# URL de base de l'API Laravel
# LARAVEL_API_URL = "http://laravel-service:8000"
LARAVEL_API_URL = "http://localhost:8000"

# Initialiser le service
laravel_service = LaravelUserService(LARAVEL_API_URL)

def user_list_view(request):
    users = laravel_service.get_users()
    return render(request, 'users/user_list.html', {'users': users})

def user_create_view(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),  # Ajouter le champ password
        }
        laravel_service.create_user(data)
        return redirect('user_list')
    return render(request, 'users/user_create.html')

def user_update_view(request, user_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),  # Ajouter le champ password
        }
        laravel_service.update_user(user_id, data)
        return redirect('user_list')
    user = laravel_service.get_user(user_id)
    return render(request, 'users/user_update.html', {'user': user})

def user_delete_view(request, user_id):
    if request.method == 'POST':
        laravel_service.delete_user(user_id)
        return redirect('user_list')
    user = laravel_service.get_user(user_id)
    return render(request, 'users/user_confirm_delete.html', {'user': user})


@csrf_exempt  # Désactive la protection CSRF pour cette vue (à utiliser avec précaution)

def call_laravel_logout(request):
    if request.method == 'POST':
        laravel_url = 'http://laravel-service/logout'  # Remplacez par l'URL réelle
        try:
            response = requests.post(laravel_url, headers={
                'Authorization': f'Bearer {request.session.get("laravel_token")}',  # Jeton d'authentification
                # 'X-CSRF-TOKEN': request.POST.get('csrf_token'),  # Jeton CSRF
            }, allow_redirects=False)  # Désactiver la redirection automatique

            # Vérifier la réponse de l'API Laravel
            if response.status_code == 302:  # Redirection attendue
                return JsonResponse({'status': 'success', 'message': 'Logged out successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Failed to log out'}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)