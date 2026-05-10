from django.http import JsonResponse

def basicHome(request , *args, **kwargs):
    json_response = {"Message" : "Hello world"}
    return JsonResponse(json_response)
