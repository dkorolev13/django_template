from django.db import models


class My_text(models.Model):
    my_text = models.CharField(max_length=255)


