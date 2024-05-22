from rest_framework import routers
from .api import personaViewSet

router = routers.DefaultRouter()

router.register("personas",personaViewSet,"persona")

urlpatterns = router.urls