import discord
import settings
import nasa_api


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

        # apod
        if command == "apod":
            await self.command_apod(message, args)
            await message.delete()

        if command == "neofeedcount":
            await self.command_neofeed_count(message, args)
            await message.delete()

        if command == "neofeedlist":
            await self.command_neofeed_list(message, args)
            await message.delete()
            
    # ## Commands ## #

    async def command_help(self, message):
        """Shows help"""

        await message.channel.send('Use command like this: $<command_name> <arguments>. For example: $apod')

    # TODO
    async def command_help_ex(self, message, args):
        """Shows extended help"""

        pass

    async def command_apod(self, message, imgDate):
        """Get Astronomy Picture of Day"""
        nasa = nasa_api.NASAClient()
        await message.channel.send(nasa.fetch_apod_img(imgDate))

    async def command_neofeed_count(self, message, dates):
        """Get a count of asteroids based on their closes approach date to Earth"""
        nasa = nasa_api.NASAClient()
        await message.channel.send(nasa.fetch_neows_feed_count(dates))

    async def command_neofeed_list(self, message, dates):
        """Get a list of asteroids based on their closes approach date to Earth"""
        nasa = nasa_api.NASAClient()
        msg = ''
        for st in nasa.fetch_neows_feed_list(dates):
            msg += st + " "

        await message.channel.send(msg)

star_explorer().run_bot()
