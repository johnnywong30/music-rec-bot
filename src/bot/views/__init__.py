import discord
from bot.tidal.tracks import get_similar_tracks, get_track


class Counter(discord.ui.View):

    @discord.ui.button(label="0", style=discord.ButtonStyle.red)
    async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


class RecommendBtn(discord.ui.View):
    @discord.ui.button(label="Get Recommendations", style=discord.ButtonStyle.primary)
    async def recommend(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await interaction.response.send_message("Hello")
