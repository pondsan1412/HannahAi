import discord
import discord.ext.commands as commands

class leave(commands.Cog):
    def __init__(
        self,
        bot:commands.Bot
    ):
        self.bot = bot

    @commands.hybrid_command(name='ออกไป')
    async def leave(self,ctx:commands.Context):
        """ให้บอทออกจากห้องเสียง"""
        # ตรวจสอบว่าบอทอยู่ในห้องเสียงหรือไม่
        if ctx.voice_client is None:
            await ctx.send("บอทไม่ได้อยู่ในห้องเสียงใดๆ!")
            return

        # ถ้าบอทอยู่ในห้องเสียง จะทำการตัดการเชื่อมต่อ
        await ctx.voice_client.disconnect()
        await ctx.send("บอทออกจากห้องเสียงแล้ว")

    


async def setup(bot: commands.Bot):
    await bot.add_cog(leave(bot))