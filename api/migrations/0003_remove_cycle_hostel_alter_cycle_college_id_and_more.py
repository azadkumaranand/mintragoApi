# Generated by Django 4.1.1 on 2022-12-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_cycle_price_alter_labdress_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='hostel',
        ),
        migrations.AlterField(
            model_name='cycle',
            name='college_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='labdress',
            name='college_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='labdress',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
