
from django.urls import path
from enrollment import views
urlpatterns =[

    path('',views.add_show,name='addshow'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
]