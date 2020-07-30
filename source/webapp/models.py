from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES=(
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питание'),
    ('household', 'Хоз.товары'),
    ('toys', 'Детские игрушки'),
    ('electronics', 'Бытовая техника')
)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='описание')

    category = models.CharField(max_length=20, verbose_name='категория',
                                choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    amount = models.IntegerField(verbose_name='остаток')
    price = models.DecimalField(verbose_name='цена', max_digits=7, decimal_places=2)

    def __str__(self):
        return  f'{self.name} - {self.amount}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'