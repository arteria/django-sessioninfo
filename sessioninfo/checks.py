# -*- coding: utf-8 -*-

# from django.core.checks import register, Warning

"""
To run checks for this app, install "ar-healthchecks" and run "manage.py check sessioninfo"
"""

"""
A list of apps that need to be listed in INSTALLED_APPS.
Checks raise an error if a dependency is missing
"""
CHECK_INSTALLED_APPS = [
    # 'some_dependency',
]

"""
A list of settings that need to be explicitly set in the project's settings.py.
Checks raise an error if a setting is missing
"""
REQUIRED_SETTINGS = [
    # 'FAVORITE_FOOD',
]

"""
A list of path settings which need to be set to writeable paths (e.g. pdf directories).
Checks raise an error if a path is not writeable
"""
WRITEABLE_PATHS = [
    # 'PDF_DIR',
]

"""
Non-python executables which need to be installed for this app to work properly.
Checks raise an error if a dependency is missing
"""
NON_PYTHON_DEPENDENCIES = [
    # 'ruby',
]

"""
Place custom check functions below
"""

# @register()
# def example_check(app_configs, **kwargs):
#     warnings = []
#     # ... your check logic here
#     warnings.append(
#         Warning(
#             'an warning',
#             id='myapp.W001',
#         )
#     )
#     return warnings