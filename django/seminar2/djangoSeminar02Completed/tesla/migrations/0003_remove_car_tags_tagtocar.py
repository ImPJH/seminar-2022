# Generated by Django 4.1.1 on 2022-10-03 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesla', '0002_tag_car_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='tags',
        ),
        migrations.CreateModel(
            name='TagToCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tesla.car')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tesla.tag')),
            ],
        ),
    ]
