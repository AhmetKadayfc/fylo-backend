from django.urls import path

from .views import BlogCreate, BlogDetail, BlogCategoryCreate, BlogCategoryDetail, TagCreate, TagDetail

#Blog url pattern
urlpatterns = [
    path('', BlogCreate.as_view(), name="blogs"),
    path('<str:title>/', BlogDetail.as_view(), name="blog"),
    path('tags', TagCreate.as_view(), name="tags"),
    path('tags/<str:title>', TagDetail.as_view(), name="tag"),
    path('categories', BlogCategoryCreate.as_view(), name="categories"),
    path('categories/<str:title>', BlogCategoryDetail.as_view(), name="category")
]
