# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 2

Pequeñas modificaciones:

Se editó el nombre de las foreing_key del modelo task, pues agregarles el sufijo "_id" hacia que fuese redundante, pues django les otorga ese sufijo automaticamente a las foreign key al momento de ejecutar las migraciones, por ejemplo: el campo de user en la tabla de task en la  DB se llamaba "user_id_id", y eliminando el sufijo "_id" del modelo ahora se llama simplemente "user_id"

Adiciones:
  - Se agregaron un total de 5 etiquetas desde el administrador de django.
  - Se agregó la vista,template y url para mostrar la lista de tareas pendientes del usuario, de igual forma se incluyó el botón para agregar tareas, sin funcionalidad por ahora.
  - Se creo la vista, template y url para poder ver una tarea en específico, así como tambien se agregaron los botones para poder editar, completar o eliminar (este con un modal de confirmación), sin embargo la funcionalidad todavía no se incluye pues esos son requisitos de los próximos aprendizajes 

De momento, el usuario admin tiene tareas precargadas para poder ver una vez logeado.

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
