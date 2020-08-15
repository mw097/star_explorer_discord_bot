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
        if message.author.id != self.user.id:
            return

        # Check if has command prefix
        if not message.content.startswith(settings.command_prefix):
            return

        # TODO: Parse commands


star_explorer().run_bot()
