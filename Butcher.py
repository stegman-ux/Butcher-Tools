from pystyle import Colorate, Colors
import clear
import os
import colorama
from colorama import Fore, init , Style
import requests
import whois
import customtkinter as ctk
import fade
import whois
import time
import instaloader
from cryptography.fernet import Fernet
import base64
import random
import discord
from discord.ext import commands
import socket
os.system("title Butcher Tools")



hostname = socket.gethostname()

root = (Fore.LIGHTMAGENTA_EX+f"""
┌──({hostname}@Butcher)-[~Menu -]│
└─$>""")

ascii_ = '''
▀█████████▄  ███    █▄      ███      ▄████████    ▄█    █▄       ▄████████    ▄████████      
  ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███     ███    ███   ███    ███ Made by intrable <3    
  ███    ███ ███    ███    ▀███▀▀██ ███    █▀    ███    ███     ███    █▀    ███    ███ Version : 1.0    
 ▄███▄▄▄██▀  ███    ███     ███   ▀ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███▀▀▀██▄  ███    ███     ███     ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        
  ███    ██▄ ███    ███     ███     ███    █▄    ███    ███     ███    █▄  ▀███████████      
  ███    ███ ███    ███     ███     ███    ███   ███    ███     ███    ███   ███    ███      
▄█████████▀  ████████▀     ▄████▀   ████████▀    ███    █▀      ██████████   ███    ███      
                                                                             ███    ███   
                                                                                           
┌─────────────────┐                        ┌─────────┐                          ┌───────────┐            
├──── Osint-Tools ┤────────────┬───────────┤ Discord ├────────────┬─────────────┤ Utilities ├────────────┤
└─────────────────┘            │           └─────────┘            │             └───────────┘            │
├ [01] OSINT Recon Menu        ├ [02] Discord-Tools Menu          ├ [03] Utilities Tool Menu             │
│────────────────────────────────────────────────────────────────────────────────────────────────────────│
│ [N] Next Page  |  [B] Back  |  [C] Credits | [Q] Quit                                                  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

   
'''

def main():
    clear.clear()
    COLs = Colorate.Diagonal(Colors.blue_to_red, ascii_)
    print(COLs)
    
    choice = input(root)
    
    if choice == "1" or choice == "01":
        clear.clear()
        osintmenu()
    if choice == "2" or choice == "02":
        clear.clear()
        discordmenu()
    if choice == "c" or choice == "C":
        clear.clear()
        Credit()
    if choice == "q" or choice == "Q":
        exit()
    if choice == "n" or choice == "N":
        input("[SOON] Next Menu comming soon ! ")
        clear.clear()
        main()
    if choice == "b" or choice == "B":
        input("[SOON] Next Menu comming soon ! ")
        clear.clear()
        main()
    else:
        input("[ERROR] Invalid option...")
        clear.clear()
        main()


def Credit():
    print(Fore.CYAN + r"""
+----------------------------------------------------------+
|                                                          |
|    ██████╗██████╗ ███████╗██████╗ ██╗████████╗           |
|   ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝           |
|   ██║     ██████╔╝█████╗  ██║  ██║██║   ██║              |
|   ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║              |
|   ╚██████╗██║  ██║███████╗██████╔╝██║   ██║              |
|    ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝              |
|                                                          |
|              Created by : Intrable                       |
|              Project    : Butcher-Tools                  |
|              Discord    : discord.gg/freeforreal         |
|              Version    : 1.0                            |
+----------------------------------------------------------+
""" + Style.RESET_ALL)
    input("Press enter for return to the menu...")
    clear.clear()
    main()
  
  
  
def discordmenu():
  ascii_discord = '''
████████▄   ▄█     ▄████████  ▄████████  ▄██████▄     ▄████████ ████████▄  
███   ▀███ ███    ███    ███ ███    ███ ███    ███   ███    ███ ███   ▀███ 
███    ███ ███▌   ███    █▀  ███    █▀  ███    ███   ███    ███ ███    ███ 
███    ███ ███▌   ███        ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
███    ███ ███▌ ▀███████████ ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███ 
███    ███ ███           ███ ███    █▄  ███    ███ ▀███████████ ███    ███ 
███   ▄███ ███     ▄█    ███ ███    ███ ███    ███   ███    ███ ███   ▄███ 
████████▀  █▀    ▄████████▀  ████████▀   ▀██████▀    ███    ███ ████████▀  
                                                     ███    ███            
╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                            DISCORD TOOLS
╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────╜

├─ [01] Discord Webhook Spammer         ├─ [06] Discord ID to First-part Token  ├─ [11] Discord Dmall Bot
├─ [02] Discord Webhook Deleter         ├─ [07] Discord Server Info             ├─ [12] Discord Token Dmall
├─ [03] Discord Token Info              ├─ [08] Discord Token Checker           ├─ [13] Soon...
├─ [04] Discord ID Info                 ├─ [09] Discord Nitro Generator         ├─ [14] Soon...
├─ [05] Discord Webhook Info            ├─ [10] Discord Bot ID to Invite        ├─ [15] EXIT Discord Menu

  '''
  coilorat = Colorate.Diagonal(Colors.blue_to_red, ascii_discord)
  print(coilorat)
  root_discord = (Fore.LIGHTMAGENTA_EX+"""
┌──(User@Assasin)-[~DISCORD]│
└─$>""")
  choicediscord = input(root_discord)
  if choicediscord == "1" or choicediscord == "01":
    webhooksend()
  if choicediscord == "2" or choicediscord == "02":
    webhookdel()
  if choicediscord == "3" or choicediscord == "03":
    discordtokeninfo()
  if choicediscord == "4" or choicediscord == "04":
    discord_idinfo()
  if choicediscord == "5" or choicediscord == "05":
    webhook_info()
  if choicediscord == "6" or choicediscord == "06":
    idtofristpartoken()
  if choicediscord == "7" or choicediscord == "07":
    serverinfo()
  if choicediscord == "8" or choicediscord == "08":
    tokencheck()
  if choicediscord == "9" or choicediscord == "09":
    nitrogen()
  if choicediscord == "10" or choicediscord == "010":
    idinvite()
  if choicediscord == "11" or choicediscord == "011":
    dmalld()
  if choicediscord == "12" or choicediscord == "012":
    dmalltoken()
  if choicediscord == "15" or choicediscord == "015":
    main()
    
    
