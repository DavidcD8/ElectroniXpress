"""
URL configuration for geekygizmos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from onlineshop import urls
from onlineshop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('add_item/', views.add_item_view, name='add_item'),
    path('product_detail/<int:item_id>/',
         views.item_detail, name='product_detail'),
    path('item_list/', views.item_list, name='item_list'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('search/', views.search_results, name='search_results'),
    path('bag/', include('bag.urls')),
    path('profile/', views.Profile, name='profile'),

    path('accounts/', include('allauth.urls')),
    path('product/add/', views.add_item_view, name='add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
