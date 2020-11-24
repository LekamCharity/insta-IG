from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('',views.index,name = 'home'),
    path('',views.profile, name='profile'),
    path('',views.search_results,name='search_results'),
    path('', views.single_pic, name='picture'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)