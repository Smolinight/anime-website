from django.db import models

'''
./manage.py shell 
Anime(name='...', description='...', rating=...)
a1 = _
||
a2 = Anime.objects.create(name='...', description='...', rating=...)
Anime.objects.all()
Anime.objects.all().order_by('rating')
Anime.objects.filter(name='Наруто')
Anime.objects.filter(rating__gte=5) #все аниме у которых рейтинг больше 5
Anime.objects.get(pk=1) # исплользуется только когда нужно вернуть строго одну запись
'''

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    rating = models.FloatField()

    def __str__(self):
        return self.name