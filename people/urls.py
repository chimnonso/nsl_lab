from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('professors/', views.professors_list, name="professors_list"),
    path('post_docs/', views.post_docs_list, name="post_docs_list"),
    path('post_docs/<int:pk>', views.PostDoctDetailView.as_view(), name="post_docs_detail"),
    # path('about', views.about, name="about"),
]