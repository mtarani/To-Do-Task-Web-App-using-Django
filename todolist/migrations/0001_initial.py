# Generated by Django 2.1.7 on 2019-03-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=250)),
                ('due_time', models.DateField(verbose_name='%m/%d/%Y %H:%M:%S')),
            ],
            options={
                'ordering': ['-due_time'],
            },
        ),
    ]