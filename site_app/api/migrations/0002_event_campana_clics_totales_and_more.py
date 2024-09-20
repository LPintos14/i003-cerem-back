# Generated by Django 5.1.1 on 2024-09-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='campana',
            name='clics_totales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campana',
            name='conversiones_totales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campana',
            name='google_calendar_event_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='campana',
            name='google_keep_note_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
