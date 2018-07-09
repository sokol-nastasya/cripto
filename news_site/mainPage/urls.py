from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name = 'news'),
	url(r'^news/(?P<n_id>[0-9]+)/$', views.show_news, name = 'show_news'),
	url(r'^about/', views.about, name = 'about'),

]
