from django.urls import path

from menu.views import MenuView, MenuPageView


urlpatterns = [
    path('', MenuView.as_view()),
    path('<slug:menu>/', MenuPageView.as_view(), name='menu'),
    path('<slug:menu>/<slug:item>/', MenuPageView.as_view(), name='item')
]
