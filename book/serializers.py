from rest_framework import serializers
from book.models import Book
from author.models import Authors 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['published']


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all())

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance