from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    #pk = serializers.IntegerField(read_only=True)
    #title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    #age = serializers.CharField(required=False, allow_blank=True, max_length=100)
    #def create(self, validated_data):
    #    """
    #    Create and return a new `Snippet` instance, given the validated data.
    #    """
    #    return Snippet.objects.create(**validated_data)

    #def update(self, instance, validated_data):
    #    """
    #    Update and return an existing `Snippet` instance, given the validated data.
    #    """
    #    instance.title = validated_data.get('title', instance.title)   
    #
    #    instance.save()
    #    return instance

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'age')
