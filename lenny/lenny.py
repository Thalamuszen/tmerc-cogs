from random import choice

from discord.ext import commands


class Lenny:

    """( ͡° ͜ʖ ͡°)"""

    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.ears = [
            "q{}p", "ʢ{}ʡ", "⸮{}?", "ʕ{}ʔ", "ᖗ{}ᖘ", "ᕦ{}ᕥ", "ᕦ({})ᕥ", "ᕙ({})ᕗ",
            "ᘳ{}ᘰ", "ᕮ{}ᕭ", "ᕳ{}ᕲ", "({})", "[{}]", "¯\\\_{}_/¯", "୧{}୨",
            "୨{}୧", "⤜({})⤏", "☞{}☞", "ᑫ{}ᑷ", "ᑴ{}ᑷ", "ヽ({})ﾉ", "\\\({})/",
            "乁({})ㄏ", "└[{}]┘", "(づ{})づ", "(ง{})ง", "|{}|"
        ]
        self.eyes = [
            "⌐■{}■", " ͠°{} °", "⇀{}↼", "´• {} •`", "´{}`", "`{}´", "ó{}ò",
            "ò{}ó", ">{}<", "Ƹ̵̡ {}Ʒ", "ᗒ{}ᗕ", "⪧{}⪦", "⪦{}⪧", "⪩{}⪨", "⪨{}⪩",
            "⪰{}⪯", "⫑{}⫒", "⨴{}⨵", "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤",
            "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ",
            "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*",
            "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•",
            "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$",
            "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧",
            "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ",
            "ಠ{}ಠ", "σ{}σ"
        ]
        self.mouth = [
            "v", "ᴥ", "ᗝ", "Ѡ", "ᗜ", "Ꮂ", "ヮ", "╭͜ʖ╮", " ͟ل͜", " ͜ʖ", " ͟ʖ",
            " ʖ̯", "ω", "³", " ε ", "﹏", "ل͜", "╭╮", "‿‿", "▾", "‸", "Д",
            "∀", "!", "人", ".", "ロ", "_", "෴", "ѽ", "ഌ", "⏏", "ツ", "益"
        ]

    @commands.command(pass_context=True, name="lenny")
    async def _lenny(self, ctx: commands.Context):
        """Displays a random ASCII face."""

        lenny = choice(self.ears).format(
            choice(self.eyes)).format(choice(self.mouth))
        await self.bot.say(lenny)


def setup(bot: commands.bot):
    bot.add_cog(Lenny(bot))