from django.core.exceptions import ValidationError


def validate_only_letters(value):
    name = ''
    for ch in value:
        name += ch
        if len(name) == 1 and name[0].isdigit():
            raise ValidationError('Name cannot start with numbers')