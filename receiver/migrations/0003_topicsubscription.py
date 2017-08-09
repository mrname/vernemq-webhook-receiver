# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0002_remove_mqttaction_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('qos', models.IntegerField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='receiver.MQTTAction')),
            ],
        ),
    ]