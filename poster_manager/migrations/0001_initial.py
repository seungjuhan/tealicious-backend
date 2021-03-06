# Generated by Django 2.0.2 on 2018-02-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_event', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_host', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
                ('events', models.ManyToManyField(to='poster_manager.Event')),
                ('hosts', models.ManyToManyField(to='poster_manager.Host')),
                ('image', models.ManyToManyField(to='poster_manager.Image')),
            ],
        ),
    ]