def dmalltoken():
    clear.clear()
    ascii_dmalltoken = """
██████╗ ███╗   ███╗ █████╗ ██╗     ██╗     
██╔══██╗████╗ ████║██╔══██╗██║     ██║     
██║  ██║██╔████╔██║███████║██║     ██║      Token
██║  ██║██║╚██╔╝██║██╔══██║██║     ██║     
██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
[!]Ctrl + C : Exit
[!]RATE LIMIT DANGER ! DONT USE ON AN IMPORTANT ACCOUNT.
                                                                                                                                                                                                                     
   """
    print(fade.greenblue(ascii_dmalltoken))
    token = input(Fore.LIGHTBLUE_EX + "Account Token : ")  
    message = input(Fore.LIGHTBLUE_EX +"Message : ")

    headers = {
        'Authorization': token
    }
    channelid = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    rsp = channelid.json()
    
    for channel in rsp: 
      time.sleep(random.uniform(6.5, 7.5)) # I put a long delay before the request because u can be rate limit if the delay is short
      requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',headers=headers,json={"content": message})  
      print(Fore.LIGHTGREEN_EX+f"Message sent to channel ID : {channel['id']}")
      
    if channelid.status_code == '429':
      print("Oh no , You are rate limit ! ")
      input("Press enter to go back...")
      clear.clear()
      discordmenu()
    print()
    input("Pres enter to go back...")
    clear.clear()
    discordmenu()
def dmalld():
    clear.clear()
    ascii_dmall = """
██████╗ ███╗   ███╗ █████╗ ██╗     ██╗     
██╔══██╗████╗ ████║██╔══██╗██║     ██║     
██║  ██║██╔████╔██║███████║██║     ██║     
██║  ██║██║╚██╔╝██║██╔══██║██║     ██║     
██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                           
    [!] Press ctrl + C to stop the dmall.
    [!] When the dmall stops, it means all messages have been sent, so press Ctrl + C to exit.                                                                                                                                                                              
   """
    print(fade.greenblue(ascii_dmall))
    print()
    bottoken = input(Fore.LIGHTBLUE_EX + "Enter the bot token: ")
    prefixs = input("Enter the command prefix you want to use (e.g. + or !): ")


    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True 
    bot = commands.Bot(command_prefix=f"{prefixs}", intents=intents)
    
    @bot.command()
    async def dmall(ctx, *, message):
      for member in ctx.guild.members:
        if member.bot : 
          continue
        
        await ctx.send('Starting mass DM...')
        await member.send(message)  
        print(Fore.LIGHTGREEN_EX+f"Sent to : {member.id} | {member.name}")
    print()
    
    print(Fore.LIGHTRED_EX+f'Type "{prefixs}dmall <message>" in a server where the bot is invited to run the command.')
    bot.run(bottoken)
    print()
    input("Pres enter to go back...")
    clear.clear()
    discordmenu()
    
    
  
def idinvite():
    clear.clear()
    ascii_idbot = """
██╗██████╗     ████████╗ ██████╗     ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝
██║██║  ██║       ██║   ██║   ██║    ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗  
██║██║  ██║       ██║   ██║   ██║    ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝  
██║██████╔╝       ██║   ╚██████╔╝    ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗
╚═╝╚═════╝        ╚═╝    ╚═════╝     ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝
                                                                               
                                                                                                                           
   """
    print(fade.greenblue(ascii_idbot))
    print()
    cod = input(Fore.LIGHTBLUE_EX+"Enter the discord Bot ID : ")
    url =  f"https://discord.com/oauth2/authorize?client_id={cod}&scope=bot&permissions=8"
    print()
    print(Fore.LIGHTGREEN_EX+f"[{cod}] Bot invite url : ",url)
    print()
    input("Pres enter to go back...")
    clear.clear()
    discordmenu()
    
def check(code):
    valid = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}')

    if not valid.status_code == 200:
        return False
    else:
        return True
  
def gene():
    code = ""
    for i in range(19):
        code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return code
  
def nitrogen():
    clear.clear()
    ascii_ntrogen = """
███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                                                           
   """
    print(fade.greenblue(ascii_ntrogen))
    with open('nitrocodes-generated.txt', 'w') as file:
      numbers = int(input(Fore.LIGHTBLUE_EX+"Enter the amount of codes to generate : "))
      for _ in range(numbers):
            code = gene()
            valid = check(code)

            if valid:
                print(Fore.GREEN + f' Valid Nitro code Generated : {code}')
                file.write(f'{code} - VALID\n')
            else:
                print(Fore.RED + f' Invalid Nitro code Generated : '+Fore.WHITE+code)
                file.write(f'{code} - INVALID\n')
    print()
    input("Pres enter to go back...")
    clear.clear()
    discordmenu()

def tokencheck():
  ascii_stkencheck = """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                        
  [1] Single token check
  [2] Multi token check                                                     
   """

  clear.clear()
  print(fade.greenblue(ascii_stkencheck))
  choix2tigre = input(Fore.LIGHTBLUE_EX+"Enter your choice : ")
  if choix2tigre == "1" or choix2tigre == "01":
    onecheck()
  if choix2tigre == "2" or choix2tigre == "02":
    multicheck()
  
  
  
