# Proyecto para probar Django

#### Instalación

- Las pruebas se van a realizar sobre Docker. Un contenedor con el proyecto de Django, y otro almacenando la bbdd,
que en este caso será PostgreSQL. Ver <https://github.com/dmsergio/django_postgresql> para más info.

#### Creando la primera app dentro del proyecto: Blog

Situado en la raíz del proyecto, __mysite__ en este caso, aplicar el siguiente comando para crear la app __blog__.

`python manage.py startapp blog`

Con ello se consigue crear una nueva estructura de directorios llamada __blog__ dentro de la raíz del proyecto.

```
misite/
    blog/
        admin.py  # donde se registran los modelos para incluirlos en el sitio de administración de Django
        apps.py  # incluye la principal configuración de la app blog
        migrations/  # contiene las migraciones de la bbdd para estar sincronizada con los modelos definidos
            __init__.py
        models.py  # incluye los datos de los modelos para la aplicación blog
        tests.py  # se alojan los tests para la aplicación
        views.py  # toda la lógica de la aplicación estará contenida aquí
```

Antes de continuar agregando modelos y lógica a la aplicación, es necesario decirle a Django que se ha creado una nueva
aplicación para que esté disponible. Para ello en el fichero `mysite/mysite/settings.py` hay que agregar en el parámetro
__INSTALLED_APPS__ el siguiente valor: `blog.apps.BlogConfig`. El valor indicado se trata de la clase contenida en
`mysite/blog/apps.py`.

#### Crear y aplicar migraciones

Las migraciones son necesarias para reflejar los modelos implementados en la bbdd. Es decir, que cada vez que se creen
nuevos modelos a la aplicación, o se agreguen/actualicen/eliminen campos en dichos modelos, hay que preparar una migración
para actualizar la bbdd.

__Comandos principales__:

- `python manage.py makemigrations blog`: Genera un fichero en la carpeta migrations de la aplicación, con las instrucciones
necesarias para poder aplicar la migración.

- `python manage.py sqlmigrate blog <nombre_fichero_migracion>`: Genera la instrucción SQL que será ejecutada internamente
en el gestor de la bbdd configurado en el proyecto. Este comando no es obligatorio, simplemente es para poder visualizar
la instrucción SQL generada a raíz del fichero de migración creado con la sentencia anterior.

- ``python manage.py migrate``: Aplica la migración sobre la bbdd.

#### Crear un sitio de administración para los nuevos modelos definidos

Se puede acceder al sitio de administración en <ip_server_django:puerto/admin>.

Es necesario crear el superusuario del sitio de administración para poder acceder a él. Para ello aplicar el siguiente
comando:

``python manage.py createsuperuser``

Para agregar los modelos deseados al sitio de administración, hay que editar el fichero ``mysite/blog/admin.py`` y registrar
el modelo deseado como se muestra a continuación:

```
from django.contrib import admin
from .models import Post

admin.site.register(<nombre_del_modelo>)
```

Con ello se podrá administrar el modelo deseado en el sitio de administración.


#### Django API: Shell

- `python manage.py shell`: Ejecuta la shell de Django.
- `Model.objects.all()`: Obtiene todos los registros del modelo.
- `Model.objects.get(pk=<id>)`: Espera obtener un único registro del modelo en base a la condición. Se lanzará una
excepción en caso de no obtener ninguno o más de un registro.
- `record = Model(field_1='', field_2='', ...)`: Crear un nuevo registro. La creación del registro no será persistente
en la bbdd hasta que no se invoque explícitamente `record.save()`.
- `Model.objects.create(field_1='', field_2='', ...)`: Crea y guarda en la bbdd el registro.
- `Model.objects.filter(<condition>)`: Obtiene todos los registros del modelo que cumplan la/las condición/es indicada/as.
- `Model.objects.filter(<condition>).exclude(<condition>)`: Con el método _exclude()_ es posible excluir de un recordset
previamente filtrado en función de la condición establecida.
- `Model.objects.order_by('<->field_to_order')`: Obtiene los registros ordenados por el campo o campos indicados.
- `object.delete()`: Elimina el registro.


![Django flow](/Users/sergio/Projects/django/mysite/images/django_flow.jpg?raw=true "Django flow")
