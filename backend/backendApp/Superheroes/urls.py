from django.urls import path
from Superheroes import views

# Routing for APIs endpoints

from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('superheroes/', views.superheroesApi),
    path('superheroes/<int:id>/', views.superheroesApi),

    path('superpowers/', views.superpowersApi),
    path('superpowers/<int:id>/', views.superpowersApi),

    path('leagues/', views.leaguesApi),
    path('leagues/<int:id>/', views.leaguesApi),

    path('superhero/SaveFile', views.SaveFile),
    path('media/images/<str:image_name>/', views.serve_image, name='serve_image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
