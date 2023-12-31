# Generated by Django 4.2.2 on 2023-06-09 12:35

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'AUTHOR_INFO',
            },
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('salary', models.IntegerField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onetoonerel.author')),
            ],
            options={
                'db_table': 'PERSONAL_INFO',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=30)),
                ('author', models.ManyToManyField(related_name='library', to='onetoonerel.author')),
            ],
            options={
                'db_table': 'LIBRARY_INFO',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='onetoonerel.author')),
            ],
            options={
                'db_table': 'BOOK_INFO',
            },
        ),
    ]
