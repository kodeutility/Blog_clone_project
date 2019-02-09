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
    path('post/<pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<pk>/publish/',views.post_publish,name='post_publish'),

]
