from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainview,name='mainview'),
    path('addmovie',views.addMovie,name='addmovie'),
    path('addcategory',views.addCategory,name='addcategory'),
    path('success',views.success,name='success'),
    path('selectshow',views.selectshow,name='selectshow'),
    path('selectseat/<int:idd>',views.selectseat,name='selectseat'),
    path('view_orders',views.view_orders,name='view_orders'),
    path('changeSeatStatus',views.changeSeatStatus,name='changeSeatStatus'),
]