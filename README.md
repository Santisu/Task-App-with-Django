# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

El presente repositorio muestra los avances progresivos del proyecto, el cual consiste en crear una aplicación de multiples usuarios para guardar tareas, usando las funcionalidades CRUD que incluye el framework Django de Python.

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 6

Pequeñas modificaciones:
  - Se modificaron las vistas agregando el metodo dispatch, el cual se ejecuta ante cualquier solicitud y luego llama al metodo que requiera la solicitud, esto sirve parra poder cargar algunas variables necesarias antes de ejecutar el método correspondiente. De esta forma, el código es más limpio, pues no se hace necesario repetir el mismo codigo para obtener un determinado valor, como podría ser, por ejemplo, el usuario; siendo este valor requerido sólo en el dispatch y luego manejado como sea necesario en cada método (GET o POST).
  - El problema de ver tareas de otros usuarios se mantenía cuando se agregaba desde la url el id de un task que pertenecía a otro usuario, pudiendo incluso editarlo o eliminarlo. Ahora, en el metodo dispatch de las vistas TaskItem y TaskEdition, se agregó una verificación de que el task efectivamente corresponda al usuario logeado, en caso de no corresponder, es decir la foreign key del task no corresponde con el id del usuario logeado, se lanza un mensaje "No tienes permiso para acceder a esta tarea".
  
Adiciones:
  - Se agregó el modelo y formulario para crear observaciones a una tarea en específica, este formulario puede ser visto en la vista individual de cada tarea. Una vez hecha una observación, la observación se mostrará en la tarjeta de la tarea, teniendo la opciónn de eliminar la observación si el usuario así lo requiere.
  - Se agregó la lógica para que los botones "eliminar" y "marcar completada" de las tareas tengan efecto, esto es manejado en el metodo post de la vista TaskItem.
  - Se agregó a la página de lista de tareas una tabla que contiene sólo las tareas completadas, en caso de no haber tareas marcadas como completadas, la tabla no se muestra.

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
