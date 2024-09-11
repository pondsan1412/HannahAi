#เข้าร่วมห้องพูดคุยเสียง
import discord.ext.commands as commands
import discord

class join(commands.Cog):
    def __init__(
        self,
        bot:commands.Bot
    ):
        self.bot = bot
    
    @commands.hybrid_command(name='เข้ามา')
    async def join(self,ctx:commands.Context):
        """เข้าห้องเสียง"""

        if ctx.author.voice is None:
            await ctx.send("คุณต้องอยู่ในห้องเสียงก่อนถึงจะให้บอทเข้าร่วมได้!")
            return

        # ดึง channel เสียงที่ผู้ใช้กำลังอยู่
        voice_channel = ctx.author.voice.channel

        # ตรวจสอบว่าบอทไม่ได้อยู่ในห้องเสียงอื่น
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(voice_channel)
        else:
            await voice_channel.connect()

        await ctx.send(f"บอทเข้าร่วมห้องเสียง: {voice_channel.name}")

async def setup(bot):
    await bot.add_cog(join(bot))

    