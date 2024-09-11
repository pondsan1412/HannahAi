import discord
import discord.ext.commands as commands
import os
import datetime
import json
import random

class hannahai(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            description="บอทนี้เป็นบอทแบบ custom ใช้งานในกลุ่มเพื่อนเท่านั้น",
            allowed_installs=False,
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        """ติดตั้ง commands และ handlers"""
        async def load_cogs_from_folder(folder):
            for filename in os.listdir(f'./{folder}'):
                if filename.endswith('.py'):
                    cog_name = filename[:-3]
                    try:
                        await self.load_extension(f'{folder}.{cog_name}')
                        print(f'โหลด {folder}/{cog_name} สำเร็จ!')
                    except Exception as e:
                        print(f'ไม่สามารถโหลด {folder}/{cog_name}: {e}')

        await load_cogs_from_folder('commands')
        await load_cogs_from_folder('handlers')
    
    # event ตอนที่บอทออนไลน์
    async def on_ready(self):
        print(f"Online.. {datetime.datetime.now()}")
        await self.tree.sync()
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        txt_ch = self.get_channel(data['channel'][0]['compile_channel'])

        if txt_ch:
            # ส่งข้อความแบบ random จาก say_hello
            await txt_ch.send(
                content=f"{random.choice(data['say_hello'])}"
            )



from dotenv import load_dotenv
load_dotenv()
bot = hannahai()
bot.run(
    os.getenv("DISCORD_BOT_TOKEN")
)
