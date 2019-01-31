import os
from django.core.exceptions import ValidationError
from zipfile import ZipFile

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    ext0 = os.path.splitext(value.name)[0]
    file_name = os.path.basename(value.name)
    valid_extensions = ['.jpg', '.jpeg', '.png', '.zip']

    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')