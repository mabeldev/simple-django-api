from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from aluraflix.views import ProgramaViewSet

router = routers.DefaultRouter()
router.register("programas", ProgramaViewSet, basename="programas")

schema_view = get_schema_view(
    openapi.Info(
        title="Alura Flix API",
        default_version="v1",
        description="Provedor loca de series e filmes da Alura",
        terms_of_service="#",
        contact=openapi.Contact(email="#"),
        license=openapi.License(name="#"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
