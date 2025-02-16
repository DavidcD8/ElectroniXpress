from django.urls import path
from onlineshop import views

urlpatterns = [
    path("add_item/", views.add_item_view, name="add_item"),
    path("item_list/", views.item_list_view, name="item_list"),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("edit_item/<int:item_id>/", views.edit_item_view, name="edit_item"),
    path("delete_item/<int:item_id>/", views.delete_item_view, name="delete_item"),
    path("profile/", views.Profile, name="profile"),
    path("profile/<str:username>/", views.view_other_profile, name="view_other_profile"),
    path("mark_as_sold/<int:item_id>/", views.mark_as_sold, name="mark_as_sold"),
    path("process_checkout/", views.process_checkout_view, name="process_checkout"),
    path("update_bag/<int:item_id>/", views.update_bag, name="update_bag"),
    path("search/", views.search_results, name="search_results"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("subscribe_newsletter/", views.subscribe_newsletter, name="subscribe_newsletter"),
    path("terms_and_privacy/", views.terms_and_privacy, name="terms_and_privacy"),
    path("profile/<str:username>/", views.Profile, name="profile"),
]
