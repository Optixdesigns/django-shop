from django.template.loaders import filesystem, app_directories
from djaml.loaders import get_haml_loader

# Quickfix see: https://github.com/chartjes/djaml/issues/12
DjamlFilesystemLoader = get_haml_loader(filesystem)
DjamlAppDirectoriesLoader = get_haml_loader(app_directories)