from django.urls import path
from . import views

app_name = 'quoteapp'


urlpatterns = [
    path('main', views.main,name='main'),
    path('addquote/',views.addquote,name='addquote'),
    path('addtag/',views.addtag,name='addtag'),
    path('addauthor/',views.addauthor,name='addauthor'),
    path('author_detail/<int:author_id>',views.author_detail,name='author_detail')
]