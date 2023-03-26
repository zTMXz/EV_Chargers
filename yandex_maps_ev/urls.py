from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from yandex_maps_ev import views

urlpatterns = [
    path("", views.yandex_maps, name='map_ya'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)