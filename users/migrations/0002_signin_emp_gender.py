# Generated by Django 4.1.4 on 2024-03-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='emp_gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]