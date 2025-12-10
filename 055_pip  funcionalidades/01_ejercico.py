"""
La aplicación pip es la herramienta fundamental que trae Python para la instalación de paquetes para poder utilizarlos en nuestros proyectos.

Vimos en el concepto anterior la sintaxis que se requiere para instalar un paquete que se encuentra publicado en el sitio pypi.org:

pip install [nombre del paquete]
La actividad inversa de instalar un paquete en nuestro equipo se hace indicando el comando 'uninstall', por ejemplo si queremos desintalar el paquete 'wxPython' que instalamos en el concepto anterior lo hacemos con la siguiente sintaxis:

pip uninstall wxPython
pip uninstall
Debemos ingresar la letra 'y' para confirmar la eliminación del paquete.

Si queremos conocer todos los archivos que tiene un paquete que hayamos instalado lo hacemos mediante la sintaxis:

pip show --files wxPython
Esto nos muestra una lista completa de archivos que contiene el paquete:

pip show --files
Hay una sintaxis resumida para la misma actividad:

pip show -f wxPython
Para conocer todos los paquetes instalados en nuestro entorno de Python debemos utilizar el comando 'list':

pip list
pip list
Como podemos ver en el listado de paquetes además del paquete que instalamos en el concepto anterior hay otros que vienen por defecto cuando instalamos Python.

Los desarrolladores de paquetes para Python están constantemente actualizando sus funcionalidades y sacan nuevas versiones. Si queremos saber si alguno de nuestros paquetes está desactualizado podemos ejecutar el comando list pasando el parámetro --outdated (se nos muestran todos los paquetes desactualizados):

pip list --outdated
Si por alguna razón queremos instalar una versión más vieja de un paquete debemos indicar en el comando 'install' la versión del mismo:

pip install wxPython==4.0.2
Indicamos el número exacto de versión a instalar.

Para actualizar un paquete ya instalado debemos pasar el parámetro 'upgrade':

pip install --upgrade wxPython

"""