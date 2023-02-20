# Generated by Django 4.1.7 on 2023-02-20 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UtmLink',
            fields=[
                ('utm_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=255)),
                ('campaign', models.CharField(max_length=255)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('term', models.CharField(blank=True, max_length=255, null=True)),
                ('short_id', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortIO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('short_link', models.CharField(max_length=255, unique=True)),
                ('parent_link_id', models.IntegerField(blank=True, null=True)),
                ('domain', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('link_id', models.CharField(max_length=255)),
                ('utm_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.utmlink')),
            ],
        ),
    ]