"""dave_e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Home.views import get_index
from Accounts import urls as accounts_urls
#from Accounts import reset_urls as reset_urls
from Products import urls as products_urls
from django.views import static
from .settings import MEDIA_ROOT
from Cart import urls as cart_urls
from Payments import urls as payments_urls
from Categories import urls as categories_urls

from django.conf.urls import url, include

from Products import views as product_views
from Cart import views as cart_views
from Gallery import urls as gallery_urls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'accounts/',include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^cart/', include(cart_urls)),
    url(r'^payments/', include(payments_urls)),
    url(r'^categories/', include(categories_urls)),
    url(r'^gallery/', include(gallery_urls)),
    


]
