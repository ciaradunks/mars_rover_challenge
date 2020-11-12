from rest_framework import routers
from users import views as myapp_views

router = routers.DefaultRouter()
router.register(r'rovers', myapp_views.RoverViewset)
router.register(r'plateau', myapp_views.PlateauViewset)

# modify rover to have rover/user_id
# define rovers/execute/rover id variable