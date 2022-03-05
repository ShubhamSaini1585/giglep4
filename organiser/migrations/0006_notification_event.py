# Generated by Django 3.2 on 2022-03-05 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gig_calendar', '0002_alter_event_title'),
        ('organiser', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gig_calendar.event'),
        ),
    ]
