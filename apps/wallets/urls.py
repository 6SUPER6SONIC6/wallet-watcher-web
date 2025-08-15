from django.urls import path

from apps.wallets import views

app_name = 'wallets'
urlpatterns = [
    path(
        route='',
        view=views.index,
        name='index'
    ),
    path(
        route='wallet/<str:address>/',
        view=views.wallet_detail,
        name='detail'
    )
]
