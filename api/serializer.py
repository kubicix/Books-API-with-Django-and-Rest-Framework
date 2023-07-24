from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_Date = serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)
