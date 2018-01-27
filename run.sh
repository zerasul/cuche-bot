#!/bin/bash
# Script ejecución de Cueh-Bot.
# Se requiere instalar python3.4 o superior.
# Antes de poder ejecutar este script hay que instalar las dependencias con pip.
# $ pip install -r requirements
command=$1
echo $command
case $command in
  'install')
    echo 'Instalando cueh-bot'
    pip install -r requirements
    ;;
  'run')
    echo 'Iniciando cueh-bot, cueh'
    python3 cuehmusicbot.py 
    ;;
    *)
    echo 'Indica el comando (install,run): \n sh run.sh install para instalar el bot,\n sh run.sh para iniciarlo'
    ;;
esac
