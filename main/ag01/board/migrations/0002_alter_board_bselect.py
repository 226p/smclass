# Generated by Django 5.1.4 on 2024-12-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('기타', '기타🔍'), ('취미', '취미🎮'), ('사건사고', '사건사고😈'), ('실시간공유', '실시간공유🗫'), ('교통', '교통🚗'), ('풍경', '풍경🌴'), ('추천맛집', '추천맛집😋'), ('생활/편의', '생활/편의🧼'), ('웨이팅', '웨이팅👥'), ('감성카페', '감성카페☕')], max_length=500),
        ),
    ]
