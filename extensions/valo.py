import lightbulb, hikari, valorant, os, miru, json
from miru.ext import nav
from dotenv import load_dotenv

load_dotenv()

with open("extensions/valorantData.json") as f:
    data = json.load(f)

plugin = lightbulb.Plugin("Valorant Plugin")

client = valorant.Client(
    os.environ["VALORANT_KEY"],
    locale=None
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
    skinsData = data["skins"]
    maxIdx = len(skinsData)


    for idx, skin in enumerate(skins):
        embed = hikari.Embed(title="Skins", description=f"{skin.name}")
        
        if(not idx > maxIdx-1):
            skinData = skinsData[idx]

            embed.set_image(skinData["url"])
            embed.color = skinData["color"]

        embeds.append(embed) 
        
    # Define our navigator and pass in our list of pages
    navigator = nav.NavigatorView(pages=embeds)
    # You may also pass an interaction object to this function
    await navigator.send(ctx.channel_id)

def load(bot: lightbulb.BotApp) -> None:
  bot.add_plugin(plugin)