from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name = 'post_list'),
    url(r'^results/$', views.search, name = 'search'),
    url(r'^about/$', views.AboutView.as_view(), name= 'about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(), name = 'post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name = 'create_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name = 'update_post'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name = 'delete_post'),
    url(r'^drafts/$', views.DraftPostView.as_view(), name= 'draft_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,name = 'comment_remove'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,name = 'approve_comment'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name = 'publish_post'),
]
