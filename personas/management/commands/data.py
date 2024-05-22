from typing import Any
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import persona

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        fake= Faker()
        value_counter= int(persona.objects.count())
        if value_counter<100:
            
            self.stdout.write(self.style.SUCCESS('Base de datos esta vacía.'))
            for i in range(value_counter,100):
                nombre = fake.first_name()
                apellido = fake.last_name()
                celular = fake.numerify(text='##########')
                correo = fake.email()
                personas = persona(nombre=nombre, apellido=apellido, celular=celular,correo=correo)
                personas.save()
            self.stdout.write(self.style.SUCCESS('Persona creada.'))
        else:
            self.stdout.write(self.style.SUCCESS('Base de datos no esta vacía.'))        
                
