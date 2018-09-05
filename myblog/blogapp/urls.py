from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

#app_name= ""

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^createblog/$', views.createblog, name='createblog'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^dashboard/resetpass/$', views.resetpass, name='resetpass'),
    url(r'^dashboard/myprofile/$', views.myprofile, name='myprofile'),
    url(r'^forget/$', views.forget, name='forget'),
    url(r'^set_new_pass/$', views.set_new_pass, name='set_new_pass'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^recipes/$', views.recipes, name='recipes'),
    url(r'^recipe-single/$', views.recipe_single, name='recipe-single'),
    url(r'^edit_recipe/$', views.edit_recipe, name='edit_recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)