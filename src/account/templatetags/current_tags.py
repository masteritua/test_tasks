import datetime
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def render_link(context, target_model=None):
    def add_link(cls):
        reverse_name = target_model or cls.model.__name__.lower()

        def link(self, instance):
            app_name = instance._meta.app_label
            reverse_path = "admin:%s_%s_change" % (app_name, reverse_name)
            link_obj = instance
            url = reverse(reverse_path, args=(link_obj.id,))

            return mark_safe("<a href='%s'>%s</a>" % (url, link_text(link_obj)))

        link.allow_tags = True
        link.short_description = reverse_name + ' link'
        cls.link = link
        cls.readonly_fields = list(getattr(cls, 'readonly_fields', [])) + ['link']

        return cls

    return add_link
