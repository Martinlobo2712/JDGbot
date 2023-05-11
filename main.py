import os
import lightbulb
import hikari
import miru
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    prefix="!", 
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(902692574601543700,)
)

miru.install(bot)

@bot.listen(hikari.ShardReadyEvent)
async def ready_listener(_):
    print("The bot is ready!")

bot.load_extensions("extensions.valo")

@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")

bot.run()