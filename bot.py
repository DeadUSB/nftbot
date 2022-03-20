import discord, os, random
from discord.ext import commands
from PIL import Image
from datetime import date, datetime

bot = commands.Bot(command_prefix='!')

def refresh_assets():
    global backpath, backgrounds, forepath, foregrounds, effectpath, effects, gifpath, gifs
    backpath = "images\\backgrounds\\"
    backgrounds = os.listdir(backpath)

    forepath = "images\\foregrounds\\"
    foregrounds = os.listdir(forepath)

    effectpath = "images\\effects\\"
    effects = os.listdir(effectpath)

    gifpath = "images\\gifs\\"
    gifs = os.listdir(gifpath)

refresh_assets()

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

@bot.command()
@commands.is_owner()
async def refresh(ctx):
    await ctx.send("Refeshing...")
    refresh_assets()
    print("refreshing!")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("bye!")
    print("Shutting down...")
    await bot.close()

@bot.command()
async def repeat(ctx, *, arg):
    await ctx.send(arg)
    print('repeated:', arg)

@bot.command()
async def gif(ctx):
    await ctx.send(file=discord.File(gifpath + random.choice(gifs)))
    print("sent funny gif haha")

@bot.command()
async def generate(ctx):
    with Image.open(backpath + random.choice(backgrounds)).convert("RGBA") as image1:
        with Image.open(forepath + random.choice(foregrounds)).convert("RGBA") as image2:
            with Image.open(effectpath + random.choice(effects)).convert("RGBA") as image3:
                final = Image.new("RGBA", image1.size)
                final = Image.alpha_composite(final, image1)
                final = Image.alpha_composite(final, image2)
                final = Image.alpha_composite(final, image3)
                final.save("images\\final.png")
                await ctx.send(file=discord.File('images\\final.png'))
                print("generated and sent NFT")

bot.run('no no no little man')