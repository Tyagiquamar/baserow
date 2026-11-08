import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0135_createusertemplatejob_make_public"),
        ("core", "0135_workspaceinvitationlink_scope"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trashentry",
            name="trash_item_owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="private_trash_entries",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
