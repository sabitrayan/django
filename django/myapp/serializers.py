from rest_framework import serializers
from myapp.models import Review
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]



class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.CharField()
    submisson_date = serializers.DateField()
    company = serializers.CharField()
    reviewer_metadata = serializers.CharField()

    class Meta:
        model = Review
        fields = [
            'id',
            'rating',
            'title',
            'summary',
            'submisson_date',
            'company',
            'reviewer_metadata',
        ]