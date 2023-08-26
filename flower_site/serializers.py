from rest_framework.serializers import ModelSerializer, ListField, ValidationError

from .models import ConsultationSignUp


class ConsultationSerializer(ModelSerializer):
    def create(self, validated_data):
        consultation = ConsultationSignUp.objects.create(**validated_data)
        return consultation

    class Meta:
        model = ConsultationSignUp
        fields = ['name', 'phone']
