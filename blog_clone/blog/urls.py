from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='new_post'),
    path('post/<pk>/edit/',views.UpdatePostView.as_view(),name='edit_post'),
    path('post/<pk>/delete/',views.DeletePostView.as_view(),name='delete_post'),
    path('drafts/',views.DraftListView.as_view(),name='draft_list'),
]
