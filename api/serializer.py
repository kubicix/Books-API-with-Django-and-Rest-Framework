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
    
    def update(self,instance,validated_data):
        instance.title=validated_data.get("title",instance.title)
        instance.number_of_pages=validated_data.get("number_of_pages",instance.number_of_pages)
        instance.publish_Date=validated_data.get("publish_Date",instance.publish_Date)
        instance.quantity=validated_data.get("quantity",instance.quantity)
        instance.save()
        return instance
