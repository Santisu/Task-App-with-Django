# Modulo-7-Acceso-a-datos-en-aplicaciones-Django

Esteban Santibáñez B

Cada entrega se separará en ramas con el nombre del aprendizaje al que corresponde la entrega, manteniendose en el main el progreso principal.

# Entregable 1

Para este proyecto escalable se crearon, por el momento, 3 aplicaciones con diferentes funciones:

- auth_app: esta app contendrá toda la lógica, modelos y views que sean necesarios para poder registrarse, hacer login y logout. Además de contener el index al que es redirigido el usuario al momento de autenticarse
- index_app: esta app contiene la página de inicio y todo su contenido, además también almacena la plantilla base del programa en general y sus statics comunes
- task_app: esta es la app que contendrá toda la lógica, modelos y vistas necesarias para manejar el propósito principal del programa

Para la base de datos se está usando PostgreSQL, sin embargo, en lugar de conectarse a una base de datos local almacenada en mi computador personal, se está usando una base de datos creada de manera gratuita en la pagina web <a href="https://render.com/" target="_blank">Render</a>, a pesar de que quizá tarde en devolver las peticiones, por el hecho de ser gratuita y de recursos limitadísimos, el acceso a una base de datos externa ayudará en la revisión del correcto funcionamiento del proyecto, actualmente tengo acceso a esta base de datos desde el pgadmin de igual forma. Por favor, no alterar la base de datos, con abstenerse de realizar migraciones sin mi consentimiento debería ser suficiente, muchas gracias.

Finalmente, en este repositorio de github estará el proyecto completo de este módulo, el que se irá actualizando a medida que avance en los ejercicios de cada aprendizaje. 

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
