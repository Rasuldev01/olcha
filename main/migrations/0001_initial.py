# Generated by Django 3.2.4 on 2021-06-08 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('exchange_rate', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=15)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price_uzs', models.BigIntegerField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Yangi'), (1, 'Qabul qilingan'), (2, 'Bekor qilingan'), (3, "Yo'lda"), (4, 'Buyurtma yopilgan')], default=0)),
                ('payment_status', models.SmallIntegerField(choices=[(0, 'Yangi'), (2, 'Bekor qiligan'), (1, "Yo'langan")])),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.deliveryaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.topproducts')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Yangi'), (1, "Ko'rinadi"), (2, "Maderator o'tkazmadi")], db_index=True, default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.currency')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.unit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price_uzs', models.BigIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.region')),
            ],
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.district'),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.region'),
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.category')),
            ],
        ),
    ]