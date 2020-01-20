from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<author>/", views.author, name="author"),
    path("<int:pk>/", views.detail, name="detail"),
    path("tag/<tag>/", views.tag, name="tag"),
    path("<random>/", views.customerror, name='error-page'),
]