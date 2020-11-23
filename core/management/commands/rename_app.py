import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'python manage.py rename_app <project> <current> <new>'

    def add_arguments(self, parser):
        parser.add_argument('project', type=str, nargs='+', help='The current Django project folder name')
        parser.add_argument('current', type=str, nargs='+', help='The current Django app folder name')
        parser.add_argument('new', type=str, nargs='+', help='The new Django app name')
    
    def handle(self, *args, **kwargs):
        current_project_name = kwargs['project'][0]
        current_app_name = kwargs['current'][0]
        new_app_name = kwargs['new'][0]

        # logic for rename the Files

        files_to_rename = [
            f'{current_app_name}/admin.py',
            f'{current_app_name}/apps.py',
            f'{current_project_name}/settings.py',
            f'{current_project_name}/urls.py',
        ]

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace(current_app_name, new_app_name)

            with open(f, 'w') as file:
                file.write(filedata)
                
        os.rename(current_app_name, new_app_name)

        self.stdout.write(self.style.SUCCESS(f'app has been rename to {new_app_name}'))
