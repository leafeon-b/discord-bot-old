# At the top of the file.
import random

import disnake
from disnake.ext import commands

import settings
from DenpoView import DenpoView


class Bot(commands.Bot):
    def __init__(self, intents: disnake.Intents):
        super().__init__(command_prefix=commands.when_mentioned, intents=intents, test_guilds=[settings.GUILD_ID])

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


intents = disnake.Intents.all()
bot = Bot(intents)


@bot.slash_command()
async def denpo(inter: disnake.AppCmdInter):
    """Starts Denpo game."""
    vc: disnake.VoiceChannel = disnake.utils.get(inter.guild.voice_channels, name="General")
    print(vc)
    member_names = [member.name for member in vc.members]
    print(f"{member_names=}")

    view = DenpoView()
    await inter.send(embed=view.embed, view=view)


@bot.slash_command()
async def shuffle(inter: disnake.AppCmdInter, vc: disnake.VoiceChannel = None):
    """Shuffle vc members(default vc is "General")."""
    if vc is None:
        vc = disnake.utils.get(inter.guild.voice_channels, name="General")
    member_names = [member.name for member in vc.members]
    member_names.append("hoge")
    member_names.append("fuga")
    random.shuffle(member_names)
    await inter.response.send_message("\n".join(member_names))


@bot.slash_command(name="char")
async def random_character(inter: disnake.AppCmdInter):
    """Creates random alphabet."""
    characters = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
    c = random.choice(characters)
    await inter.response.send_message(c)


@bot.slash_command(name="ito", description="Creates random natural number <= 100. This message is shown to only you.")
async def random_n(inter: disnake.AppCmdInter):
    n = random.randint(1, 100)
    await inter.response.send_message(n, ephemeral=True)


@bot.slash_command()
async def dice(inter: disnake.AppCmdInter, number: commands.Range[1, ...]):
    """Show the result of dice roll only to you."""
    await inter.response.send_message(random.randint(1, number), ephemeral=True)


@bot.slash_command()
async def d(inter: disnake.AppCmdInter, number: commands.Range[1, ...]):
    """Alias of dice."""
    await dice(inter, number)


bot.run(settings.TOKEN)
