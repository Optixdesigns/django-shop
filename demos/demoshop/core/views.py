from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.views.generic import TemplateView
from shop.product.models import Product
from shop.category.models import Category
from core.forms import CatalogForm
#from shop.models import Product

class IndexView(TemplateView):
  template_name = 'index.haml'
  
  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['products_latest'] = Product.objects.all()
    context['products_featured'] = Product.objects.filter(featured=True)[:12]
    context['random_span'] = ["1", "2", "3", "4", "6"]
    return context

  def get_settings(request):
    response_dict = RequestContext(request)
    return render_to_response('base.haml', response_dict)

def CatalogView(request, category_slug=None):
  form = CatalogForm()
  category = None

  if request.REQUEST:
    data = request.REQUEST.copy()
    form = CatalogForm(data=data)

  if category_slug:
    category = get_object_or_404(Category.objects.all(), slug=category_slug)
    form.qs = Product.objects.filter(categories=category)

  return render_to_response('shop/catalog.haml', {'form': form, 'category': category, }, context_instance=RequestContext(request))