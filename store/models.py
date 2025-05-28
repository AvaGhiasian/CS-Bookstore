from django.conf import settings
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="دسته بندی")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="اسلاگ")

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name="نویسنده")
    bio = models.TextField(blank=True, verbose_name="بایو")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسنده ها"

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE, verbose_name='دسته بندی')
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ')
    description = models.TextField(max_length=1200, verbose_name='توضیحات')
    available = models.BooleanField(default=True)
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')
    page_num = models.PositiveIntegerField(default=0, verbose_name="تعداد صفحات")
    publish_date = models.DateTimeField(verbose_name="تاریخ انتشار")

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:book_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title


class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images", verbose_name="کتاب")
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")
    title = models.CharField(max_length=250, verbose_name="عنوان", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews", verbose_name="کتاب")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="کاربر")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="امتیاز")
    body = models.TextField(verbose_name="متن نظر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    active = models.BooleanField(default=False, verbose_name="فعال")

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.user}: {self.book}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="کاربر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت سفارش")
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"

    def __str__(self):
        return f"order {self.id} by {self.user}"
