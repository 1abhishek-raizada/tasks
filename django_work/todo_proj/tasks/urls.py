from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import task_list,delete_task,update_task


urlpatterns=[
    path('',task_list,name='task_list'),
    path('update/<int:task_id>/',update_task,name='update_task'),
    path('delete/<int:task_id>/',delete_task,name='delete_task'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
