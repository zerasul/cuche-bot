import discord
import settings
import datetime as DT
import random
import cuehchistescontroller
from discord.ext import commands

discord.opus.load_opus('libopus.0.dylib')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='Reproduce musica desde youtube')

class Cueh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.chistecontroller = cuehchistescontroller.ChisteController()
        self.playlist = []
        self.current = 0

    async def join_channel(self,voicechannel):
        self.voice = await self.bot.join_voice_channel(voicechannel)
        pass
    @commands.command()
    async def cueh(self, ctx, channel: discord.VoiceChannel):
       
        print('Conectando a {}'.format(channel))
        if voice_channel is None:
            await self.show_message('Primero Conectate a un canal de voz, Cueh', mtts=False)
        else:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command(pass_context=True, no_pm=True)
    async def cuehplay(self, ctx, urlsong):
        if self.voice is None:
            await self.show_message("Primero conectate a un canal de Voz, Cueh", mtts=False)
        if self.player is not None:
            if not self.player.is_done():
                await self.show_message("Parando {}".format(self.player.title), mtts=False)
                self.player.stop()
        print("Reproduciendo {}".format(urlsong))
        self.player = await self.voice.create_ytdl_player(urlsong)
        msg = "Reproduciendo {}, cueh".format(self.player.title)
        await self.show_message(msg, mtts=False)
        self.player.start()
        pass

    @commands.command(pass_context=True, no_pm=True)
    async def cuehclean(self,ctx):
        today = DT.date.today()
        date_week= today - DT.timedelta(days = 7)
        current_channel=ctx.message.channel
        await bot.purge_from(channel=current_channel,before=date_week,limit=settings.message_limit)
        pass

    @commands.command(pass_context=True, no_pm=True)
    async def cuehlist(self,ctx):
        if not self.playlist:
            await  self.show_message("La Lista esta vacia; utiliza el comando cuehadd para añadir una cancion")
        else:
            i = 0
            msg = ""
            for song in self.playlist:
                msg += "{}.- {}\n".format(i+1, song)
                i += 1
            msg += "\nCurrent Song: {}\n".format(self.current+1)
            await self.show_message(msg)

    @commands.command(pass_context=True, no_pm=True)
    async def cuehadd(self, ctx, url):
        self.playlist.append(url)
        if self.player is None or self.player.is_done():
            await self.playsong(url)

    @commands.command(pass_context=True, no_pm=True)
    async def cuehaddlist(self, ctx, slist):
        songlist = slist.split(",")
        print(songlist)
        for s in songlist:
            self.playlist.append(s)
        await self.show_message("Añadidas {} Canciones".format(len(songlist)))

    @commands.command(pass_context=True, no_pm=True)
    async def cuehplaysongs(self, ctx):
        if self.player is None or self.player.is_done():
            url = self.playlist[self.current]
            await self.playsong(url)
    
    @commands.command(pass_context=True,no_mp=True)
    async def cuehballeneros(self):
        urlballeneros="https://www.youtube.com/watch?v=6bQ3lZRMI6c"
        if(self.player is None or self.player.is_done()):
            await self.playsong(urlballeneros)

    async def playsong(self, url):
        if self.voice is None:
            await  self.show_message("Primero conectame a un canal de voz con el comando !cueh")
        else:
            if self.player is None or self.player.is_done():
                self.player = await self.voice.create_ytdl_player(url)
                await self.show_message("Reproduciendo {}".format(url))
                self.player.start()

    @commands.command(pass_context=True, no_pm=True)
    async def cuehnext(self, ctx):
        if len(self.playlist) == 1:
            await self.show_message("Solo hay una cancion por favor añade mas canciones con cuehadd")
        await self.stopsong(self.playlist[self.current])
        self.current += 1
        self.current %= len(self.playlist)
        await self.playsong(self.playlist[self.current])

    @commands.command(pass_context=True, no_pm=True)
    async def cuehback(self, ctx):
        if len(self.playlist) == 1:
            await self.show_message("Solo hay una cancion por favor añade mas canciones con cuehadd")
        await self.stopsong(self.playlist[self.current])
        self.current -= 1
        self.current %= len(self.playlist)
        await self.playsong(self.playlist[self.current])

    @commands.command(pass_context=True, no_pm=True)
    async def cuehstop(self, ctx):
        if self.player is not None:
            if not self.player.is_done():
                msg = "Parando {}, cueh".format(self.player.title)
                await self.show_message(msg, mtts=False)
                self.player.stop()
        pass

    async def show_message(self, msg, mtts=False):
        print(msg)
        await self.bot.say(msg, tts=mtts)
        pass

    async def stopsong(self, url):
        if self.player is not None:
            await self.show_message("Parando {}".format(url))
            self.player.stop()


bot.add_cog(Cueh(bot))
@bot.event
async def on_ready():
    print("cueh v{} ready".format(settings.version))
    print("Logged into {} ".format(bot.user.id))
bot.run(settings.bot_token)