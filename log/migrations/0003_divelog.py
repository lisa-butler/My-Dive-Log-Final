# Generated by Django 3.2.15 on 2022-09-09 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0002_item_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiveLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DiveLog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
