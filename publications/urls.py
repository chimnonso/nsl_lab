from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [
    path('journals/', views.journal_list, name="journal_list"),
    path('journals/create/', views.JournalCreateView.as_view(), name='journal_create'),
    path('journals/update/<int:pk>', views.journal_update, name='journal_update'),
    path('journals/<int:pk>', views.JournalDetailView.as_view(), name='journal_detail'),
]