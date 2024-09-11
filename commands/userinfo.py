import discord
from discord.ext import commands

class userinfo(commands.Cog):
    def __init__(
        self,
        bot:commands.Bot
    ):
        self.bot = bot

    @commands.hybrid_command(name="userinfo")
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None):
        """แสดงข้อมูลของผู้ใช้"""
        member = member or ctx.author
        embed = discord.Embed(title=f"ข้อมูลของ {member}", color=discord.Color.blue())
        embed.add_field(name="ชื่อ", value=member.display_name)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="วันที่เข้าร่วม", value=member.joined_at.strftime("%Y-%m-%d"))
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(userinfo(bot))