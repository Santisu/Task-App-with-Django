# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 5

Pequeñas modificaciones:
  - Se modificaron las clases de bootstrap para que las nuevas modificaciones desde el aprendizaje dos puedan ser vistas de forma correcta en dispositivos móviles.
  - Se modificó el formulario TaskCreationForm, ahora es simplemente TaskForm. Esto porque el mismo formulario puede ser usado para crear una nueva tarea o editar una tarea, por lo que el nombre podía llevar a una confusión respecto a los usos que se le daban
  
Adiciones:
  - Al filtro de tareas se le agregaron nuevas opciones como filtrar por fecha y filtrar por estado.
  - Se creó la vista, template y formulario de edición de tareas, este comparte el mismo template y formulario con la vista de creación de tareas, pero para este caso al formulario se le asigna un instance del objeto que se desea actualizar, cargando en el formulario todos los datos que tenía previamente el objeto tarea que se pretende editar.

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
