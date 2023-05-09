import lightbulb
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
#    account = client.get_user_by_name(ctx.options.name)
#
#    match = account.matchlist().history.find(queueId="competitive")
#    
#    if match == None:
#        print("No Ranked match in recent history!")
#        exit(1)
#    else:
#        match = match.get()
    skins = client.get_skins()

    for skin in skins:
       print(f"{skin.name}\n")

def load(bot: lightbulb.BotApp) -> None:
  bot.add_plugin(plugin)