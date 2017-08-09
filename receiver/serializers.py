from rest_framework import serializers

from .models import MQTTAction, TopicSubscription

class TopicSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicSubscription
        fields = '__all__'


class MQTTActionSerializer(serializers.ModelSerializer):
    topics = TopicSubscriptionSerializer(read_only=True, many=True)
    class Meta:
        model = MQTTAction
        fields = '__all__'

    def create(self, validated_data):
        validated_data['action'] = self.context['request'].META['HTTP_VERNEMQ_HOOK']
        return super().create(validated_data)
