# Generated by Django 4.0.3 on 2023-06-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_answer_modify_count_question_modify_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
