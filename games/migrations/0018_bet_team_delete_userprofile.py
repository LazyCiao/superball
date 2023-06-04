# Generated by Django 4.2.1 on 2023-06-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.team'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
