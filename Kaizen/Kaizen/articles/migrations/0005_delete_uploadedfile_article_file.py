# Generated by Django 4.2.7 on 2023-11-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFile',
        ),
        migrations.AddField(
            model_name='article',
            name='File',
            field=models.FileField(blank=True, default='default.pdf', upload_to=''),
        ),
    ]