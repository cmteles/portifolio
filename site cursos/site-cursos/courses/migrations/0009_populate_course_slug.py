from django.db import migrations
from django.utils.text import slugify
import uuid

def populate_course_slug(apps, shema_editor):
    
    Courses = apps.get_model('courses', 'Course')

    for course in Courses.objects.all():
        
        if not course.slug:
            course.slug = slugify(course.name) or str(uuid.uuid4())[:8]

            course.save()

class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0008_course_slug')
    ]

    operations = [
        migrations.RunPython(populate_course_slug)
    ]