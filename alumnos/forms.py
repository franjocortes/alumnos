from django.forms import *

from alumnos.models import Alumno


class AlumnoForm(ModelForm):

    class Meta:
        model = Alumno
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del alumno',
                }
            ),
        }