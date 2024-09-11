import discord.ext.commands as commands
import discord

class message_handlers(commands.Cog):
    def __init__(
        self,
        bot:commands.Bot
    ):
        self.bot = bot

    #handlers event messages
    async def on_message(self, message:discord.Message):
        """included all channel"""
        if message.author == self.bot.user:
            return #required ไม่งั้น spamming
        
        if message.content.startswith('!hi'):
            await message.reply("Hello world!")

        
#export modules
async def setup(bot:commands.Bot):
    await bot.add_cog(message_handlers(bot))

        