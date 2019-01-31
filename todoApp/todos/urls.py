from django.urls import path
from todos.views import TodoList, DeleteItems, UploadImage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('delete/<itemId>', DeleteItems.as_view(), name='todo-delete'),
    path('uploads/', UploadImage.as_view(), name='upload-image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)