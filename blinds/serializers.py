from rest_framework import serializers
from blinds.models import Article
from blinds.models import Comment


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(required=True, allow_blank=False, max_length=10)
    board_id = serializers.IntegerField(required=False, allow_null=False)
    title = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    body = serializers.CharField(required=True, allow_blank=False, max_length=2000)
    views = serializers.IntegerField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(required=True, allow_blank=False, max_length=10)
    article_id = serializers.IntegerField(required=False, allow_null=False)
    comment_id = serializers.IntegerField(required=False, allow_null=False)
    body = serializers.CharField(required=True, allow_null=False, max_length=2000)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
