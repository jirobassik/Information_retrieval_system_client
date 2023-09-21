import re

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
def truncate_bold_world(filename: str, search_words: list, files):
    for file in files:
        if Path(file['upload_file']).name == filename:
            file_text = file.get('file_content')

            def truncate_word_in_text(text: str, words: str):
                lower_text = text.lower()
                replaced_text = text
                for word in words.split(" "):
                    lower_word = word.lower()
                    index = lower_text.find(lower_word)

                    if index != -1:
                        start_index = max(0, index - 100)
                        end_index = min(len(lower_text), index + len(word) + 100)
                        pattern = re.compile(re.escape(word), re.IGNORECASE)
                        replaced_text = pattern.sub(f'<strong>{text[index:index + len(lower_word)]}</strong>',
                                                    replaced_text)
                        replaced_text = replaced_text[start_index:end_index]

                if replaced_text != text:
                    return replaced_text

                return 'Text cannot be snipped'

            return format_html(truncate_word_in_text(file_text, search_words))
