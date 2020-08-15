import discord
import settings


class star_explorer(discord.Client):
    """Constructor for StarExplorer"""

    def __init__(self):
        # Initialise the discord.Client
        super().__init__()

    def run_bot(self):
        """Run StarExplorer"""

        print('[StarExplorer]: Loading bot...')
        self.run(settings.token_discord)

    async def on_ready(self):
        """Method called when bot has started"""

        print('[StarExplorer]: Logged in as {0.user}'.format(self))

    async def on_message(self, message):
        """Method called when new message is received by bot"""

        # Check if sender is self
        if message.author.id == self.user.id:
            return

        # Check if has command prefix
        if not message.content.startswith(settings.command_prefix):
            return

        # Parse command and args
        command = message.content.replace(settings.command_prefix, "", 1).split(" ")[0]
        args = message.content.replace(settings.command_prefix, "", 1).split(" ")[1:]

        # ## Execute command ## #

        # help
        if command == "help":
            await self.command_help(message)
            await message.delete()

        # TODO
        # help <args>
        if command == "help" and len(args) == 1:
            await self.command_help(args, message.channel)
            await message.delete()

    # ## Commands ## #

    async def command_help(self, message):
        """Shows help"""

        await message.channel.send('Use command like this: $<command_name> <arguments>. For example: $apod')

    # TODO
    async def command_help_ex(self, message, args):
        """Shows extended help"""

        pass

star_explorer().run_bot()
