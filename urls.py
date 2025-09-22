from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name='create'),
    path('display/',views.display,name='display'),
    path("single/<int:pk>",views.single,name='single'),
    path("update/<int:vk>",views.update,name='update'),
    path("delete/<int:z>",views.delete,name='delete')
]
