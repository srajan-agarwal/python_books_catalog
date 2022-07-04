from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r"^", views.BooksCatalogueView)

urlpatterns = router.urls
