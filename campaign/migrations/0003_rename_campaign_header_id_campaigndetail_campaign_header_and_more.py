# Generated by Django 4.2.4 on 2023-08-16 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_campaigninquiry_campaignreview_campaignphoto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaigndetail',
            old_name='campaign_header_id',
            new_name='campaign_header',
        ),
        migrations.RenameField(
            model_name='campaigninquiry',
            old_name='campaign_header_id',
            new_name='campaign_header',
        ),
        migrations.RenameField(
            model_name='campaigninquiry',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='campaigninquiryanswer',
            old_name='campaign_inquiry_id',
            new_name='campaign_inquiry',
        ),
        migrations.RenameField(
            model_name='campaigninquiryanswer',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='campaignparticipant',
            old_name='campaign_header_id',
            new_name='campaign_header',
        ),
        migrations.RenameField(
            model_name='campaignparticipant',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='campaignphoto',
            old_name='campaign_header_id',
            new_name='campaign_header',
        ),
        migrations.RenameField(
            model_name='campaignphoto',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='campaignreview',
            old_name='campaign_header_id',
            new_name='campaign_header',
        ),
        migrations.RenameField(
            model_name='campaignreview',
            old_name='member_id',
            new_name='member',
        ),
    ]
