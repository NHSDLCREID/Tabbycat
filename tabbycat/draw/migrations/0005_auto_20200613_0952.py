# Generated by Django 2.2.9 on 2020-06-13 12:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("draw", "0004_remove_league_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="debate",
            name="flags_temp",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=15),
                choices=[
                    ("max_swapped", "Too many swaps"),
                    ("1u1d_hist", "One-up-one-down (history)"),
                    ("1u1d_inst", "One-up-one-down (institution)"),
                    ("1u1d_other", "One-up-one-down (to accommodate)"),
                    ("bub_up_hist", "Bubble up (history)"),
                    ("bub_dn_hist", "Bubble down (history)"),
                    ("bub_up_inst", "Bubble up (institution)"),
                    ("bub_dn_inst", "Bubble down (institution)"),
                    ("bub_up_accom", "Bubble up (to accommodate)"),
                    ("bub_dn_accom", "Bubble down (to accommodate)"),
                    ("no_bub_updn", "Can't bubble up/down"),
                    ("pullup", "Pull-up team"),
                ],
                blank=True,
                size=None,
                default=list,
            ),
        ),
        migrations.RunSQL(
            sql="UPDATE draw_debate SET flags_temp=string_to_array(flags, ',');",
            reverse_sql="UPDATE draw_debate SET flags=array_to_string(flags_temp, ',');",
        ),
        migrations.RemoveField(
            model_name="debate",
            name="flags",
        ),
        migrations.RenameField(
            model_name="debate",
            old_name="flags_temp",
            new_name="flags",
        ),
        migrations.AddField(
            model_name="debateteam",
            name="flags_temp",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=15),
                choices=[
                    ("max_swapped", "Too many swaps"),
                    ("1u1d_hist", "One-up-one-down (history)"),
                    ("1u1d_inst", "One-up-one-down (institution)"),
                    ("1u1d_other", "One-up-one-down (to accommodate)"),
                    ("bub_up_hist", "Bubble up (history)"),
                    ("bub_dn_hist", "Bubble down (history)"),
                    ("bub_up_inst", "Bubble up (institution)"),
                    ("bub_dn_inst", "Bubble down (institution)"),
                    ("bub_up_accom", "Bubble up (to accommodate)"),
                    ("bub_dn_accom", "Bubble down (to accommodate)"),
                    ("no_bub_updn", "Can't bubble up/down"),
                    ("pullup", "Pull-up team"),
                ],
                blank=True,
                size=None,
                default=list,
            ),
        ),
        migrations.RunSQL(
            sql="UPDATE draw_debateteam SET flags_temp=string_to_array(flags, ',');",
            reverse_sql="UPDATE draw_debateteam SET flags=array_to_string(flags_temp, ',');",
        ),
        migrations.RemoveField(model_name="debateteam", name="flags"),
        migrations.RenameField(model_name="debateteam", old_name="flags_temp", new_name="flags"),
    ]