def onecheck():
  token = input(Fore.LIGHTBLUE_EX + "Enter the Discord Token : ")
  headers = {'Authorization': token}
    
  res = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
  if res.status_code == 200:
        print(Fore.LIGHTGREEN_EX + f"[+] Valid Token : {token}")
        print("User :", res.json()['username'])
  if res.status_code == 401:
        print(Fore.LIGHTRED_EX + f"[-] Invalid token : {token}")
    
  print()
  input("Pres enter to go back...")
  clear.clear()
  discordmenu()
    
    
    
    
def multicheck():
    tokens = input(Fore.LIGHTBLUE_EX + "Enter the Discord Tokens (comma-separated) : ")
    tokens = tokens.split(",")  
    
    for token in tokens:
        headers = {'Authorization': token}
        res = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        print()
        
        if res.status_code == 200:
            print(Fore.LIGHTGREEN_EX + f"[+] Valid Token : {token}")
            print("User :", res.json()['username'])
        elif res.status_code == 401:
            print(Fore.LIGHTRED_EX + f"[-] Invalid token : {token}")
        else:
            print(Fore.LIGHTRED_EX + "Error with Discord API.")
    
    
    print()
    input("Pres enter to go back...")
    clear.clear()
    discordmenu()
   
def serverinfo():
  ascii_serverinfo = """
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║██╔██╗ ██║█████╗  ██║   ██║
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║██║╚██╗██║██╔══╝  ██║   ██║
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║██║ ╚████║██║     ╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_serverinfo))
  invite = input(Fore.LIGHTBLUE_EX+"Enter the Discord Server Link : ")
  invite_code = invite.split("/")[-1]

  response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
  api = response.json()
  
  type_value = api.get('type', "n/a")
  code_value = api.get('code', "n/a")
  expires_at = api.get('expires_at', "n/a") # J'assume ouvertement m'etre aidé de l'ia afin de récuperer toutes les informations possibles , trop long , sinon.
  flags = api.get('flags', "n/a")

  server_info = api.get('guild', {})
  server_id = server_info.get('id', "n/a")
  server_name = server_info.get('name', "n/a")
  server_icon = server_info.get('icon', "n/a")
  server_features = server_info.get('features', [])
  server_features_str = ' / '.join(server_features) if server_features else "n/a"
  server_verification_level = server_info.get('verification_level', "n/a")
  server_nsfw_level = server_info.get('nsfw_level', "n/a")
  server_description = server_info.get('description', "n/a")
  server_nsfw = server_info.get('nsfw', "n/a")
  server_premium_subscription_count = server_info.get('premium_subscription_count', "n/a")

  channel_info = api.get('channel', {})
  channel_id = channel_info.get('id', "n/a")
  channel_type = channel_info.get('type', "n/a")
  channel_name = channel_info.get('name', "n/a")
  print()
  print(Fore.LIGHTBLUE_EX+f"""
📋 Invitation Information:

🔹 Invitation         : {invite}
🔹 Type               : {type_value}
🔹 Code               : {code_value}
🔹 Expired            : {expires_at}

🏰 Server:
  - ID                 : {server_id}
  - Name               : {server_name}
  - Description        : {server_description}
  - Icon               : {server_icon}
  - Features           : {server_features_str}
  - Verification Level : {server_verification_level}
  - NSFW Level         : {server_nsfw_level}
  - NSFW               : {server_nsfw}
  - Premium Subs Count : {server_premium_subscription_count}

📺 Channel:
  - ID                 : {channel_id}
  - Name               : {channel_name}
  - Type               : {channel_type}

🏳️ Flags               : {flags}
""")
  print()
  input("Pres enter to go back...")
  clear.clear()
  discordmenu()
    
def idtofristpartoken():
  ascii_tokenfirst = """
██╗██████╗          ██╗      ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║██╔══██╗         ╚██╗     ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║██║  ██║    █████╗╚██╗       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║██║  ██║    ╚════╝██╔╝       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║██████╔╝         ██╔╝        ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝╚═════╝          ╚═╝         ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_tokenfirst))
  tokenfirst= input(Fore.LIGHTBLUE_EX+"Enter the Discord ID : ")
  decodetoken = base64.b64encode(tokenfirst.encode()).decode().rstrip("=")
  print()
  print(Fore.LIGHTBLUE_EX+f"Token First Part of '{tokenfirst}' : {decodetoken} ")
  print()
  input("Pres enter to go back...")
  clear.clear()
  discordmenu()


def webhook_info(): 
  ascii_webok = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝  Information
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_webok))
  webhook = input(Fore.LIGHTBLUE_EX+"Enter the Discord Webhook URL : ")
  r = requests.get(webhook)
  jso = r.json()

  print("🔎 Webhook Info")
  print()
  print(f"🆔 ID              : {jso.get('id', 'N/A')}")
  print(f"🧩 Application ID  : {jso.get('application_id', 'N/A')}")
  print(f"🖼️ Avatar          : {jso.get('avatar', 'N/A')}")
  print(f"📺 Channel ID      : {jso.get('channel_id', 'N/A')}")
  print(f"🏠 Guild ID        : {jso.get('guild_id', 'N/A')}")
  print(f"🌍 Name            : {jso.get('name', 'N/A')}")
  print(f"🔑 Token           : {jso.get('token', 'N/A')}")
  print()
  input("Pres enter to go back...")
  clear.clear()
  discordmenu()

