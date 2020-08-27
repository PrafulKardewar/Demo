from rest_framework.routers import SimpleRouter
from appone.views import *

router = SimpleRouter()

router.register('api/v1',EmpOperations)    #appone
router.register('api/v2',AddressOperations)  #apptwo

urlpatterns = router.urls