# Generated by Django 3.0.4 on 2020-03-22 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medRegApp', '0006_auto_20200322_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpseeker',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medRegApp.Institution'),
        ),
    ]
