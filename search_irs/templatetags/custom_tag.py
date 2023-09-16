from django import template
from pathlib import Path
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def get_filename(file_path: str) -> str:
    return Path(file_path).name


@register.simple_tag
def get_file_id(filename: str, files):
    for file in files:
        if Path(file['upload_file']).name == filename:
            return file.get('id')


@register.simple_tag
def truncate_bold_world(filename: str, search_word: str, files):
    for file in files:
        if Path(file['upload_file']).name == filename:
            file_text = file.get('file_content')
            replace_find_world = file_text.replace(search_word, f'<strong>{search_word}</strong>')

            def truncate_word_in_text(text, word):
                index = text.find(word)
                if index != -1:
                    start_index = max(0, index - 100)
                    end_index = min(len(text), index + len(word) + 100)
                    truncated_text = text[start_index:end_index]
                    return truncated_text
                return 'Text cant be snipped'

            return format_html(truncate_word_in_text(replace_find_world, search_word))
