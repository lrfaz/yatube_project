# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
    CharField,
    SET_NULL,
)

User = get_user_model()


class Group(Model):
    title = CharField(max_length=200)
    slug = CharField(max_length=200)
    description = TextField()

    def __str__(self) -> str:
        return f"{self.title}"


class Post(Model):
    text = TextField()
    pub_date = DateTimeField(auto_now_add=True)
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="posts",
    )
    group = ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="posts",        
    )

    class Meta:
        ordering = ['-pub_date']