def discord_idinfo():
    ascii_idinfo = """
██╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
██║██║  ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
██║██║  ██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
██║██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                             
"""

    clear.clear()
    print(fade.greenblue(ascii_idinfo))

    user_id = input(Fore.LIGHTBLUE_EX+"Enter the Discord user ID : ")
    url = f"https://discordlookup.mesalytic.moe/v1/user/{user_id}" # api DE TIGRE
    res = requests.get(url)
    data = res.json()
    print()
    print(Fore.LIGHTBLUE_EX+"🔎 Discord User Info")
    print(f"👤 Username           : {data.get('username', 'N/A')}")
    print(f"🆔 User ID            : {data.get('id', 'N/A')}")
    print(f"📅 Created At         : {data.get('created_at', 'N/A')}") # Yeah AI for the style of my print , I just ask chatgpt for the style of the print not other
    print(f"🌐 Global Name        : {data.get('global_name', 'N/A')}")
    avatar = data.get("avatar", {})
    print(f"🖼️ Avatar URL         : {avatar.get('link', 'N/A')}")
    print(f"🎞️ Animated Avatar    : {avatar.get('is_animated', False)}")
    banner = data.get("banner", {})
    print(f"🖼️ Banner URL         : {banner.get('link', 'N/A')}")
    print(f"🎞️ Animated Banner    : {banner.get('is_animated', False)}")
    print(f"🎨 Banner Color       : {banner.get('color', 'N/A')}")
    print(f"🎨 Accent Color       : {data.get('accent_color', 'N/A')}")
    badges = data.get("badges", [])
    print(f"🏅 Badges             : {', '.join(badges) if badges else 'None'}")
    print()
    input("Press enter to go back...")
    clear.clear()
    discordmenu()
  
def webhookdel(): 
  ascii_webhookdel = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗  DELETER
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                            
    """
  clear.clear()
  print(fade.greenblue(ascii_webhookdel))
  webhook = input(Fore.LIGHTBLUE_EX+"Enter The webhook URL : ")
  requests.delete(webhook)
  print(f"[INFO] The webhook '{webhook}' got Deleted ")
  print()
  input("Press enter to go back...")
  discordmenu()
  
def discordtokeninfo():
    ascii_tokeninfo= """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██╗███╗   ██╗███████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██║████╗  ██║██╔════╝██╔═══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██║██║ ╚████║██║     ╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝                                          
    """
    clear.clear()
    print(fade.greenblue(ascii_tokeninfo))
    token = input(Fore.LIGHTBLUE_EX+"Enter the Discord token: ")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
    user = response.json()

    full_username       = user.get("username", "None")
    display_name        = user.get("global_name", "None")
    user_id             = user.get("id", "None")
    email               = user.get("email", "None")
    email_verified      = user.get("verified", "None")
    phone_number        = user.get("phone", "None")
    has_2fa             = user.get("mfa_enabled", "None")
    locale              = user.get("locale", "None")
    avatar_hash         = user.get("avatar", "None")
    avatar_decoration   = user.get("avatar_decoration_data", "None")
    public_flags        = user.get("public_flags", "None")
    internal_flags      = user.get("flags", "None")
    banner_hash         = user.get("banner", "None")
    banner_color        = user.get("banner_color", "None")
    accent_color        = user.get("accent_color", "None")
    nsfw_allowed        = user.get("nsfw_allowed", "None")

    print("🔎 Discord Account Info")
    print()
    print(f"👤 Username           : {full_username}")
    print(f"📛 Display Name       : {display_name}")
    print(f"🆔 User ID            : {user_id}")
    print(f"📧 Email              : {email}")
    print(f"✅ Email Verified     : {email_verified}")
    print(f"📱 Phone Number       : {phone_number}")
    print(f"🔐 2FA Enabled        : {has_2fa}")
    print(f"🌍 Locale             : {locale}")
    print(f"🖼️ Avatar Hash        : {avatar_hash}")
    print(f"✨ Avatar Decoration  : {avatar_decoration}")
    print(f"🚩 Public Flags       : {public_flags}")
    print(f"🎌 Internal Flags     : {internal_flags}")
    print(f"🖼️ Banner Hash        : {banner_hash}")
    print(f"🎨 Banner Color       : {banner_color}")
    print(f"🎨 Accent Color       : {accent_color}")
    print(f"🔞 NSFW Allowed       : {nsfw_allowed}")
    print()
    input("Press enter to go back...")
    clear.clear()
    discordmenu()


def webhooksend(): 
  ascii_webhooksend = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗  Sender
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                            
    """
  clear.clear()
  print(fade.greenblue(ascii_webhooksend))
  webhook = input(Fore.LIGHTBLUE_EX+"Enter The webhook URL : ")
  message = input(Fore.LIGHTBLUE_EX+"Enter the message to send : ")
  count = int(input(Fore.LIGHTBLUE_EX+"Enter the number of messages to send  : "))
  message_to_send = {
    "content":f"{message}"
}
  webhook_url = f"{webhook}"
  for _ in range(count):
    requests.post(webhook_url,json=message_to_send)
    print(f'✅ Sent: "{message}"')
  print()
  input("Press enter for return to the menu...")
  discordmenu()
  
  
  
  
  
  

def osintmenu():

  ascii_osint = """
▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███   Made by intrable <3   
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                            OSINT TOOLS
╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────╜

├─ [01] Leakcheck.io Searcher           ├─ [06] GitHub Email Finder             ├─ [11] Subdomains Finder
├─ [02] IP Informations                 ├─ [07] Phone Lookup                    ├─ [12] Email Breach Checker
├─ [03] OsintKit GUI                    ├─ [08] WHOIS Lookup                    ├─ [13] Instagram Lookup
├─ [04] DNS Lookup                      ├─ [09] Email Verifier                  ├─ [14] genderize.io (name to gender)
├─ [05] GitHub Informations Searcher    ├─ [10] All OSINT Websites              ├─ [15] EXIT Osint Menu

                                                                                      
"""
  COLorss = Colorate.Diagonal(Colors.blue_to_red, ascii_osint)
  print(COLorss)
  root_osint = (Fore.LIGHTMAGENTA_EX+"""
┌──(User@Assasin)-[~OSINT]│
└─$>""")
  choiceosint = input(root_osint)
  if choiceosint == "1" or choiceosint == "01":
    clear.clear()
    leakcheck()
  if choiceosint == "2" or choiceosint == "02":
    ip()
  if choiceosint == "3" or choiceosint == "03":
    launch_gui()
  if choiceosint == "4" or choiceosint == "04":
    dnsscan()
  if choiceosint == "5" or choiceosint == "05":
    github_info()
  if choiceosint == "6" or choiceosint == "06":
    githubemail()
  if choiceosint == "7" or choiceosint == "07":
    phonelookup()
  if choiceosint == "8" or choiceosint == "08":
    whhois()
  if choiceosint == "9" or choiceosint == "09":
    emailverif()
  if choiceosint == "10" or choiceosint == "010":
    osintwebsite()
  if choiceosint == "11" or choiceosint == "011":
    subfinder()
  if choiceosint == "12" or choiceosint == "012":
    mailcompromise()
  if choiceosint == "13" or choiceosint == "013":
    clear.clear()
    instagraminfo()
  if choiceosint == "14" or choiceosint == "014":
    genderiz()
  if choiceosint == "15" or choiceosint == "015":
    main()
  else:
    print("[ERROR] Invalide Options")
    time.sleep(1)
    clear.clear()
    osintmenu()
  


