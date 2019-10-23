# Generated by Django 2.2.6 on 2019-10-18 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_auto_20191018_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailers',
        ),
        migrations.AddField(
            model_name='trailer',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Movie'),
        ),
    ]