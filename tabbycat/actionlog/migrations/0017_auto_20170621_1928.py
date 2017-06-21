# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actionlog', '0016_auto_20160913_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlogentry',
            name='type',
            field=models.CharField(choices=[('ba.disc', 'Discarded ballot set'), ('ba.ckin', 'Checked in ballot set'), ('ba.crea', 'Created ballot set'), ('ba.edit', 'Edited ballot set'), ('ba.conf', 'Confirmed ballot set'), ('ba.subm', 'Submitted ballot set from the public form'), ('fb.subm', 'Submitted feedback from the public form'), ('fb.save', 'Saved feedback'), ('ts.edit', 'Edited adjudicator test score'), ('aj.note', 'Set adjudicator note'), ('aa.save', 'Saved adjudicator allocation'), ('aa.auto', 'Auto-allocated adjudicators'), ('ve.save', 'Saved a venue manual edit'), ('ve.auto', 'Auto-allocated venues'), ('dr.crea', 'Created draw'), ('dr.conf', 'Confirmed draw'), ('dr.rege', 'Regenerated draw'), ('dr.rele', 'Released draw'), ('dr.unre', 'Unreleased draw'), ('mu.save', 'Saved a matchup manual edit'), ('dv.save', 'Saved divisions'), ('mo.edit', 'Added/edited motion'), ('mo.rele', 'Released motions'), ('mo.unre', 'Unreleased motions'), ('db.im.edit', 'Edited debate importance'), ('br.aj.set', 'Changed adjudicator breaking status'), ('br.el.edit', 'Edited break eligibility'), ('br.gene', 'Generated the team break for all categories'), ('br.upda', 'Edited breaking team remarks and updated all team breaks'), ('br.upd1', 'Edited breaking team remarks and updated this team break'), ('br.rm.edit', 'Edited breaking team remarks'), ('rd.st.set', 'Set start time'), ('rd.adva', 'Advanced the current round to'), ('av.tm.save', 'Edited teams availability'), ('av.aj.save', 'Edited adjudicators availability'), ('av.ve.save', 'Edited venue availability'), ('op.edit', 'Edited tournament options')], max_length=10),
        ),
    ]
