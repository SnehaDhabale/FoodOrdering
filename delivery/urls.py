
from django.urls import path, include
from . import views

app_name = 'delivery'
urlpatterns = [
    path('',views.customer_home, name = 'customer_home'),
    path('signin/',views.sign_in, name="sign_in"),
    path('signup/',views.sign_up, name = 'sign_up'),
    path('handle_signin/',views.handle_signin, name = 'handle_signin'),
    path('handle_signup/',views.handle_signup, name = 'handle_signup'),
    path('admin_home/',views.admin_home, name = 'admin_home'),
    path("admin_users/", views.admin_users, name="admin_users"),
    path("edit_user/<int:id>/", views.edit_user, name="edit_user"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
    path('add_res/',views.add_res, name = 'add_res'),
    path('display_res/', views.display_res, name='display_res'),
    path('admin_res/', views.admin_res, name='admin_res'),
    path('admin_menu/<int:id>/', views.admin_menu, name='admin_menu'),
    path('add_menu/<int:id>/',views.add_menu, name = 'add_menu'),
    path('edit_menu/<int:id>/', views.edit_menu, name='edit_menu'),
    path('delete_menu/<int:id>/',views.delete_menu, name= 'delete_menu'),
    path('delete_res/<int:id>/',views.delete_res, name= 'delete_res'),
    path('cusdisplay_res/<str:username>/',views.cusdisplay_res, name = 'cusdisplay_res'),
    path('cusmenu/<int:id>/<str:username>/',views.cusmenu, name = 'cusmenu'),
    path('show_cart/<str:username>/',views.show_cart,name = 'show_cart'),
    path('add_to_cart/<int:menuid>/<str:username>/',views.add_to_cart, name = 'add_to_cart'),
    path('orders/<str:username>',views.orders, name = 'orders'),
    path('checkout/<str:username>/',views.checkout, name = 'checkout'),
    path('about/', views.about, name='about'),
    path("orders_list/", views.orders_list, name="orders_list"),
    path("save-order/<str:username>/", views.save_order, name="save_order"),

]
