from django.urls import path,include

urlpatterns = [
    path("djangoApi/",include("myApi.urls")),
]
