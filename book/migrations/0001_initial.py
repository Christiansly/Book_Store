# Generated by Django 3.0.8 on 2020-08-25 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='author_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('ratings', models.FloatField()),
                ('copies', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('isbn', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='book_images/')),
                ('authors', models.ManyToManyField(related_name='books', to='book.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.Publisher')),
            ],
        ),
    ]
