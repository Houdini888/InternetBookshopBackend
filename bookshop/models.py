from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=1000, default="No description available.")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=255)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def get_absolute_cover_url(self):
        if self.cover:
            return f'http://localhost:8000{self.cover.url}'
        return ''

    def __str__(self):
        return self.title
