from restapisecurity.views import BookAPIs#,#PostViewSet,JPostViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api',BookAPIs) # these 6 URIs

urlpatterns = router.urls