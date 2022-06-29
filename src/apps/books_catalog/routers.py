from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

# router.register("", views.ContentBriefView, 'content_brief')
router.register(r"^", views.BooksCatalogueView)

urlpatterns = router.urls
