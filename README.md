# Wagtail -> Response Checker

Admin and frontend page response checker

- [branch 216 is the original v2.16.2 site](https://github.com/nickmoreton/wagtail-response-checker/tree/216)
- [branch 300 is the site convered to v3.0.3](https://github.com/nickmoreton/wagtail-response-checker/tree/300) But a required change was missed

## `Live` testing scenario

*If you run check_responses command on this branch it will not show any errors*

Wagtail 3 has had some extensive changes over previous verions: [Documentation](https://docs.wagtail.org/en/stable/releases/3.0.html)

Mostly, if you miss renaming an import it can be seen quite quickly when running the site. But some other changes can be hard to spot. E.G.

```python
class CustomHelpPanel(EditHandler):
  template = 'toolkits/custom_help_panel.html'

  def render(self):
    return mark_safe(render_to_string(self.template, {
      'self': self,
        'title': self.form.parent_page.title
    }))
```

Won't show up as an error until you try to edit the page it's used on.

If you have one page model that all pages use/inherit from where the above is used like so:

```python
content_panels = [CustomHelpPanel()] + Page.content_panels + [
    ...
]
```

I dare say you will spot it quickly. But you might just have 1000's of pages to potentially check across 10's of different page models.

### Check Responses Command

`check_responses.py` can be dropped into any app folder as per the django management command folder stucture and run with `./manage.py check_responses`

Your site will need some content, preferably close to the same content as your live or staging site and will need to be running: `python manage.py runserver`

## Don't commit the check_responses file and end up deploying it! (suggestion)

It's really only useful during development and testing.
