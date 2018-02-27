# Generated by Django 2.0.2 on 2018-02-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='poster',
            name='image',
        ),
        migrations.AddField(
            model_name='poster',
            name='image',
            field=models.ManyToManyField(to='poster_manager.Image'),
        ),
    ]