from django.views import generic

from . import models


class ProductListView(generic.ListView):
    template_name = 'product_list.html'

    model = models.Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'detail_view.html'

    model = models.Product

    def get_context_data(self, **kwargs):
        queryset = super(ProductDetailView, self).get_context_data(**kwargs)
        return queryset
