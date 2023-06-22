from rest_framework import routers
from .api import projectviewset
router = routers.DefaultRouter()

router.register('api/projects', projectviewset, 'projects' )

urlpatterns  = router.urls