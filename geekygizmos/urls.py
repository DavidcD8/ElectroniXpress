from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from allauth.account.views import LogoutView, LoginView
from onlineshop.views import Home
from geekygizmos.sitemaps import StaticViewSitemap

# Custom error handler
handler404 = "onlineshop.views.handler404"

sitemaps = {"static": StaticViewSitemap}

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # Sitemap
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

    # Home Page
    path("", Home, name="home"),

    # Authentication
    path("accounts/logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("accounts/login/", LoginView.as_view(), name="account_login"),
    path("accounts/", include("allauth.urls")),

    # Include URLs from apps
    path("shop/", include("onlineshop.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path("faq/", include("faq.urls")),
]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
