import os

TOKEN = os.environ.get("BOT_TOKEN")

if TOKEN is None:
    raise RuntimeError("BOT_TOKEN environment variable topilmadi")