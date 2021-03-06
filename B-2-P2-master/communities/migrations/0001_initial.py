# Generated by Django 3.2.3 on 2021-05-31 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='community/community_name/%Y/%m/%d/')),
                ('description', models.TextField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=480)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'Random'), (1, 'Movie'), (2, 'Music'), (3, 'News'), (4, 'Celebrity'), (5, 'TV Shows'), (6, 'Games'), (7, 'General'), (8, 'Business'), (9, 'Sports'), (10, 'Academic'), (11, 'Social')], default=0)),
                ('member', models.ManyToManyField(blank=True, related_name='member', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
