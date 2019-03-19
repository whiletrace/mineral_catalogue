from django.urls import path


from . import views
app_name = 'trace_minerals'

# sets URL for Index and detail templates for app trace_minerals
urlpatterns =[

    path('', views.mineral_list, name='trace_minerals_index'),
    path('<int:pk>', views.mineral_detail, name='trace_minerals_detail'),

    ]
