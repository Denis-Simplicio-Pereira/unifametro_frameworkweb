# Generated by Django 4.1.6 on 2023-02-25 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('ovino', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovino',
            name='tag',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tag.tag'),
        ),
    ]
