# Generated by Django 3.2.4 on 2021-06-20 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210619_1455'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date_and_time',
            field=models.DateTimeField(blank=True, help_text='Date and time of the recording (autofilled from CRAIG/GIARC link)', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='recording',
            field=models.CharField(blank=True, help_text='Recording link from the CDN (autofilled from CRAIG/GIARC link)', max_length=300),
        ),
    ]
