from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    rating = models.IntegerField(max_length=5)
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    submisson_date = models.DateField()
    company = models.TextField()
    reviewer_metadata = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return '{}: {}'.format(self.title, self.id)


    def to_json(self):
        return {
            'id': self.id,
            'rating':self.rating,
            'title': self.title,
            'summary': self.summary,
            'submisson_date': self.submisson_date,
            'company': self.company,
            'reviewer_metadata': self.reviewer_metadata,
            'created_by': self.created_by
        }
