
from django.conf.urls import url
from countries_app import views


urlpatterns=[
    url(r'^api/countries$', views.countries_list),
    # regex usesd here
    #  r tells that it's a raw string expression

    url(r'^api/countries/(?P<pk>\d+)$', views.countries_detail),
    #  named regex froup

    # url('api/countries', views.countries_list),
    # url('/api/countries/(?P<pk>\d+)/$', views.countries_detail),

]
