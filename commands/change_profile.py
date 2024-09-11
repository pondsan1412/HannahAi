import discord
from discord.ext import commands
import requests

class change_profile(commands.Cog):
    def __init__(
        self,
        bot:commands.Bot
    ):
        self.bot = bot

    @commands.hybrid_command(name="เปลี่ยนรูปโปร")
    async def change_pfp(self, ctx: commands.Context):
        """เปลี่ยนรูปโปรไฟล์ให้บอทโดยใช้ไฟล์ภาพที่แนบมาด้วย"""
        await ctx.defer()

        # ตรวจสอบว่ามีไฟล์ถูกแนบมาหรือไม่
        if len(ctx.message.attachments) == 0:
            await ctx.send("กรุณาแนบไฟล์ภาพมาด้วย!")
            return

        # ดึงไฟล์ที่ถูกแนบมา
        attachment = ctx.message.attachments[0]

        # ตรวจสอบว่าไฟล์ที่แนบมาเป็นภาพหรือไม่
        if attachment.content_type not in ['image/png', 'image/jpeg', 'image/webp']:
            await ctx.send(f"ไฟล์รูปแบบ {attachment.content_type} ไม่รองรับ")
            return
        
        # ดึงข้อมูลภาพในรูปแบบ bytes
        image_bytes = await attachment.read()

        # เปลี่ยนรูปโปรไฟล์ของบอท
        try:
            await self.bot.user.edit(avatar=image_bytes)
            await ctx.send("เปลี่ยนรูปโปรไฟล์สำเร็จ!")
        except Exception as e:
            await ctx.send(f"เกิดข้อผิดพลาดในการเปลี่ยนรูปโปรไฟล์: {e}")

async def setup(bot):
    await bot.add_cog(change_profile(bot))