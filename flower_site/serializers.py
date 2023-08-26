from rest_framework.serializers import ModelSerializer, Serializer, IntegerField, ValidationError

from .models import ConsultationSignUp, Bouquet, Order, OrderedBouquet


class ConsultationSerializer(ModelSerializer):
    def create(self, validated_data):
        consultation = ConsultationSignUp.objects.create(**validated_data)
        return consultation

    class Meta:
        model = ConsultationSignUp
        fields = ['name', 'phone']


class BouquetIDSerializer(Serializer):
    bouquet_id = IntegerField(min_value=0)

    def validate_id(self, value):
        try:
            Bouquet.objects.get(id=value)
        except Bouquet.DoesNotExist:
            raise ValidationError
        return value


class OrderSerializer(ModelSerializer):
    bouquet_id = IntegerField(min_value=0)

    def create(self, validated_data):
        bouquet_id = validated_data.pop('bouquet_id')
        order = Order.objects.create(**validated_data)
        bouquet = Bouquet.objects.get(id=bouquet_id)
        ordered_bouquet = OrderedBouquet.objects.create(bouquet=bouquet, order=order)
        ordered_bouquet.fixed_price = bouquet.price
        ordered_bouquet.save()
        return order

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'bouquet_id', 'delivery_interval']
