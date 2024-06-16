# Generated by Django 2.0.8 on 2018-09-20 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adjallocation", "0004_add_teaminstitutionconflict"),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO adjallocation_teaminstitutionconflict (team_id, institution_id) SELECT id, institution_id FROM participants_team WHERE institution_id IS NOT NULL ON CONFLICT DO NOTHING;",
            migrations.RunSQL.noop,
            elidable=True,
        ),
    ]
