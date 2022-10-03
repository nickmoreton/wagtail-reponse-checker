from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, RichTextFieldPanel,
                                         StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from home.edit_handlers import CustomHelpPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        RichTextFieldPanel("body"),
    ]


class StandardPage(Page):
    body = RichTextField(blank=True)
    story = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        CustomHelpPanel(),
        RichTextFieldPanel("body"),
        StreamFieldPanel("story"),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        RichTextFieldPanel("intro"),
    ]

    subpage_types = ["BlogPage"]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        RichTextFieldPanel("body"),
    ]

    parent_page_types = ["BlogIndexPage"]
