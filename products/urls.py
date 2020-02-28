from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/v2/mode/', views.UpdateView.as_view(), name='mode'),
    path('<int:pk>/mode/', views.DeprecatedUpdateView.as_view(), name='deprecated_mode'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]