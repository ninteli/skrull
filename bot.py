import os
from dotenv import load_dotenv
import discord
from discord import app_commands

# Charge les variables du fichier .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Commande /ping
        @self.tree.command(name="ping", description="Renvoie Pong!")
        async def ping(interaction: discord.Interaction):
            await interaction.response.send_message("Pong!")
        
        # Commande /say avec confirmation éphémère
        @self.tree.command(name="say", description="Le bot répète votre message")
        @app_commands.describe(message="Le message à dire")
        async def say(interaction: discord.Interaction, message: str):
            # Envoie le message dans le salon (en tant que bot, pas en réponse à la commande)
            await interaction.channel.send(message)
            # Envoie la confirmation de façon éphémère à l'utilisateur
            await interaction.response.send_message("Message envoyé !", ephemeral=True)

        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

client.run(TOKEN)
