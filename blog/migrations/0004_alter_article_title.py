# Generated by Django 4.0 on 2021-12-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]