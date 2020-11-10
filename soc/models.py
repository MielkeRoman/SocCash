from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

User = get_user_model()


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class New(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('wait_publish', 'Wait Publish')
    )
    new_author = models.ForeignKey(User, on_delete=models.CASCADE)
    new_title = models.CharField(max_length=200)
    new_body = models.TextField()
    new_publish = models.DateTimeField(default=timezone.now)
    new_created = models.DateTimeField(auto_now_add=True)
    new_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default='draft')
    new_slug = models.SlugField(max_length=250,
                            unique_for_date='new_publish')

    class Meta:
        def __str__(self):
            ordering = ('-new_publish',)

            return self.title

    published = PublishedManager()

    def get_absolute_url(self):
        return reverse(
                       args=[self.new_publish.year,
                             self.new_publish.month,
                             self.new_publish.day,
                             self.new_slug])