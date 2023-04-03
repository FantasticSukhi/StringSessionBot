from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

from data import Data


ask_ques = "𝐂𝐡𝐨𝐨𝐬𝐞 𝐭𝐡𝐚𝐭 𝐖𝐡𝐚𝐭 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐨𝐫 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧"
buttons_ques = [
    [
        InlineKeyboardButton("ρуяσgяαм", callback_data="pyrogram"),
        InlineKeyboardButton("тєℓєтнση", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ρуяσgяαм вσт", callback_data="pyrogram_bot"),
        InlineKeyboardButton("тєℓєтнση вσт", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "тєℓєтнση"
    else:
        ty = "ρуяσgяαм ν2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"ѕтαятιηg {ty} ѕєѕѕιση gєηєяαтιση...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'ρℓєαѕє ѕєη∂ уσυя `αρι_ι∂`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('𝙉𝙤𝙩 𝙖 𝙫𝙖𝙡𝙞𝙙 𝘼𝙋𝙄_𝙄𝘿 (𝙬𝙝𝙞𝙘𝙝 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙖𝙣 𝙞𝙣𝙩𝙚𝙜𝙚𝙧). 𝙋𝙡𝙚𝙖𝙨𝙚 𝙨𝙩𝙖𝙧𝙩 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙞𝙣𝙜 𝙨𝙚𝙨𝙨𝙞𝙤𝙣 𝙖𝙜𝙖𝙞𝙣.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'ρℓєαѕє ѕєη∂ уσυя `αρι_нαѕн`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "ησω ρℓєαѕє ѕєη∂ уσυя `ρнσηє_ηυмвєя` αℓσηg ωιтн тнє ¢συηтяу ¢σ∂є. \nєχαмρℓє : `+19876543210`'"
    else:
        t = "ησω ρℓєαѕє ѕєη∂ уσυя `вσт_тσкєη` \nєχαмρℓє : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("ѕєη∂ιηg σтρ...")
    else:
        await msg.reply("ℓσggιηg αѕ вσт υѕєя...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`αρι_ι∂` αη∂ `αρι_нαѕн` ¢σмвιηαтιση ιѕ ιηναℓι∂. ρℓєαѕє ѕтαят gєηєяαтιηg ѕєѕѕιση αgαιη.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`ρнσηє_ηυмвєя` ιѕ ιηναℓι∂. ρℓєαѕє ѕтαят gєηєяαтιηg ѕєѕѕιση αgαιη.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "ρℓєαѕє ¢нє¢к ƒσя αη σтρ ιη σƒƒι¢ιαℓ тєℓєgяαм α¢¢συηт. ιƒ уσυ gσт ιт, ѕєη∂ σтρ нєяє αƒтєя яєα∂ιηg тнє вєℓσω ƒσямαт. \ηιƒ σтρ ιѕ `12345`, **ρℓєαѕє ѕєη∂ ιт αѕ** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('тιмє ℓιмιт яєα¢нє∂ σƒ 10 мιηυтєѕ. ρℓєαѕє ѕтαят gєηєяαтιηg ѕєѕѕιση αgαιη.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('𝐎𝐓𝐏 𝐢𝐬 𝐢𝐧𝐯𝐚𝐥𝐢𝐝. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐭𝐚𝐫𝐭 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐚𝐠𝐚𝐢𝐧.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('𝐎𝐓𝐏 𝐢𝐬 𝐞𝐱𝐩𝐢𝐫𝐞𝐝. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐭𝐚𝐫𝐭 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐚𝐠𝐚𝐢𝐧.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '𝔜𝔬𝔲𝔯 𝔞𝔠𝔠𝔬𝔲𝔫𝔱 𝔥𝔞𝔰 𝔢𝔫𝔞𝔟𝔩𝔢𝔡 𝔱𝔴𝔬-𝔰𝔱𝔢𝔭 𝔳𝔢𝔯𝔦𝔣𝔦𝔠𝔞𝔱𝔦𝔬𝔫. 𝔓𝔩𝔢𝔞𝔰𝔢 𝔭𝔯𝔬𝔳𝔦𝔡𝔢 𝔱𝔥𝔢 𝔭𝔞𝔰𝔰𝔴𝔬𝔯𝔡.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('𝐓𝐢𝐦𝐞 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝 𝐨𝐟 𝟓 𝐦𝐢𝐧𝐮𝐭𝐞𝐬. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐭𝐚𝐫𝐭 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐚𝐠𝐚𝐢𝐧.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('ιηναℓι∂ ραѕѕωσя∂ ρяσνι∂є∂. ρℓєαѕє ѕтαят gєηєяαтιηg ѕєѕѕιση αgαιη.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} 𝔖𝔱𝔯𝔦𝔫𝔤 𝔖𝔢𝔰𝔰𝔦𝔬𝔫** \n\n`{string_session}` \n\n𝕲𝖊𝖓𝖊𝖗𝖆𝖙𝖊𝖉 𝖇𝖞 @GORILLA_SESSION_GBOT
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "𝔖𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔤𝔢𝔫𝔢𝔯𝔞𝔱𝔢𝔡 {} 𝔰𝔱𝔯𝔦𝔫𝔤 𝔰𝔢𝔰𝔰𝔦𝔬𝔫. \n\n𝕻𝖑𝖊𝖆𝖘𝖊 𝖈𝖍𝖊𝖈𝖐 𝖞𝖔𝖚𝖗 𝖘𝖆𝖛𝖊𝖉 𝖒𝖊𝖘𝖘𝖆𝖌𝖊𝖘!".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancℭ𝔞𝔫𝔠𝔢𝔩𝔩𝔢𝔡 𝔱𝔥𝔢 𝔭𝔯𝔬𝔠𝔢𝔰𝔰!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("ℜ𝔢𝔰𝔱𝔞𝔯𝔱𝔢𝔡 𝔱𝔥𝔢 𝔅𝔬𝔱!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("ℭ𝔞𝔫𝔠𝔢𝔩𝔩𝔢𝔡 𝔱𝔥𝔢 𝔤𝔢𝔫𝔢𝔯𝔞𝔱𝔦𝔬𝔫 𝔭𝔯𝔬𝔠𝔢𝔰𝔰!", quote=True)
        return True
    else:
        return False
