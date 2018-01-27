rem Script windows para cueh-Bot. Se requiere instalar las dependencias anteriores con el fichero requirements.txt
command=%1
IF "%command"=="install" pip install -r requirements.txt & goto exit
IF "%command"=="run" python3 cuehmusicbot.py & goto exit

echo "Seleccionar comando run.bat (install,run): \n install - instala las dependencias con pip. \n run -  ejecuta el bot. \n NOTA: Se requiere python 3.4 o superior."

:exit