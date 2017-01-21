"""pynguinii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import json
import urllib2

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from social_news import views
from social_news.models import Posts

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^login/', auth_views.login, name='login'),
                  url(r'^register/', views.register_user),
                  url(r'^add-comment/(?P<post_id>\d+)/$', views.add_comment, name='add_comment'),
                  url(r'^add-post/', views.add_post),
                  url(r'^increase_by_one/', views.increase_by_one),
                  url(r'^post/(?P<post_id>\d+)/$', views.get_post_by_id),
                  url(r'^post/(?P<post_id>\d+)/edit/$', views.edit_post),
                  url(r'^post/(?P<post_id>\d+)/delete/$', views.delete_post),
                  url(r'^like_post/(?P<post_id>\d+)/$', views.like_post),
                  url(r'^my_news/$', views.get_my_news),
                  url(r'^my_comments/$', views.get_my_comments),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
                  url(r'^$', views.homepage)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

request_key_string = '7b19599570274c70b0d7132ca457eab6'
response = urllib2.urlopen(
    'https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=' + request_key_string)
data = json.load(response)
user = User.objects.filter(is_superuser=True).first()
for article in data['articles']:
    Posts.objects.get_or_create(title=article['title'], content=article['description'], user=user)
