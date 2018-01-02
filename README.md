# cueh-bot

**Discord Example Bot**

Bot de ejemplo para Discord; este bot responde a la cadena !cueh con un 'cueh para ti @usuario'. Es un bot de ejemplo.

Requiere la librería discord.py. Que puede instalarse mediante pip.

```
$ pip install -U discord.py
```

Se ha añadido un requirements.txt para usar con pip.

```
$ pip install -r requirements.txt
```

Para poder usar el bot se requiere un token que deberá solicitarse como se indica [aquí](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token).
El token deberá ponerse en el fichero ```settings.py```.

---

## Cueh Music Bot

Segundo Discord Bot (cuehmusicbot.py) que reproduce musica desde Youtube. Requiere la libreria ```youtube-dl``` la cual puede instalarse con Pip 
```
$ pip install youtube-dl
```

Además requiere de la librería _libOpus_ que debe instalarse en su sistema Operativo.

El bot funciona de la siguiente manera. Primero debe conectarse al canal de voz donde se encuentre quien quiera escuchar con el comando ```!cueh```.

Una vez conectado ejecutar el comando _!cuehplay_ seguido de la dirección de youtube a reproducir.

Si se quiere parar su reproducción, ejecutar el comando !cuehstop o poner otra canción.
