from django.urls import path,include
from .views import home_View,audioList,audioCreate,audioUpdate,audioDelete

urlpatterns = [
    path("", home_View, name="home"),
    path("create/",audioCreate,name='audioFileType-create'),
    path("<str:audioFileType>/", audioList, name="audioFileType-list"),
    path("<str:audioFileType>/<str:pk>/",audioList,name='audioFileType-detail'),
    path('update/<str:audioFileType>/<str:pk>/',audioUpdate,name='audioFileType-update'),
    path('delete/<str:audioFileType>/<str:pk>/',audioDelete,name='audioFileType-delete')
    
]