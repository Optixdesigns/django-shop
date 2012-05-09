### Django shop by Optixdesigns.

## Installation

		pip install https://github.com/Optixdesigns/django-shop

Add the folowwing to your ``INSTALLED_APPS`` setting

		...
		'shop',
    	'shop.products',
    	'shop.orders',
    	'shop.cart',
    	...

Add ``'shop.cart.middleware.CartMiddleware'`` to ``MIDDLEWARE_CLASSES``.

Add ``'shop.cart.context_processors.cart'`` to ``TEMPLATE_CONTEXT_PROCESSORS``.

Add app urls to your project URLConf::

    url(r'^shop/', include('shop.urls'))
   	