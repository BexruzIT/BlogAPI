from django.urls import path
from blog import views

urlpatterns = [
    # fbw
    path('blogs/search/', views.search_blogs, name='search-blogs'),
    path('blogs/', views.BlogListCreateAPIView.as_view(), name='blog-list-create'),

    # cbw
    path('cbw/blogs/', views.BlogListCreateAPIView.as_view(), name='cbw-blogs-list-create'),
    path('cbw/blogs/<int:pk>/', views.BlogRetriveUpdateDeleteAPIView.as_view(), name='cbw-blogs-list-create'),
]
