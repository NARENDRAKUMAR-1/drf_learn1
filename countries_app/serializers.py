from rest_framework import serializers

from countries_app.models import Countries # it's out table class

class CountriesSerializer(serializers.ModelSerializer):

    # CountriesSerializer will manage the serialization and deserialization from JSON ?, only json?
    # serializers class of rest framework has all the validators and other things needed

    class Meta:
        # Meta class has what to be serialized
        model = Countries
        fields=('id', 'name', 'capital' )