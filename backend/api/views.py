from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "This is your first APIS response from a request"})
