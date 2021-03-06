from rest_framework import serializers
from ..models.Device import DeviceData
from ..utils.function import TimestampField


class DeviceSerializer(serializers.ModelSerializer):
    # create_at = TimestampField("create_at")
    create_at = serializers.DateTimeField( format="%H:%M:%S %d-%m-%Y",input_formats=["%Y-%m-%d %H:%M:%S",])
    class Meta:
        model = DeviceData
        fields = ['id', 'device', 'data', 'create_at']