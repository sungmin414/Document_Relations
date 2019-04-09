from django.db import models

__all__ = (
    'RelatedUser',
    'PhotoPost',
    'TextPost',
    'PostBase',
)


class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete=models.CASCADE,
        # 유저(Person) 입장에서
        # 자신이 특정 Post의 author인 경우에 해당하는 모든 PostBase 객체를 참조
        related_name='%(class)s_set',
        related_query_name='%(class)s'

    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    # author의 related_name
    # photopost_set
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'


class TextPost(PostBase):
    # author의 related_name
    # textpost_set
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'
