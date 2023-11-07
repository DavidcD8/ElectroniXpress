
from django.contrib import admin
from django.urls import path, include
from onlineshop import urls
from onlineshop import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import LogoutView
from allauth.account.views import LoginView
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('home.html', views.Home, name='home'),
    path('add_item/', views.add_item_view, name='add_item'),
    path('product_detail/<int:item_id>/',
         views.item_detail, name='product_detail'),
    path('item_list/', views.item_list_view, name='item_list'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('success/', views.success_view, name='success'),
    path('accounts/logout/',
         LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('profile/', views.Profile, name='profile'),
    path('edit_item/<int:item_id>/', views.edit_item_view, name='edit_item'),
    path('delete_item/<int:item_id>/',
         views.delete_item_view, name='delete_item'),
    path('profile/<str:username>/', views.view_other_profile,
         name='view_other_profile'),
    path('mark_as_sold/<int:item_id>/', views.mark_as_sold, name='mark_as_sold'),
    path('process_checkout/', views.process_checkout_view, name='process_checkout'),
    path('update_bag/<int:item_id>/', views.update_bag, name='update_bag'),
    path('profile/<str:username>/', views.Profile, name='profile'),
    path('item_list/', views.item_list_view, name='item_list'),
    path('search/', views.search_results, name='search_results'),
    path('bag/', include('bag.urls')),
    path('cart/', include('bag.urls')),  # Include the 'bag' app's URL patterns
    path('item/<int:item_id>/', views.item_detail, name='item'),
    path('checkout/', include('checkout.urls')),

    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
