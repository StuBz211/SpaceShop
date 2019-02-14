from django.views import generic

from . import models


class ProductListView(generic.ListView):
    template_name = 'templates/web_site/list_view.html'

    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'templates/web_site/detail_view.html'
    model = models.Product

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        return queryset
