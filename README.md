# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

El presente repositorio muestra los avances progresivos del proyecto, el cual consiste en crear una aplicación de multiples usuarios para guardar tareas, usando las funcionalidades CRUD que incluye el framework Django de Python.

# Sprint Final

Pequeñas modificaciones:
  - Se corrigió el redireccionamiento del login en caso de ingresar un usuario o contraseña erronea, el nombre del template que cargaba estaba mal escrito.
  
Adiciones:
  - Se editó el TaskForm para que las tareas puedan ser asignadas a un usuario diferente a quien realiza el request, siendo este señalado por el usuario en cuestión.
  - Se creó el modelo de Priority, agregandolo a la administración de Django para poder agregar registros de prioridades.
  - Se agregó el campo priority al modelo Task el cual se relaciona como foreign key con el modelo Priority, se asignó el valor null y blank para que no hubiese incongruencia con las task creadas previamente a la adición de este campo.
  - En la visualización de cada tarea individua, se agregó una tarjeta que indica la prioridad, cambiando el color y la animación en relación a la urgencia.
  - Se agregó la columna correspondiente a prioridades en la columna listado.
  - Además, se agregó la vista y template de registro de usuario para que se puedan registrar nuevos usuarios. También se agregó en el index del usuario el despliegue de tarjetas con las tareas pendientes que tenga.

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
