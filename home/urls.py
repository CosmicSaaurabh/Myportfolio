from django.contrib import admin
from django.urls import path, include 
from home import views

# Djang admin header customisation
admin.site.site_header = "Login to Database"
admin.site.site_title = "Welcome to saurabh's database"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
   path('', views.index, name='index'),
   path('about', views.about, name='about'),
   path('project', views.project, name='project'),
   path('contactme', views.contactme, name='contactme'),
   path('Achievements', views.Achievements, name='Achievements'),
   path('Links', views.Links, name='Links'),
]
