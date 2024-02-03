# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname','lastname','profilePicture','email', 'password',  'role', 'bio', 'address', 'stripeCustomerId', 'stripeSubscriptionId', 'stripePriceId', 'stripeCurrentPeriodEnd',]
        extra_kwargs = {'password': {'write_only': True}}
