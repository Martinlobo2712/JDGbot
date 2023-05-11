import lightbulb
import hikari
import valorant
import os
import miru
from miru.ext import nav
from dotenv import load_dotenv

load_dotenv()

plugin = lightbulb.Plugin("Valorant Plugin")

client = valorant.Client(
    os.environ["VALORANT_KEY"],
    locale="en-US"
)

class MyNavButton(nav.NavButton):
    # This is how you can create your own navigator button
    # The extension also comes with the following nav buttons built-in:
    #
    # FirstButton - Goes to the first page
    # PrevButton - Goes to previous page
    # IndicatorButton - Indicates current page number
    # StopButton - Stops the navigator session and disables all buttons
    # NextButton - Goes to next page
    # LastButton - Goes to the last page

    async def callback(self, ctx: miru.ViewContext) -> None:
        await ctx.respond("You clicked me!", flags=hikari.MessageFlag.EPHEMERAL)

    async def before_page_change(self) -> None:
        # This function is called before the new page is sent by
        # NavigatorView.send_page()
        self.label = f"Page: {self.view.current_page+1}"

@plugin.command
@lightbulb.command("skins", "shows skins")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def showSkins(ctx: lightbulb.Context):
    embeds = []
    skins = client.get_skins()

    for skin in skins:
        embeds.append(hikari.Embed(title="Skins", description=f"{skin.name}")) 
        
    # Define our navigator and pass in our list of pages
    navigator = nav.NavigatorView(pages=embeds)
    # You may also pass an interaction object to this function
    await navigator.send(ctx.channel_id)

def load(bot: lightbulb.BotApp) -> None:
  bot.add_plugin(plugin)