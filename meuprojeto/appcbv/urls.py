from django.urls import path
from .views import HelloView, CachorroListView

urlpatterns = [path("", HelloView.as_view(), name="index"),
               path ("listar", CachorroListView.as_view(), name="listar_cachorros"),
               ]