# Generated by Django 5.1.3 on 2024-12-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_remove_star_star_delete_reservation_delete_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('rNo', models.AutoField(primary_key=True, serialize=False)),
                ('resPeople', models.IntegerField(default=0)),
                ('resMemo', models.TextField(default='', max_length=2000)),
                ('rDate', models.DateTimeField(auto_now=True)),
                ('res', models.ManyToManyField(default='', related_name='res_members', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('sDate', models.DateTimeField(auto_now=True)),
                ('star', models.ManyToManyField(default='', related_name='star_members', to='member.member')),
            ],
        ),
    ]
