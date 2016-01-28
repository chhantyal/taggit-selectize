#!/usr/bin/env python
import os
import sys

# Add parent dir to the PYTHON_PATH so that we can find the included version of taggit_selectize
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
