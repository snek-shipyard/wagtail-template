# Generated by Django 2.2 on 2020-10-27 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("wagtailcore", "0052_pagelogentry"),
        ("images", "0001_initial"),
        ("utils", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="snekimage",
            name="license",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="utils.LicenseSnippet",
            ),
        ),
        migrations.AddField(
            model_name="snekimage",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text=None,
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="snekimage",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AddField(
            model_name="snekachievementimage",
            name="collection",
            field=models.ForeignKey(
                default=wagtail.core.models.get_root_collection_id,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.Collection",
                verbose_name="collection",
            ),
        ),
        migrations.AddField(
            model_name="snekachievementimage",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text=None,
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="snekachievementimage",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AddField(
            model_name="rendition",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="renditions",
                to="images.SNEKImage",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rendition",
            unique_together={("image", "filter_spec", "focal_point_key")},
        ),
    ]