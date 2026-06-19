import re
import time
import telebot

from transliterate import to_cyrillic, to_latin
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

CYRILLIC_CHARS = (
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    "ўқғҳЎҚҒҲ"
)


def is_cyrillic(text: str) -> bool:
    return any(char in CYRILLIC_CHARS for char in text)


def detect_text_type(text: str) -> str:
    """
    whole_cyrillic
    whole_latin
    mixed
    """

    has_cyr = False
    has_lat = False

    for char in text:
        if char in CYRILLIC_CHARS:
            has_cyr = True
        elif char.isalpha():
            has_lat = True

    if has_cyr and has_lat:
        return "mixed"

    if has_cyr:
        return "whole_cyrillic"

    return "whole_latin"


def smart_transliterate(text: str) -> str:
    """
    Aralash matn uchun.
    Har bir so'z ustida alohida ishlaydi.
    """

    parts = re.split(r"(\s+)", text)

    result = []

    for part in parts:

        if not part.strip():
            result.append(part)
            continue

        if is_cyrillic(part):
            result.append(to_latin(part))
        else:
            result.append(to_cyrillic(part))

    return "".join(result)


@bot.message_handler(commands=["start"])
def start_handler(message):

    text = (
        "👋 Assalomu alaykum!\n\n"
        "🔄 Lotin ↔ Kirill transliteratsiya boti.\n\n"
        "• Lotin matn yuborsangiz → Kirillga o'tkazaman.\n"
        "• Kirill matn yuborsangiz → Lotinga o'tkazaman.\n"
        "• Aralash matn yuborsangiz → Har bir so'zni alohida o'zgartiraman."
    )

    bot.reply_to(message, text)


@bot.message_handler(commands=["help"])
def help_handler(message):

    text = (
        "📚 Foydalanish:\n\n"
        "Salom dunyo\n"
        "➡️ Салом дунё\n\n"
        "Салом дунё\n"
        "➡️ Salom dunyo\n\n"
        "Salom друг\n"
        "➡️ Салом drug"
    )

    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def transliterate_handler(message):

    text = message.text

    if text is None:
        return

    text = text.strip()

    if not text:
        bot.reply_to(
            message,
            "❌ Bo'sh matn yuborildi."
        )
        return

    try:

        text_type = detect_text_type(text)

        if text_type == "whole_cyrillic":
            result = to_latin(text)

        elif text_type == "whole_latin":
            result = to_cyrillic(text)

        else:
            result = smart_transliterate(text)

        bot.reply_to(message, result)

    except Exception as error:

        print(f"Xatolik: {error}")

        bot.reply_to(
            message,
            "❌ Xatolik yuz berdi."
        )


def run_bot():

    while True:

        try:

            print("🤖 Bot ishga tushdi...")

            bot.infinity_polling(
                timeout=60,
                long_polling_timeout=60,
                skip_pending=True
            )

        except Exception as error:

            print(f"Bot to'xtadi: {error}")

            time.sleep(5)


if __name__ == "__main__":
    run_bot()