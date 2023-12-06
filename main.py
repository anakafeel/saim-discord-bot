import discord
import os
import asyncio
from discord.ext import commands
import discord.ext.commands
import numpy
import random
import math
import requests
import json
from keep_alive import keep_alive
from bs4 import BeautifulSoup
import lxml
import aiohttp

client = commands.Bot(command_prefix=">")
client.remove_command('help')

commands.Bot(command_prefix='>', help_command=None)


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


omar = 368058579657293824
arfan = 573557000697282580
saim = 587612275460931595
saad = 720635516868886589
eris = 581163843376381973
juv = 849660858685980702


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    while message.author.id == saad:
        choices = (
            'i love biharis', 'omg the better bihari', 'hi saad cutie ',
            'wa alaykum as salaam (bihaari) <:smiling_imp:866035689882910730>')
        if message.content.startswith('>'):
            await message.channel.send(random.choices(choices))
            await message.channel.send('<:jawline:858627661442187314>')
            return

        else:
            return

    while message.content.startswith('>salaam'):
        if message.author.id == omar:
            await message.channel.send(
                'wa alaykum as-salam wa rahmatullahi wa barakatuh omar')
            await message.channel.send('<:promuslim:861429824844464158>')
            return

        if message.author.id == saim:
            await message.channel.send(
                'walekumassalaam saim <:maloomaeenaaa:858630011594211338>')
            return

        if message.author.id == eris:
            await message.channel.send('walekumassalaam maryam')
            return

        if message.author.id == arfan:
            choices = ('begone thot', 'are you like degenerate?',
                       'you are adopted', 'chutiya', "shahzan was here :)")
            await message.channel.send(random.choice(choices))
            await message.channel.send
            ('<:orphan:858625863854587924>')
            return

        else:
            await message.channel.send('walekumassalaam ')
            return

    while message.content.startswith('>sex'):
        if message.author.id == omar:
            await message.channel.send('anytime with you baby ;)')
            return

        if message.author.id == saim:
            await message.channel.send('ok. but dont tell ur gf ;)')
            return

        if message.author.id == arfan:
            await message.channel.send(
                "ew. never in your wildest dreams you cunt.")
            return

        if message.author.id == juv:
            await message.channel.send(
                "I think you'd rather have the real thing")
            await message.channel.send('<:maloomaeenaaa:858630011594211338>')
            return

        else:
            choices = ('Nah,you too ugly for that',
                       'Wouldnt mind having it with your mom',
                       'Only if you play wid deez nuts')
            await message.channel.send(random.choice(choices))

            return

    await client.process_commands(message)


@client.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author

    embed = discord.message.Embed(
        title='So you asked for assistance eh?',
        description='This is a list of commands you can use for now: ',
        color=discord.Colour.gold())
    embed.set_author(name='Omar & Saim')

    embed.set_thumbnail(
        url='https://thumbs.gfycat.com/PossibleSmartAsp-size_restricted.gif')

    embed.add_field(name='>salaam',
                    value='Greet the bot. <:promuslim:861429824844464158>',
                    inline=False)
    embed.add_field(name='>wave',
                    value='Wave at someone! <:wave:870326359426224138>',
                    inline=False)
    embed.add_field(name='>hug',
                    value='Hug someone! <:people_hugging:870326977167495178>',
                    inline=False)
    embed.add_field(
        name='>slap',
        value='Slap someone lul? <:constipation:858628094717591557>',
        inline=False)
    embed.add_field(name='>spank',
                    value='Spank someone. <:no_mouth:870643177227440178> ',
                    inline=False)
    embed.add_field(
        name='>howgay',
        value=
        'Find out how gay someone really is... <:rainbow_flag:866731552708493322>',
        inline=False)
    embed.add_field(name='>kiss',
                    value='Kiss someone. <:gafsmash:858629493601468417>',
                    inline=False)
    embed.add_field(
        name='>sex',
        value=
        'Ask the bot for sex? <:eggplant:867287895144267826> <:watermelon:867287895144267826> <:sweat_drops:867287895144267826>',
        inline=False)

    embed.set_footer(
        text='Information requested by: {}'.format(ctx.author.display_name))

    await ctx.send('Check your DM!')
    await ctx.send('<:smiling_imp:866035689882910730>')
    await author.send(embed=embed)
    return


@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member):

    if user.bot:
        await ctx.send("Sorry, I only have eyes for Yuvi's mom")
        await ctx.send("<:02smug:907840620712841258>")

    elif user.id == saim:
        await ctx.send("He is straighter than the pole your mom dances on.")
        await ctx.send("<:AwOo:907840918349029429>")

    elif user == ctx.author:
        await ctx.send("You are gae.")
        await ctx.send(":rainbow_flag:")

    else:

        g_value = math.floor(random.randint(1, 101))

        await ctx.send(f"Looks like {user.mention} is {g_value} % gay...")

        g_value = int(str(numpy.array(g_value)))

        if g_value in range(0, 30):
            await ctx.send(
                "https://tenor.com/view/shaking-head-cute-dog-straight-face-gif-16172986"
            )
            await ctx.send("Pretty straight eh?")

        elif g_value in range(31, 60):
            await ctx.send(
                "https://tenor.com/view/sus-fry-futurama-gif-4691459")
            await ctx.send("You're walking a thin line dude...")

        elif g_value in range(61, 90):
            await ctx.send(
                "https://tenor.com/view/datdragonshow-dragons-and-things-real-close-really-close-really-gif-12158274"
            )
            await ctx.send("just... *a little more...*")

        elif g_value in range(91, 102):
            await ctx.send(
                "https://tenor.com/view/soap-gay-bath-oops-gif-10322886")
            await ctx.send("**GAAAEEEEE**")
            return

        return
        client.add_command('howgay')


