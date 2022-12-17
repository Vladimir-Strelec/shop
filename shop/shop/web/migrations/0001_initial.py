# Generated by Django 4.1.2 on 2022-12-17 13:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shop.validators.custom_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('is_active_in_filter', models.BooleanField(default=False, verbose_name='Is activ in filters')),
                ('is_active_in_bank', models.BooleanField(default=False, verbose_name='Is activ in bank')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images/%Y-%m-%d/', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('new_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='New price')),
                ('manufacturer', models.CharField(max_length=160, validators=[django.core.validators.MinLengthValidator(2), shop.validators.custom_validators.validate_only_letters], verbose_name='Manufacturer')),
                ('promotion', models.BooleanField(default=False, verbose_name='Promotion')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.usershop')),
            ],
        ),
    ]
