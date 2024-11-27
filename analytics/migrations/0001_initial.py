# Generated by Django 5.1.3 on 2024-11-27 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=250, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=250, null=True)),
                ('ip_add', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]