def genderiz():
  clear.clear()
  name  = input(Fore.LIGHTBLUE_EX+"enter the Name / full name to genderize (Name to gender) : ")
  res = requests.get(f'https://api.genderize.io/?name={name}')
  data = res.json()
  gender = data.get('gender','N/A')
  propability = data.get('probability','N/A')
  nome = data.get('name','N/A')
  count = data.get('count','N/A')
  print()
  print(Fore.LIGHTBLUE_EX+f"""
       Name : {nome}
       Gender : {gender}
       Propability : {propability}%
       Count : {count}""")
  print()
  input("Press enter to go back...")
  clear.clear()
  osintmenu()
def instagraminfo():
    ascii_insta = """
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║ Lookup
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                                                   
    """
    clear.clear()
    print(fade.greenblue(ascii_insta))
    username  = input(Fore.LIGHTBLUE_EX+"enter the Instagram Username to lookup : ")
    
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)

    print()
    print(Fore.LIGHTBLUE_EX+f"Full Name: {profile.full_name}")
    print(f"Username: {profile.username}")
    print(f"Biography: {profile.biography}")
    print(f"Followers: {profile.followers}")
    print(f"Following: {profile.followees}")
    print(f"Posts: {profile.mediacount}")
    print()
    input("Press enter to go back...")
    clear.clear()
    osintmenu()
    
def mailcompromise():
    ascii_compro = """
██╗     ███████╗ █████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗██╗     
██║     ██╔════╝██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██║██║     
██║     █████╗  ███████║█████╔╝     ██╔████╔██║███████║██║██║     
██║     ██╔══╝  ██╔══██║██╔═██╗     ██║╚██╔╝██║██╔══██║██║██║     
███████╗███████╗██║  ██║██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
      Find if an email is compromised                                                              
    """
    clear.clear()
    print(fade.greenblue(ascii_compro))
    mail = input(Fore.LIGHTBLUE_EX+"enter the email to lookup breach info : ")
    response = requests.get(
        "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email",
        params={"email": mail}
    )

    data = response.json()
    stealers = data.get("stealers", [])

    if not stealers:
        print(f"No issues detected for {mail}")
    else:
        for idx, item in enumerate(stealers, 1):
            print(f"Compromised Device #{idx}")
            print(f"📅 Date Compromised     : {item.get('date_compromised', 'N/A')}")
            print(f"💻 Computer Name        : {item.get('computer_name', 'N/A')}") # Oui , ca fais IA car j'ai demander a chatgpt de styliser le print ): 
            print(f"🖥️ Operating System     : {item.get('operating_system', 'N/A')}")
            print(f"🦠 Malware Path         : {item.get('malware_path', 'N/A')}")
            print(f"🛡️ Antiviruses          : {', '.join(item.get('antiviruses', [])) or 'None'}")
            print(f"🌍 IP Address           : {item.get('ip', 'N/A')}")
            print(f"🔢 User Services        : {item.get('total_user_services', 'N/A')}")
            print(f"🔑 Top Passwords        : {', '.join(item.get('top_passwords', [])) or 'None'}")
            print(f"📧 Top Logins           : {', '.join(item.get('top_logins', [])) or 'None'}")
            input("Press enter for return to the menu...")
            clear.clear()
            osintmenu()



def subfinder():
    ascii_sub = """
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗    
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝    
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║███████╗    Finder 
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║╚════██║    
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████║   
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝                                                                       
    """
    clear.clear()
    print(fade.greenblue(ascii_sub))
    link = input(Fore.LIGHTBLUE_EX+"Enter the domain to scan for subdomains : ")
    res = requests.get(f"https://api.hackertarget.com/hostsearch/?q={link}")
    print()
    print(res.text)
    print()
    save = input("Save as a .txt file ? (Y/N) : ")
    if save == "n" or save == "N":
      clear.clear()
      osintmenu()
    else:
      with open(f"Subdomains-{link}.txt", "w") as file:
        content = file.write(res.text)
        input(f"The file Subdomains-{link}.txt got created ...")
        clear.clear()
        osintmenu()

