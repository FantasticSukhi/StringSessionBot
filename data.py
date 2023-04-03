from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 ѕтαят gєηєяαтιηg ѕєѕѕιση 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 яєтυяη нσмє 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ вσт ѕυρρσят ✨", url="https://t.me/GORILLA_BOTS")],
        [
            InlineKeyboardButton("нσω тσ υѕє❔", callback_data="help"),
            InlineKeyboardButton("🎪 αвσυт 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ вσт ѕυρρσят ♥", url="https://t.me/GORILLA_BOTS")],
    ]

    START = """
нєу {}

ωєℓ¢σмє тσ {}

ιƒ уσυ ∂ση'т тяυѕт тнιѕ вσт, 
1) ѕтσρ яєα∂ιηg тнιѕ мєѕѕαgє
2) ∂єℓєтє тнιѕ ¢нαт

ѕтιℓℓ яєα∂ιηg?
уσυ ¢αη υѕє мє тσ gєηєяαтє ρуяσgяαм (єνєη νєяѕιση 2) αη∂ тєℓєтнση ѕтяιηg ѕєѕѕιση. υѕє вєℓσω вυттσηѕ тσ ℓєαяη мσяє !

By @GORILLA_BOTS
    """

    HELP = """
✨ **𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬** ✨

/about - αвσυт тнє вσт
/help - тнιѕ мєѕѕαgє
/start - ѕтαят тнє вσт
/generate - gєηєяαтє ѕєѕѕιση
/cancel - ¢αη¢єℓ тнє ρяσ¢єѕѕ
/restart - яєѕтαят тнє ρяσ¢єѕѕ
"""

αвσυт = """
**αвσυт тнιѕ вσт** 

тєℓєgяαм вσт тσ gєηєяαтє ρуяσgяαм αη∂ тєℓєтнση ѕтяιηg ѕєѕѕιση ву @gσяιℓℓα_вσтѕ

ѕσυя¢є ¢σ∂є : [¢ℓι¢к нєяє](https://github.com/FantasticSukhi/StringSessionBot)

ƒяαмєωσяк : [ρуяσgяαм](https://docs.pyrogram.org)

ℓαηgυαgє : [ρутнση](https://www.python.org)

∂єνєℓσρєя : @GORILLA_BOTS
    """
