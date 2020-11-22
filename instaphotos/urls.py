from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from instaphotos.views import PostLikeToggle, PostLikeAPIToggle

urlpatterns = [
    path('', views.signup, name='signup'),
    path('', include('registration.backends.simple.urls')),
    path('', views.profile, name='profile'),
    path('', views.user_profile, name='user_profile'),
    path('', views.post_comment, name='comment'),
    path('', PostLikeToggle.as_view(), name='liked'),
    path('', PostLikeAPIToggle.as_view(), name='liked-api'),
    path('', views.like_post, name='like_post'),
    path('', views.search_profile, name='search'),
    path('', views.follow, name='follow'),
    path('', views.unfollow, name='unfollow'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


 