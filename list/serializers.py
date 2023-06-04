from rest_framework import serializers
from .models import ToDoItem, Tag
from django.contrib.auth.models import User
from datetime import datetime


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['user']


class ToDoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, allow_empty=True)

    class Meta:
        model = ToDoItem
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        # Remove tags from validated_data
        tags_data = validated_data.pop('tags', [])
        due_date = validated_data.get('due_date')

        # Check if due_date is in the past
        if due_date and due_date < datetime.now().date():
            raise serializers.ValidationError("Due date must be in the future.")

        user = self.context['request'].user

        # Create the ToDoItem object
        todo_item = ToDoItem.objects.create(**validated_data)

        for tag_data in tags_data:
            tag_name = tag_data.get('name')
            # Get or create the Tag object
            tag = Tag.objects.filter(name=tag_name)
            # Associate the Tag object's pk with the ToDoItem
            if not tag.exists():
                tag = Tag.objects.create(name=tag_name, user=user)
            else:
                tag = Tag.objects.get(name=tag_name)
            todo_item.tags.add(tag.pk)

        return todo_item

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        due_date = validated_data.get('due_date', instance.due_date)

        # Check if the requested ToDoItem belongs to the current user
        if instance.user != self.context['request'].user:
            raise serializers.ValidationError("You do not have permission to update this ToDoItem.")

        if due_date and due_date < datetime.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        user = self.context['request'].user

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.tags.clear()

        for tag_data in tags_data:
            tag_name = tag_data.get('name')
            # Get or create the Tag object
            tag = Tag.objects.filter(name=tag_name)
            # Associate the Tag object's pk with the ToDoItem
            if not tag.exists():
                tag = Tag.objects.create(name=tag_name, user=user)
            else:
                tag = Tag.objects.get(name=tag_name)
            instance.tags.add(tag)

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
