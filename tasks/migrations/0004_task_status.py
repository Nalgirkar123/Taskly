# Generated by Django 4.2.20 on 2025-05-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_category_emoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('incomplete', 'Incomplete ❌'), ('ongoing', 'Ongoing 🔄'), ('complete', 'Completed ✅')], default='incomplete', max_length=20),
        ),
    ]
