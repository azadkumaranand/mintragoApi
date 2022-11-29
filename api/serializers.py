from rest_framework import serializers
from api.models import LabDress, Cycle
class DressSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LabDress
        fields = "__all__"

class CycleSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cycle
        fields = "__all__"