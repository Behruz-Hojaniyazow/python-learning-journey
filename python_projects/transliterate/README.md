Uzbek Latin ↔ Cyrillic Transliteration Telegram Bot

A fast and reliable Telegram bot that automatically transliterates Uzbek text between Latin and Cyrillic alphabets.

The bot can:

- Convert Latin → Cyrillic
- Convert Cyrillic → Latin
- Detect the writing system automatically
- Handle mixed-language messages
- Work 24/7 on Railway
- Support modern Uzbek alphabet characters ("o‘", "g‘", "sh", "ch", "ng", etc.)

---

Features

✅ Automatic alphabet detection

✅ Latin → Cyrillic transliteration

✅ Cyrillic → Latin transliteration

✅ Mixed text processing

✅ Telegram Bot API integration

✅ Railway deployment ready

✅ Environment variables support

✅ Production-ready project structure

---

Project Structure

transliterate/
│
├── main_bot.py
├── transliterate.py
├── config.py
├── requirements.txt
├── runtime.txt
└── README.md

---

Installation

Clone the repository:

git clone https://github.com/behruz-hojaniyazow/python-learning-journey.git
cd transliterate

Install dependencies:

pip install -r requirements.txt

---

Configuration

Create a Telegram bot using @BotFather and obtain your bot token.

Set the token as an environment variable:

Linux / Railway

export BOT_TOKEN="YOUR_BOT_TOKEN"

Windows

set BOT_TOKEN=YOUR_BOT_TOKEN

---

Run Locally

python main_bot.py

If everything is configured correctly, you should see:

🤖 Bot ishga tushdi...

---

Railway Deployment

1. Push project to GitHub

git add .
git commit -m "Deploy transliteration bot"
git push origin main

2. Create Railway Project

- Open Railway
- Create New Project
- Deploy from GitHub Repository
- Select your repository

3. Add Environment Variable

Variable name:

BOT_TOKEN

Value:

your_telegram_bot_token

4. Deploy

Railway will automatically:

- Install dependencies
- Create a Python environment
- Launch the bot
- Keep it running 24/7

---

Supported Transliteration

Examples:

Latin → Cyrillic

Assalomu alaykum

↓

Ассалому алайкум

---

Cyrillic → Latin

Ўзбекистон

↓

Oʻzbekiston

---

Mixed Text

Salom Мир

↓

Салом Mir

---

Technologies Used

- Python 3.11+
- pyTelegramBotAPI
- Telegram Bot API
- Railway
- GitHub

---

Requirements

pyTelegramBotAPI==4.34.0

---

Author

Developed by Behruz Hojaniyazow.

GitHub:
https://github.com/Behruz-Hojaniyazow

---

License

This project is open-source and available under the MIT License.