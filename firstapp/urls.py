
from django.urls import path

from firstapp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('wayanad',views.wayanad,name='wayanad'),
    path('thrissur',views.thrissur,name='thrissur'),
    path('idukki',views.idukki,name='idukki'),
    path('alappuzha',views.alappuzha,name='alappuzha'),
    path('add',views.add,name='add'),
    path('add_num',views.add_num,name='add_num'),
    path('result',views.result,name='result'),
    path('',views.calc_page,name='calc_page'),
    path('calc',views.calc,name='calc')


]

