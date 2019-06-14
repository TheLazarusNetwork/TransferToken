from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^transfer-token/', views.TransferToken.as_view(), name='transfer_token'),

]