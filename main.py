import os
import lightbulb
import hikari

import dotenv

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    prefix="!", 
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(902692574601543700,)
)

@bot.listen(hikari.ShardReadyEvent)
async def ready_listener(_):
    print("The bot is ready!")


@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")

bot.run()