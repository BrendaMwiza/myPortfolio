from django.db import models

class Bakery(models.Model):
      name = models.CharField(max_length=32)
      description = models.CharField(max_length=300)
      post = models.ImageField(upload_to = 'pictures/')

      def save_post(self):
          self.save()

      def __str__(self):
        return self.name