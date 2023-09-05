from django import template
from pathlib import Path

register = template.Library()


@register.simple_tag
def get_filename(file_path: str) -> str:
    return Path(file_path).name
