from django.db import models
from django.utils.text import slugify as django_slugify
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}
def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название меню'
        verbose_name_plural = 'Названия меню'
        ordering = ['title']


class MenuItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка')
    level = models.PositiveIntegerField(default=1, verbose_name='Уровень')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name='Родитель')
    menu_name = models.ForeignKey(Menu, verbose_name='Название меню', on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        
        if self.parent:  
            self.level = self.parent.level + 1
            self.url = self.parent.url + '/' + slugify(self.title)
        else:
            self.url = slugify(self.title)  
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.title} - ({self.parent.title})'
        return self.title
    
    class Meta:
        verbose_name = 'Поля меню'
        verbose_name_plural = 'Поля меню'
        ordering = ['menu_name']
    

