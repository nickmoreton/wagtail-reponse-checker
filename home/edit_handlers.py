from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.admin.edit_handlers import EditHandler


class CustomHelpPanel(EditHandler):
    template = "custom/help_panel.html"

    def render(self):
        return mark_safe(
            render_to_string(
                self.template, {"self": self, "title": self.form.parent_page.title}
            )
        )
