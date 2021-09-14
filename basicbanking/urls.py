from django.urls import path
from .views import home, home_post, transaction

urlpatterns = [
    path('', home, name='home-page'),
    path('<int:key>/', home_post, name='post-home'),
    path('transaction/<int:key>/', transaction, name='transaction'),
]