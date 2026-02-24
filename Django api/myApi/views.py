import json
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def tasks(request):

    if request.method == "GET":
        data = list(Task.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)
        Task.objects.create(title=body.get("title",""))
        return JsonResponse({"status":"created"})