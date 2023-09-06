from django import template
from pathlib import Path

register = template.Library()


@register.simple_tag
def get_filename(file_path: str) -> str:
    return Path(file_path).name

@register.simple_tag
def get_file_id(filename: str, files):
    for file in files:
        if Path(file['upload_file']).name == filename:
            return file.get('id')
