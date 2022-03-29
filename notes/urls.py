from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update',views.update,name="update"),
    path('delete',views.delete,name="delete"),
    path('tagviewer',views.getByTag,name="tagviewer"),
    path('tags',views.tags,name="tags"),
]