# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('checked_out', models.BooleanField(default=False, verbose_name='checked out')),
            ],
            options={
                'ordering': (b'-creation_date',),
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('unit_price', models.DecimalField(verbose_name='unit price', max_digits=18, decimal_places=2)),
                ('object_id', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(verbose_name='cart', to='cart.Cart')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': (b'cart',),
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
            bases=(models.Model,),
        ),
    ]
