from django.conf.urls.defaults import patterns, url

from shop.products.views import ProductDetailView
from shop.products.models import Product

urlpatterns = patterns('',
    #url(r'^$',
     #   ShopListView.as_view(model=Product),
      #  name='product_list'
    #    ),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$',
        ProductDetailView.as_view(),
        name='product_detail'
        ),
    )