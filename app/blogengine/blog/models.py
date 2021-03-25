from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))




class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug  = models.SlugField(max_length=150, blank=True ,unique=True)
    body  = models.TextField(blank=True, db_index=True)
    price = models.DecimalField(max_digits=10, default='0', decimal_places=2, verbose_name='Цена')
    color  = models.ManyToManyField('Color', blank=True, related_name='posts')
    size  = models.ManyToManyField('Size', blank=True, related_name='posts')
    item_type = models.ManyToManyField('ItemAttributes', blank=True, related_name='posts')
    tags  = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)



    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField(max_length=50, unique=True)


    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
         return '{}'.format(self.title)
    class Meta:
         ordering = ['title']

class Color(models.Model):
    color = models.CharField(max_length=50, verbose_name='Color')
    slug  = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('color_detail_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.color)
        super().save(*args, **kwargs)

    def __str__(self):
         return '{}'.format(self.color)

class Size(models.Model):
    size = models.DecimalField(max_digits=3, default='0', decimal_places=1, verbose_name='Size')
    slug  = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.size)
        super().save(*args, **kwargs)

    def __str__(self):
         return '{}'.format(self.size)





class AttributeType(models.Model):
    item_type = models.CharField(max_length=50, verbose_name='Attribute', blank=True)
    slug  = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.item_type)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('attrs_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('attrs_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('attrs_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.item_type)




class ItemAttributes(models.Model):
    size = models.CharField(max_length=50, verbose_name='Size', blank=True)
    color = models.CharField(max_length=50, verbose_name='Color', blank=True)
    label = models.CharField(max_length=50, verbose_name='Label', blank=True)

    class Meta:
        ordering = ['label']


class Coverage(models.Model):
    itemattribute = models.ManyToManyField(ItemAttributes, through='BoundTable', through_fields=('item_id', 'attribute_id'))


class BoundTable(models.Model):
    item_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_title")
    attribute_id = models.ForeignKey(AttributeType, on_delete=models.CASCADE)
