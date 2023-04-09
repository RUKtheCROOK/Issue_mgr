from django.urls import path
# from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView
from issues import views

urlpatterns = [
    path('', views.IssueListView.as_view(), name='issue_list'),
    path('<int:pk>/', views.IssueDetailView.as_view(), name='issue_detail'),
    path('new/', views.IssueCreateView.as_view(), name='issue_new'),
    path('<int:pk>/edit/', views.IssueUpdateView.as_view(), name='issue_edit'),
    path('<int:pk>/delete/', views.IssueDeleteView.as_view(), name='issue_delete'),
]
