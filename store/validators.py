from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 500
    if file.size > max_size * 1024:
            raise ValidationError(f'File size cant be larger than {max_size}kb!')
        