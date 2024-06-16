# Generated by Django 2.0.5 on 2018-06-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adjfeedback", "0003_auto_20171110_0905"),
    ]

    operations = [
        migrations.AddField(
            model_name="adjudicatorfeedback",
            name="ignored",
            field=models.BooleanField(
                default=False,
                help_text="Whether the feedback should affect the judge's score",
                verbose_name="ignored",
            ),
        ),
    ]
