from rest_framework import routers
from users import views as myapp_views

# Router classes handle the complexities of defining an url conf.
# Similar to providing an url pattern
router = routers.DefaultRouter()
router.register(r'rovers', myapp_views.RoverViewset)
router.register(r'plateau', myapp_views.PlateauViewset)

