import os, random, pathlib, sys, requests

TOKEN   = os.environ['TOKEN']        # берём из Secrets
CHAT_ID = os.environ['CHAT_ID']

# По умолчанию читаем «утренний» список.
# Но если передан аргумент (evening), берём второй.
file_name = (
    'messages_evening.txt' if len(sys.argv) > 1 and sys.argv[1] == 'evening'
    else 'messages_morning.txt'
)

msg_file = pathlib.Path(__file__).with_name(file_name)
with msg_file.open(encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

text = random.choice(lines)          # случайная фраза

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": text}
)
