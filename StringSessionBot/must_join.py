from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"𝔜𝔬𝔲 𝔪𝔲𝔰𝔱 𝔧𝔬𝔦𝔫 [𝔐𝔶]({link}) 𝔤𝔯𝔬𝔲𝔭 𝔱𝔬 𝔲𝔰𝔢 𝔪𝔢. 𝔄𝔣𝔱𝔢𝔯 𝔧𝔬𝔦𝔫𝔦𝔫𝔤 𝔱𝔯𝔶 𝔞𝔤𝔞𝔦𝔫 !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ 𝔍𝔬𝔦𝔫 ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ℑ'𝔪 𝔫𝔬𝔱 𝔞𝔡𝔪𝔦𝔫 𝔦𝔫 𝔱𝔥𝔢 MUST_JOIN 𝔠𝔥𝔞𝔱 : {MUST_JOIN} !")
