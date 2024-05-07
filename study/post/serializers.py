# serializers.py
from rest_framework import serializers
from .models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    image = serializers.ImageField(write_only=True, required=False)
  
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('image')
        post = Post.objects.create(**validated_data, image=images_data[0] if images_data else None)
        for image_data in images_data:
            PostImage.objects.create(post=post, image=image_data)
        return post

