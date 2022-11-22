from rest_framework import serializers
from api.models import Students
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"