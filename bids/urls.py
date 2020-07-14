from django.urls import path, include
from .views  import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'bids'

urlpatterns = format_suffix_patterns([
    path('', SubmitList.as_view(), name='bidding-upload'),
    path('detail/', Table.as_view(), name = 'biding-top'),
])
