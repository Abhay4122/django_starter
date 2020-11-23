import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'python manage.py rename_project <current> <new>'

    def add_arguments(self, parser):
        parser.add_argument('current', type=str, nargs='+', help='The current Django project name')
        parser.add_argument('new', type=str, nargs='+', help='The new Django project name')
    
    def handle(self, *args, **kwargs):
        current_project_name = kwargs['current'][0]
        new_project_name = kwargs['new'][0]

        # logic for rename the Files

        files_to_rename = [
            f'{current_project_name}/settings.py',
            f'{current_project_name}/wsgi.py',
            f'{current_project_name}/asgi.py',
            f'{current_project_name}/urls.py',
            'manage.py'
        ]

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace(current_project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)
                
        os.rename(current_project_name, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been rename to %s' % new_project_name))
