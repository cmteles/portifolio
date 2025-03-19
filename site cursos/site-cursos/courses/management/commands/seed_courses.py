from django.core.management.base import BaseCommand

from courses.models import Course

class Command(BaseCommand):
    ##
    help = 'Seed para cadastrar registro na tabela courses'

    def handle(self, *args, **kwargs):


        description = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in venenatis enim. Sed euismod, urna eu tincidunt consectetur, nisi nisl aliquam eros, a bibendum libero sapien nec justo.</p><h2>Subtítulo</h2><p>Curabitur vel urna nec justo bibendum fermentum. Proin ac orci ac libero tincidunt tincidunt. Integer non felis nec nulla facilisis tincidunt.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><p>Phasellus sit amet sapien nec arcu vehicula fermentum. Nulla facilisi. Donec auctor, justo at tincidunt vehicula, libero justo cursus odio, nec tincidunt felis eros nec justo.</p>"

        courses = [
            {
            'name': 'Curso de Python 2',
            'original_price': 997.43,
            'discounted_price': 229.90,
            'description': description,
        },

        {
            'name': 'Curso de Python 3',
            'original_price': 879.80,
            'discounted_price': 349.90,
            'description': description,
        },

        {
            'name': 'Curso de Django 2',
            'original_price': 599.80,
            'discounted_price': 189.90,
            'description': description,
        }

        
        ]

        for course_data in courses:

            Course.objects.update_or_create(
                name=course_data['name'],
                defaults=course_data
            )

        self.stdout.write(self.style.SUCCESS('Cursos adicionados com sucesso!'))