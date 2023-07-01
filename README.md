# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 3

Pequeñas modificaciones:
  - Se modificó el campo due_date del modelo Task, ya que no se implementaba bien al momento de querer agregar una fecha y hora en el formulario de creación de tareas, ahora funciona de forma correcta, además se agregó el atributo "null=True" para poder elegir la opción de no ponerle una fecha límite.
  - Me encontré con el problema de que no sólo se mostraban las tareas del usuario que estuviese usando la aplicación, sino que también las de otros usuarios. Se pudo corregir facilmente especificando algunas variables en la vista de tasks_list.
  - Se importó "Q" de django en las vistas, que sirve para poder encapsular filtros para poder usar los condicionales logicos "and" y "or", esto para poder mostrar no sólo las tareas pendientes sino que tambien las tareas en progreso, que, a fin de cuentas, siguen estando pendientes hasta no ser completadas.
  
Adiciones:
  - Se creó el filtro de tareas por etiqueta, al seleccionar un filtro en específico se mostrarán solo las tareas que correspondan a dicho filtro, en caso de no haber tareas con la etiqueta se muestra un mensaje pintorezco indicando que no hay tareas pendientes con dicha etiqueta.
  - Se creó la vista, template y formulario de creación de tareas, a la que se puede acceder desde el listado de tareas pendientes. Es totalmente funcional y se pueden agregar nuevas tareas y persistir el registro con cualquier usuario sin problema.
  - Se agregó la vista de editar tareas, por ahora está comentada para poder ser entregada más adelante.


# Usuarios

<table>
  <thead>
    <th>Username</th>
    <th>Contraseña</th>
    <th>Clase</th>
  </thead>
  <tbody>
    <tr>
      <td>admin</td>
      <td>123</td>
      <td>Superuser</td>
    </tr>
    <tr>
      <td>usuario1</td>
      <td>contrasena2023</td>
      <td>Usuario</td>
    </tr>
    <tr>
      <td>usuario2</td>
      <td>contrasena2023</td>
      <td>Usuario</td>
    </tr>
  </tbody>
</table>
