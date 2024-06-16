# Generated by Django 2.0.2 on 2018-03-08 06:17

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ("availability", "0004_auto_20180305_1544"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roundavailability",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=django.db.models.query_utils.Q(
                    django.db.models.query_utils.Q(
                        ("app_label", "participants"), ("model", "team"), _connector="AND"
                    ),
                    django.db.models.query_utils.Q(
                        ("app_label", "participants"), ("model", "adjudicator"), _connector="AND"
                    ),
                    django.db.models.query_utils.Q(
                        ("app_label", "venues"), ("model", "venue"), _connector="AND"
                    ),
                    _connector="OR",
                ),
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.ContentType",
                verbose_name="content type",
            ),
        ),
    ]
