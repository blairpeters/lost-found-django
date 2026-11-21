from django.db import models
import uuid

def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return f'uploads/{new_filename}'

CATEGORIES = [
    ('Electronics', 'Electronics'),
    ('IDs', 'IDs'),
    ('Clothing', 'Clothing'),
    ('Others', 'Others'),

]
STATUS = [
    ('Lost', 'Lost'),
    ('Found', 'Found'),
    ('Claimed', 'Claimed'),
]

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    pic =models.ImageField(upload_to=gen_unique_path, default='default.jpg')
    status = models.CharField(max_length=100, choices=STATUS)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'items'


