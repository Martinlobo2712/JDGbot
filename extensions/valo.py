import lightbulb
import hikari
import valorant
import os
from dotenv import load_dotenv

plugin = lightbulb.Plugin("Valorant Plugin")

client = valorant.Client(
    os.environ["VALORANT_KEY"],
    locale=None
)

@plugin.command
#@lightbulb.option("name", "Name of the player", type=str, required=True)
@lightbulb.command("skins", "gets player info")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def playerInfo(ctx: lightbulb.Context):

    skins = client.get_skins()

    for skin in skins:
        embed = hikari.Embed(title="Skins", description=f"{skin.name}")
        
        await ctx.respond(embed)



def load(bot: lightbulb.BotApp) -> None:
  bot.add_plugin(plugin)