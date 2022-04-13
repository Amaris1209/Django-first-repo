from django.urls import path,include

app_name = "gari_wala"

urlpatterns = [
    path("api/",include('gari_wala.api.urls')),
   ]