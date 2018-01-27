import discord
import settings
import datetime as DT
from discord.ext import commands

discord.opus.load_opus('libopus.0.dylib')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='Reproduce musica desde youtube')

class Cueh:
    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None

    async def join_channel(self,voicechannel):
        self.voice = await self.bot.join_voice_channel(voicechannel)
        pass
    @commands.command(pass_context=True, no_pm=True)
    async def cueh(self, ctx):
        voice_channel = ctx.message.author.voice_channel
        print('Conectando a {}'.format(voice_channel))
        if voice_channel is None:
            await self.show_message('Primero Conectate a un canal de voz, Cueh', mtts=True)
        await self.join_channel(voice_channel)

    @commands.command(pass_context=True, no_pm=True)
    async def cuehplay(self, ctx, urlsong):
        if self.voice is None:
            await self.show_message("Primero conectate a un canal de Voz, Cueh", mtts=True)
        if self.player != None:
            if not self.player.is_done():
                await self.show_message("Parando {}".format(self.player.title), mtts=True)
                self.player.stop()
        print("Reproduciendo {}".format(urlsong))
        self.player = await self.voice.create_ytdl_player(urlsong)
        msg = "Reproduciendo {}, cueh".format(self.player.title)
        await self.show_message(msg, mtts=True)
        self.player.start()
        pass
    @commands.command(pass_context=True,no_pm=True)
    async def cuehclean(self,ctx):
        today = DT.date.today()
        date_week= today - DT.timedelta(days = 7)
        current_channel=ctx.message.channel
        await bot.purge_from(channel=current_channel,before=date_week,limit=settings.message_limit)
        pass
    @commands.command(pass_context=True, no_pm=True)
    async def cuehstop(self, ctx):
        if self.player != None:
            if not self.player.is_done():
                msg = "Parando {}, cueh".format(self.player.title)
                await self.show_message(msg, mtts=True)
                self.player.stop()
        pass
    async def show_message(self, msg, mtts=False):
        print(msg)
        await self.bot.say(msg, tts=mtts)
        pass
bot.add_cog(Cueh(bot))
@bot.event
async def on_ready():
    print("cueh v{} ready".format(settings.version))
    print("Logged into {} ".format(bot.user.id))
bot.run(settings.bot_token)