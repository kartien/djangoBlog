#!/bin/bash
# Definir el puerto
PORT=3000

# Imprimir el banner
echo "  _              _   _            "
echo " | | ____ _ _ __| |_(_) ___ _ __  "
echo " | |/ / _  | '__| __| |/ _ \ '_ \ "
echo " |   < (_| | |  | |_| |  __/ | | |"
echo " |_|\_\__,_|_|   \__|_|\___|_| |_|"

# Iniciar el servidor en el puerto definido
echo "Server on port $PORT"
if python manage.py runserver $PORT; then
    echo "Servidor iniciado correctamente en el puerto $PORT."
else
    echo "Error al iniciar el servidor. Por favor, verifica el código."
fi
