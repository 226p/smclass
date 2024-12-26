# Generated by Django 5.1.3 on 2024-12-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0004_alter_fboard_btime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='bTime',
            field=models.CharField(choices=[(10, '10분 이내'), (120, '2시간 이상'), (60, '1시간 이상'), (30, '30분 이내'), (45, '30분~1시간'), (0, '바로 입장')], max_length=200),
        ),
    ]
