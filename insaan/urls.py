from django.urls import path,include

app_name = "insaan"

urlpatterns = [
    path("api/",include('insaan.api.urls')),
   ]