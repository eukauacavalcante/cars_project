from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Marca')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(
        max_length=200,
        verbose_name='Modelo',
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='car_brand',
        verbose_name='Marca',
    )
    plate = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Placa',
    )
    factory_year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ano de Fabricação',
    )
    model_year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ano do Modelo',
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor',
    )
    value = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Preço',
    )
    photo = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True,
        verbose_name='Foto',
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Descrição',
    )

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarInventory(models.Model):
    cars_count = models.IntegerField(blank=True, null=True)
    cars_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # '-' para ordenar do menor para o menor

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
