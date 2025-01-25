"""
URL configuration for eisaal_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('shop', views.shop, name='shop' ),
    path('about', views.about, name='about' ),
    path('get_products/<int:Sno>', views.get_products, name='get_products' ),
    path('contact', views.contact, name='contact' ),
    path('<int:Sno>/order', views.order, name='order'),
    path('order_now/', views.order_now, name='order_now'),
    path('verify_payment/', views.verify_payment, name='verify_payment'),
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),

]
