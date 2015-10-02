# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='accessories/')),
                ('season', models.CharField(default='All', choices=[('Summer', 'Summer'), ('Winter', 'Winter'), ('Rainy', 'Rainy'), ('All', 'All')], max_length=7)),
                ('occasion', models.CharField(default='Party', choices=[('Informal', 'Informal/Casuals'), ('Work', 'Work'), ('Sport', 'Sport'), ('Party', 'Party')], max_length=10)),
                ('category', models.CharField(default='Top', choices=[('HandBag', 'Handbag'), ('Clutches', 'Clutches'), ('Broche', 'Broche'), ('Wallet', 'Wallet'), ('Belt', 'Belt'), ('Hat', 'Hat'), ('SunGlasses', 'SunGlasses'), ('Scarf', 'Scarf'), ('Bracelet', 'Bracelet'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Earing', 'Earing'), ('Watch', 'Watch'), ('Gloves', 'Gloves'), ('Sandals', 'Sandals'), ('Shoes', 'Shoes'), ('Bellies', 'Bellies')], max_length=15)),
                ('hash_tag', models.CharField(null=True, max_length=32, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='accessories')),
            ],
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='dresses/')),
                ('season', models.CharField(default='All', choices=[('Summer', 'Summer'), ('Winter', 'Winter'), ('Rainy', 'Rainy'), ('All', 'All')], max_length=7)),
                ('occasion', models.CharField(default='Work', choices=[('Informal', 'Informal/Casuals'), ('Work', 'Work'), ('Sport', 'Sport'), ('Party', 'Party')], max_length=10)),
                ('color', colorful.fields.RGBColorField(null=True, blank=True)),
                ('hash_tag', models.CharField(null=True, max_length=32, blank=True)),
                ('at_laundry', models.BooleanField(default=False)),
                ('wear_on', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DressCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('parent_category_id', models.ForeignKey(to='wardrobe.DressCategory', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, blank=True)),
                ('accessories_needed', models.ManyToManyField(to='wardrobe.Accessory')),
                ('dress_components', models.ManyToManyField(to='wardrobe.Dress')),
            ],
        ),
        migrations.CreateModel(
            name='Wardrobe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tops_count', models.IntegerField(default=0)),
                ('lowers_count', models.IntegerField(default=0)),
                ('singlePieces_count', models.IntegerField(default=0)),
                ('outfits_count', models.IntegerField(default=0)),
                ('accessories_count', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dress',
            name='category',
            field=models.ForeignKey(to='wardrobe.DressCategory'),
        ),
        migrations.AddField(
            model_name='dress',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='outfits'),
        ),
        migrations.AddField(
            model_name='dress',
            name='wardrobe',
            field=models.ForeignKey(to='wardrobe.Wardrobe', null=True, related_name='dresses'),
        ),
    ]
