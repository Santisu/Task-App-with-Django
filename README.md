# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 2

Pequeñas modificaciones:

Reflexionando, me hizo más sentido que el index_user estuviera en la app index_app en lugar de la app auth_app, por lo que fueron modificadas las vistas, reubicados los templates y editadas las urls.py para lograr esta modificación. 

Adiciones:

En esta segunda parte se agregaron los modelos correspondiente a las tareas (Task) y etiquetas (Label). Se ejecutaron las migraciones necesarias y además se habilitó la gestion del modelo Label en la administración de Django.


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