@client.command(pass_context=True)
async def slap(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("awww you could never slap me, alpha sama")
            apikey = "GST1BBXCT14X"
            lmt = 15
            search_term = "anime smile"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
        else:
            await ctx.send("you think you can slap me?")

            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime slap"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

            await ctx.send(f"{ctx.author.mention} was slapped by me.")

    elif user == ctx.author:
        await ctx.send("Awwww, why do you want to slap yourself?")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime pat"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} slapped " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime slap"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("OMG ALPHA SAMA COME HERE")
            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime hug"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
            await ctx.send("<:7974_rimuru_lewd_hearteyes:907840855828729886>")
        else:
            await ctx.send("Ew. I'd never hug scum like you")
            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime disgust"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

    elif user == ctx.author:
        await ctx.send("You wanna hug yourself??")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime what"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} hugged " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime hug"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


@client.command(pass_context=True)
async def wave(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("**HIIIII ALPHA SAMA**")
            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime wave"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
        else:
            await ctx.send(f"yo {ctx.author.mention}")

            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime wave"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

    elif user == ctx.author:
        await ctx.send("You're waving at yourself??")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime what"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} waved at " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime wave"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


@client.command(pass_context=True)
async def spank(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("*MMMH ALPHA SAMA YAMETE*")
            apikey = "GST1BBXCT14X"
            lmt = 15
            search_term = "anime lewd"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
        else:
            await ctx.send("You think **YOU** can spank **ME**??")

            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime spank"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

            await ctx.send(f"{ctx.author.mention} got reverse spanked lol")
            await ctx.send("<:02smug:907840620712841258>")

    elif user == ctx.author:
        await ctx.send("**What.** You.... *tried to spank yourself???*")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime huh"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} spanked " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime spank"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


@client.command(pass_context=True)
async def gm(ctx):
    await ctx.send(f"{ctx.author.mention} GOOD FRIKIN MORNING FAM")

    apikey = "GST1BBXCT14X"
    lmt = 20

    search_term = "anime good morning"

    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                     (search_term, apikey, lmt))

    json_file = r.json()

    index = math.floor(random.randint(0, int(len(json_file['results']) - 1)))

    await ctx.send(json_file['results'][index]['url'])
    return

    client.add_command('gm')


@client.command(pass_context=True)
async def kill(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("Alpha sama wouldn't kill me")
            apikey = "GST1BBXCT14X"
            lmt = 10
            search_term = "anime hug"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
        else:
            await ctx.send("You can't kill me, silly")

            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime evil laugh"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

            await ctx.send("Only my... **Alpha sama can kill me**")
            await ctx.send("<:SagiriShy:907840919808671814>")

    elif user == ctx.author:
        await ctx.send("You wanna die? **LOOOOL OK**")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime suicide"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} killed " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime kill"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):

    if user.bot:
        if ctx.author.id == omar:
            await ctx.send("*alpha sama.... dame dayo*")
            apikey = "GST1BBXCT14X"
            lmt = 10
            search_term = "anime intimate kiss"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])
        else:
            await ctx.send("Ew. Why tf would I kiss you??")
            apikey = "GST1BBXCT14X"
            lmt = 40
            search_term = "anime disgust"

            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                (search_term, apikey, lmt))

            json_file = r.json()

            index = math.floor(
                random.randint(0, int(len(json_file['results']) - 1)))

            await ctx.send(json_file['results'][index]['url'])

    elif user == ctx.author:
        await ctx.send("You wanna kiss yourself??")
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime what"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])

    else:
        await ctx.send(f"{ctx.author.mention} kissed " + user.mention)
        apikey = "GST1BBXCT14X"
        lmt = 40
        search_term = "anime kiss"

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (search_term, apikey, lmt))

        json_file = r.json()

        index = math.floor(
            random.randint(0, int(len(json_file['results']) - 1)))

        await ctx.send(json_file['results'][index]['url'])
        return


async def web_scrape(text):
    async with aiohttp.ClientSession() as session:
        async with session.get(text) as r:
            status = r.status
            if status == 200:
                text = await r.text()
                return text


@client.command()
async def wyr(ctx):
    text = await web_scrape("http://either.io/")
    soup = BeautifulSoup(text, 'lxml')
    l = []
    for choice in soup.find_all("span", {"class": "option-text"}):
        l.append(choice.text)

    e = discord.message.Embed(color=discord.Colour.random())
    e.set_author(name="Would you Rather...?",
                 url="http://either.io/",
                 icon_url=client.user.avatar_url)
    e.add_field(name="EITHER...",
                value=f":regional_indicator_a: {l[0]}",
                inline=False)
    e.add_field(name="OR",
                value=f":regional_indicator_b: {l[1]}",
                inline=False)

    msg = await ctx.send(embed=e)
    await msg.add_reaction("🇦")
    await msg.add_reaction("🇧")


keep_alive()
client.run(os.environ['key'])
