# Generated by Django 4.2.6 on 2023-11-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_tagposts_alter_women_cat_women_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads')),
            ],
        ),
    ]