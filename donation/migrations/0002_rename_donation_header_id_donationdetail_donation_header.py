# Generated by Django 4.2.4 on 2023-08-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationdetail',
            old_name='donation_header_id',
            new_name='donation_header',
        ),
    ]
