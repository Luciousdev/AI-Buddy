from twitchio.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')  # Get Twitch token from environment variables
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')  # Get Twitch channel from environment variables

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN, 
            prefix='!',  
            initial_channels=[TWITCH_CHANNEL]
        )

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        # Log the message content
        print(f'[{message.author.name}] {message.content}')

        # Process the message further if needed
        await self.handle_commands(message)

# Create an instance of the Bot and run it
bot = Bot()
bot.run()