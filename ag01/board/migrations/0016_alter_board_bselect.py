# Generated by Django 5.1.3 on 2024-12-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_alter_board_bselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('취미', '취미🎮'), ('기타', '기타🔍'), ('교통', '교통🚗'), ('사건사고', '사건사고😈'), ('웨이팅', '웨이팅👥'), ('생활/편의', '생활/편의🧼'), ('감성카페', '감성카페☕'), ('추천맛집', '추천맛집😋'), ('실시간공유', '실시간공유🗫'), ('풍경', '풍경🌴')], max_length=500),
        ),
    ]
