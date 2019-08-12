from django.urls import path, include
from blogging.views import stub_view, list_view, detail_view, new_post
from blogging.views import PostsViewSet, CategoriesViewSet, UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('new-post/', new_post, name='new_post'),
    path('api/', include(router.urls)),
]