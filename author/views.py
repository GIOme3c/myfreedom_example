from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from author.models import Authors


class AuthorDetailView(DetailView):
    model = Authors


class AuthorListView(ListView):
    model = Authors


class AuthorCreateView(CreateView):
    model = Authors
    fields = "__all__"
    template_name = "author/authors_create.html"
    success_url = reverse_lazy('authors-list')


class AuthorUpdateView(UpdateView):
    model = Authors
    fields = "__all__"
    template_name = "author/authors_update.html"
    success_url = reverse_lazy('authors-list')


class AuthorDeleteView(DeleteView):
    model = Authors
    success_url = reverse_lazy('authors-list')
    template_name = "author/authors_delete.html"