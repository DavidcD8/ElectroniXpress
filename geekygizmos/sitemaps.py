from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'item_list', 'add_item', 'profile', 'checkout']

    def location(self, item):
        return reverse(item)
