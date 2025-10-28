from django.db import models


class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Publish"
    COMING_SOON = "soon", "Coming soon"
    DRAFT = "draft", "Draft"


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT,
    )

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
