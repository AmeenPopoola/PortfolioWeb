# Generated by Django 5.1.3 on 2024-11-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_portfolio_skills_used_alter_about_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=models.TextField(default=''),
        ),
    ]