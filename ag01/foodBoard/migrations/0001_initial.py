# Generated by Django 5.1.3 on 2024-12-12 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fBoard',
            fields=[
                ('bNo', models.AutoField(primary_key=True, serialize=False)),
                ('bTitle', models.CharField(max_length=200)),
                ('bSubtitle', models.CharField(max_length=200)),
                ('bContent', models.TextField(max_length=2000)),
                ('bFile1', models.ImageField(null=True, upload_to='fBoard')),
                ('bFile2', models.ImageField(null=True, upload_to='fBoard')),
                ('bFile3', models.ImageField(null=True, upload_to='fBoard')),
                ('bHit', models.IntegerField(default=0)),
                ('bLike', models.IntegerField(default=0)),
                ('bDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bNo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='foodBoard.fboard')),
            ],
        ),
    ]
