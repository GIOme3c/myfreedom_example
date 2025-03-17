from django.urls import path
from author.views import AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

арр_name = "authors"

urlpatterns = [
    path('<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('list/', AuthorListView.as_view(), name="authors-list"),
    path('create/', AuthorCreateView.as_view(), name="authors-create"),
    path('update/', AuthorUpdateView.as_view(), name="authors-update"),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name="authors-delete"),
]