def osintwebsite():
    ascii_osintweb = """
┌──────────────┐   ┌───────────────┐   ┌───────────────┐
│ [01] Email   │   │ [03] Face     │   │ [05] Username │
│     OSINT    │   │     OSINT     │   │     OSINT     │
│--------------│   │---------------│   │---------------│
│ Email Sites  │   │ Face Sites    │   │ Username Sites│
└──────────────┘   └───────────────┘   └───────────────┘

┌──────────────┐   ┌──────────────┐   ┌───────────────┐
│ [02] IP      │   │ [04] Person  │   │[06] Frameworks│
│     OSINT    │   │     Lookup   │   │               │
│--------------│   │--------------│   │---------------│
│ IP Sites     │   │ Person Sites │   │Framework Sites│
└──────────────┘   └──────────────┘   └───────────────┘

────────────────────────────────────────────────────────────────────────────
                     [07] Return to Main OSINT Menu
────────────────────────────────────────────────────────────────────────────

                                                                                                                                                    
    """
    clear.clear()
    print(fade.greenblue(ascii_osintweb))
    sitechoice = input(Fore.LIGHTBLUE_EX+"Your choice ->  ")
    
    if sitechoice == "1" or sitechoice == "01":
        clear.clear()
        email_osint = [
            "https://epieos.com",
            "https://haveibeenpwned.com",
            "https://emailrep.io",
            "https://hunter.io",
            "https://leakcheck.io",
            "https://snusbase.com",
            "https://dehashed.com"
        ]
        print(Fore.LIGHTBLUE_EX+"Email OSINT Sites:")
        print()
        for site in email_osint:
            print()
            print(site)
        print()
        input("Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "2" or sitechoice == "02":
        clear.clear()
        ip_osint = [
            "https://www.shodan.io",
            "https://ipinfo.io",
            "https://portscanner.online",
            "https://www.abuseipdb.com",
            "https://search.censys.io",
            "https://threatfox.abuse.ch"
        ]
        print(Fore.LIGHTBLUE_EX+"IP OSINT Sites:")
        print()
        for site in ip_osint:
            print()
            print(site)
        print()
        input("Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "3" or sitechoice == "03":
        clear.clear()
        face_osint = [
            "https://pimeyes.com/en",
            "https://yandex.com/images",
            "https://facecheck.id"
        ]
        print(Fore.LIGHTBLUE_EX+"Face OSINT Sites:")
        print()
        for site in face_osint:
            print()
            print(site)
        print()
        input("Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "4" or sitechoice == "04":
        clear.clear()
        person_lookup = [
            "https://www.pagesjaunes.fr",
            "https://webmii.com",
            "https://www.idcrawl.com",
            "https://www.whitepages.com",
            "https://www.truepeoplesearch.com",
            "https://www.peekyou.com"
        ]
        print("Person Lookup Sites:")
        print()
        for site in person_lookup:
            print()
            print(site)
        print()
        input(Fore.LIGHTBLUE_EX+"Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "5" or sitechoice == "05":
        clear.clear()
        username_osint = [
            "https://whatsmyname.app",
            "https://www.namecheckr.com",
            "https://usersearch.org",
            "https://github.com/sherlock-project/sherlock (Github-Tool not Website)",
            "https://github.com/soxoj/maigret (Github-Tool not Website)"
        ]
        print(Fore.LIGHTBLUE_EX+"Username OSINT Sites:")
        print()
        for site in username_osint:
            print()
            print(site)
        print()
        input("Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "6" or sitechoice == "06":
        clear.clear()
        osint_frameworks = [
            "https://osintframework.com",
            "https://www.maltego.com",
            "https://www.spiderfoot.net",
            "https://github.com/lanmaster53/recon-ng (Github-Tool not Website)"
        ]
        print(Fore.LIGHTBLUE_EX+"OSINT Frameworks and Tools:")
        print()
        for site in osint_frameworks:
            print()
            print(site)
        print()
        input("Press enter to go back...")
        clear.clear()
        osintwebsite()

    if sitechoice == "7" or sitechoice == "07":
        clear.clear()
        osintmenu()
        
def emailverif():
    ascii_mailverif = """
███████╗███╗   ███╗ █████╗ ██╗██╗         ██╗   ██╗███████╗██████╗ ██╗███████╗██╗███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██║   ██║█████╗  ██████╔╝██║█████╗  ██║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗     ╚████╔╝ ███████╗██║  ██║██║██║     ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                   
    """
    clear.clear()
    print(fade.greenblue(ascii_mailverif))
    emails = input(Fore.LIGHTBLUE_EX+"Enter the email to verif : ")
    res = requests.get(f"https://api.hunter.io/v2/email-verifier?email={emails}&api_key=2cde17cd082478662ec5f9cf832f4402ad73bc1c")
    respons = res.json()
    data = respons.get('data')
    print("status:", data.get("status"))
    print("result:", data.get("result"))
    print("_deprecation_notice:", data.get("_deprecation_notice"))
    print("score:", data.get("score"))
    print("email:", data.get("email"))
    print("regexp:", data.get("regexp"))
    print("gibberish:", data.get("gibberish"))
    print("disposable:", data.get("disposable"))
    print("webmail:", data.get("webmail"))
    print("mx_records:", data.get("mx_records"))
    print("smtp_server:", data.get("smtp_server"))
    print("smtp_check:", data.get("smtp_check"))
    print("accept_all:", data.get("accept_all"))
    print("block:", data.get("block"))
    print()
    input("Press enter for return to the Menu...")
    clear.clear()
    osintmenu()
def whhois():
    ascii_whois = """
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║ █╗ ██║███████║██║   ██║██║███████╗    ███████╗██║     ███████║██╔██╗ ██║
██║███╗██║██╔══██║██║   ██║██║╚════██║    ╚════██║██║     ██╔══██║██║╚██╗██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║    ███████║╚██████╗██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                       
    """
    clear.clear()
    print(fade.greenblue(ascii_whois))
    link = input(Fore.LIGHTBLUE_EX+"Enter the link to scan with WHOIS : ")
    whhois = whois.whois(link)
    print(whhois)
    print()
    input("Press enter for return to the Menu...")
    clear.clear()
    osintmenu()
    
def leakcheck():
    ascii_art = """   
             *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
            """
    clear.clear()
    print(fade.greenblue(ascii_art))
    search = input(Fore.LIGHTBLUE_EX+"Your leakcheck.io search (Username,email) --> ")
    api = f"https://leakcheck.io/api/public?check={search}"
    res = requests.get(api)
    data = res.json()
    resultat = (f"Status  : {data['success']}")
    resultat2 = (f"fields  : {data['fields']}")
    resultat3 =(f"sources  : {data['sources']}")
    print(f"Status  : {data['success']}")
    print(f"fields  : {data['fields']}")
    print(f"sources  : {data['sources']}")
    print()
    print()
    question = input(Fore.LIGHTBLUE_EX+"Do you want to save the results in a txt file ? Y/N : ") 
    if question == 'Y' or question == 'y':
      with open("result-leakcheck.io.txt", "w") as file:
         file.write(f"{resultat}")
         file.write("-------------------------------")
         file.write(f"{resultat2}")
         file.write("-------------------------------")
         file.write(f"{resultat3}")
         input(Fore.LIGHTWHITE_EX+f"The leakcheck results are enregisred in the file 'result-leakcheck.io'...")  
         clear.clear()
         osintmenu()
    else:
      clear.clear()
      osintmenu()
    
    
  
def phonelookup():
    ascii_art = """
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                             
    """
    clear.clear()
    print(fade.greenblue(ascii_art))
    phone_number = input(Fore.LIGHTBLUE_EX+"Enter the phone number : ")
    response = requests.get(f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_pWHeBCRhv2VgqQ9nFOBTaDEDgVsKeHBa6VE6oghz")
    data = response.json()
    phone_lookup_result = (
    f"[*] Valid              : {data.get('valid')}\n"
    f"[*] Number             : {data.get('number')}\n"
    f"[*] Local Format       : {data.get('local_format')}\n"
    f"[*] International      : {data.get('international_format')}\n"
    f"[*] Country Prefix     : {data.get('country_prefix')}\n"
    f"[*] Country Code       : {data.get('country_code')}\n"
    f"[*] Country Name       : {data.get('country_name')}\n"
    f"[*] Location           : {data.get('location')}\n"
    f"[*] Carrier            : {data.get('carrier')}\n"
    f"[*] Line Type          : {data.get('line_type')}"
    )
    print()
    print(phone_lookup_result)
    print()
    input("Press enter for return to the menu...")
    clear.clear()
    osintmenu()

    
def githubemail():
    ascii_art = """
                /|  /|  -----------------------------------
                ||__||  |                                 |
               /   O O\__  I am a big hacker !!           |
              /          \ I can find your github email ! |
             /      \     \                               |
            /   _    \     \ ------------------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       | Made by intrable (stegman-ux)
 ___/ /   |       |       | Simple script
|____/    c_c_c_C/ \C_c_c_c
    """
    clear.clear()
    print(fade.greenblue(ascii_art))
    Username = input(Fore.LIGHTYELLOW_EX+"Enter the github username --> ")
    repos = input(Fore.LIGHTYELLOW_EX+"Enter the name of the github repositorie --> ")
    res = requests.get(f"https://api.github.com/repos/{Username}/{repos}/commits")
    data = res.json()
    first_commit = data[0] # ici je récpurere le premier commits car sinon le terminal serais remplis de fou
    author = first_commit.get('commit', {}).get('author', {})  # je n'ai pas pue directement obtenir les infos en faisant un data.get donc j'ai cherché de l'aide sur internet , cette ligne n'a pas étais fais par moi ! 
    Email = author.get('email', 'N/A')
    User = author.get('name', 'N/A')
    print(f"""
+----+------------------+-------------+
| ID | Username         | Email       | 
+----+------------------+-------------+ 
| 1  | {User}           | {Email}     |
+----+-------------+------------------+""") # le "id" c'est pour le style et j'me suis donner pour le print en vraie les mec
    input(Fore.WHITE+"Press enter for return to the menu..")
    clear.clear()
    osintmenu()
    
    
  
def ip():
  art = '''
██╗██████╗       ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║           ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
    '''
  clear.clear()
  print(fade.greenblue(art))
  search_ip = input(Fore.LIGHTBLUE_EX+"Enter the ip to lookup --> ")
  res = requests.get(f"http://ip-api.com/json/{search_ip}")
  data = res.json()
  query = f"{data.get('query', 'N/A')}\n"
  status = f"{data.get('status', 'N/A')}\n"
  country = f"{data.get('country', 'N/A')}\n"
  countryCode = f"{data.get('countryCode', 'N/A')}\n"
  region = f"{data.get('region', 'N/A')}\n"
  regionName = f"{data.get('regionName', 'N/A')}\n"
  city = f"{data.get('city', 'N/A')}\n"
  zip = f"{data.get('zip', 'N/A')}\n"
  lat = f"{data.get('lat', 'N/A')}\n"
  lon = f"{data.get('lon', 'N/A')}\n"
  timezone = f"{data.get('timezone', 'N/A')}\n"
  isp = f"{data.get('isp', 'N/A')}\n"
  org = f"{data.get('org', 'N/A')}\n"
  print(f"""
╔══════════════ IP LOOKUP RESULT ══════════════╗
║ Query       : {query}
║ Status      : {status}
║ Country     : {country}
║ Code        : {countryCode}
║ Region      : {region}
║ Region Name : {regionName}
║ City        : {city}
║ ZIP         : {zip}
║ Latitude    : {lat}
║ Longitude   : {lon}
║ Timezone    : {timezone}
║ ISP         : {isp}
║ Org         : {org}
╚══════════════════════════════════════════════╝
  """)
  input(Fore.LIGHTBLUE_EX+"Press enter for return to the menu...")
  clear.clear()
  osintmenu()







def launch_gui():
    app = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("Osint-kit Gui - By intrable")
    app.geometry("900x750")

    def whhois():
        link = entry.get()
        whhois_res = whois.whois(link)
        result_textbox.delete(1.0, ctk.END)
        result_textbox.insert(1.0, whhois_res)

    whois_label = ctk.CTkLabel(
        app,
        text="Whois Lookup",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    whois_label.pack()

    labeel = ctk.CTkLabel(master=app, text="Link of the Website to scan with WHOIS : ")
    labeel.pack()

    entry = ctk.CTkEntry(master=app, width=200, height=10)
    entry.pack()

    button = ctk.CTkButton(master=app, text="Scan Url", command=whhois)
    button.pack()

    label_info = ctk.CTkLabel(master=app, text="Output of whois scan : ")
    label_info.pack()

    result_textbox = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox.pack()

    def ipinfo():
        ip = entry_ip.get()
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        ip_lookup_result = (
            f"[*] Country     : {data.get('country')}\n"
            f"[*] CountryCode : {data.get('countryCode')}\n"
            f"[*] City        : {data.get('city')}\n"
            f"[*] Zip Code    : {data.get('zip')}\n"
            f"[*] Timezone    : {data.get('timezone')}\n"
            f"[*] Org         : {data.get('org')}\n"
            f"[*] Region      : {data.get('region')}\n"
            f"[*] RegionName  : {data.get('regionName')}\n"
            f"[*] AS          : {data.get('as')}\n"
            f"[*] Latitude    : {data.get('lat')}\n"
            f"[*] Longitude   : {data.get('lon')}"
        )
        result_textbox_ip.delete(1.0, ctk.END)
        result_textbox_ip.insert(1.0, ip_lookup_result)

    ipinfo_label = ctk.CTkLabel(
        app,
        text="Ip Lookup",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    ipinfo_label.pack()

    label_ip = ctk.CTkLabel(master=app, text="Ip adress : ")
    label_ip.pack()

    entry_ip = ctk.CTkEntry(master=app, width=200, height=10)
    entry_ip.pack()

    button_ip = ctk.CTkButton(master=app, text="Get ip Infos", command=ipinfo)
    button_ip.pack()

    label_ip2 = ctk.CTkLabel(master=app, text="Ip Infos Output : ")
    label_ip2.pack()

    result_textbox_ip = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox_ip.pack()

    def phone():
        phone_number = entry_phone.get()
        response = requests.get(
            f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_pWHeBCRhv2VgqQ9nFOBTaDEDgVsKeHBa6VE6oghz"
        )
        data = response.json()
        phone_lookup_result = (
            f"[*] Valid              : {data.get('valid')}\n"
            f"[*] Number             : {data.get('number')}\n"
            f"[*] Local Format       : {data.get('local_format')}\n"
            f"[*] International      : {data.get('international_format')}\n"
            f"[*] Country Prefix     : {data.get('country_prefix')}\n"
            f"[*] Country Code       : {data.get('country_code')}\n"
            f"[*] Country Name       : {data.get('country_name')}\n"
            f"[*] Location           : {data.get('location')}\n"
            f"[*] Carrier            : {data.get('carrier')}\n"
            f"[*] Line Type          : {data.get('line_type')}"
        )
        result_textbox_phone.delete(1.0, ctk.END)
        result_textbox_phone.insert(1.0, phone_lookup_result)

    phone_label = ctk.CTkLabel(
        app,
        text="Phone number Lookup",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    phone_label.pack()

    label_phone = ctk.CTkLabel(master=app, text="Phone number : ")
    label_phone.pack()

    entry_phone = ctk.CTkEntry(master=app, width=200, height=10)
    entry_phone.pack()

    button_phone = ctk.CTkButton(master=app, text="Get number Infos.", command=phone)
    button_phone.pack()

    label_phone2 = ctk.CTkLabel(master=app, text="Phone Info Output : ")
    label_phone2.pack()

    result_textbox_phone = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox_phone.pack()
    app.mainloop()


def dnsscan():
    ascii_art = '''
██▄      ▄      ▄▄▄▄▄       █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
█  █      █    █     ▀▄     █    █   █ █   █ █▄█     █  █   █ 
█   █ ██   █ ▄  ▀▀▀▀▄       █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █  █  ▀▄▄▄▄▀        ███▄ ▀████ ▀████ █  █ █   █ █     
███▀  █  █ █                    ▀              █  █▄ ▄█  █    
      █   ██                                  ▀    ▀▀▀    ▀   
                                                            '''
    clear.clear()                                                      
    print(fade.greenblue(ascii_art))
    choice = input(Fore.LIGHTBLUE_EX+"enter the link to scan : ")
    api = "https://api.hackertarget.com/dnslookup/?q=" + choice
    res = requests.get(api)
    results = res.text
    print()
    print(results)
    print()
    input("Press enter for return to the menu...")
    clear.clear()
    osintmenu()
    
    
    

def github_info():
    clear.clear()
    target = input(Fore.LIGHTBLUE_EX+"Enter the github username --> ")
    res = requests.get(f"https://api.github.com/users/{target}")
    data = res.json()
    name = f"{data.get('login', 'N/A')}"
    idd = f"{data.get('id', 'N/A')}"
    avatar_url = f"{data.get('avatar_url', 'N/A')}"
    bio = f"{data.get('bio', 'N/A')}"
    location = f"{data.get('location', 'N/A')}"
    public_repos = f"{data.get('public_repos', 'N/A')}"
    twitter_username = f"{data.get('twitter_username', 'N/A')}"
    followers = f"{data.get('followers', 'N/A')}"
    following = f"{data.get('following', 'N/A')}"
    print()
    print(Fore.LIGHTBLUE_EX+f"""
╠══════════════ GITHUB USER DATA ══════════════╣
║ Login       : {name}
║ ID          : {idd}
║ Avatar URL  : {avatar_url}
║ Bio         : {bio}
║ Location    : {location}
║ Repos       : {public_repos}
║ Twitter     : {twitter_username}
║ Followers   : {followers}
║ Following   : {following}
╚══════════════════════════════════════════════╝
  """)
    print()
    input("Press enter for return to the menu...")
    clear.clear()
    osintmenu()
    


main()
