from django.db import models


class DemoA(models.Model):
    name = models.CharField(max_length=255)
    expire_timestamp = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'demo_a'

