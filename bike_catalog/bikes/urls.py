from django.urls import path
from .views import bike_list, add_bike, edit_bike, delete_bike, bike_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bikes'

urlpatterns = [
    path('', bike_list, name='bike_list'),
    path('add/', add_bike, name='add_bike'),
    path('edit/<int:id>/', edit_bike, name='edit_bike'),
    path('delete/<int:id>/', delete_bike, name='delete_bike'),
    path('<int:id>/', bike_detail, name='bike_detail'),  # New URL pattern
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


