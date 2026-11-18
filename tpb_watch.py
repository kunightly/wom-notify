import json
import os
import requests
from telegram import send_gmt_message

URL = "https://apibay.org/q.php?q=top100:207"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tpb_state.json")
HEADERS = {"User-Agent": "Knightly-WOM-Notify/1.0"}
MARK_NEW = True   # put 🆕 in front of titles that weren't on yesterday's list
TOP_N = 15        # how many titles to track and show
CHUNK = 3500      # max characters per Telegram message


def fetch_names():
    r = requests.get(URL, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return [item["name"] for item in r.json() if item.get("id") != "0"][:TOP_N]


def load_previous():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_current(names):
    with open(STATE_FILE, "w") as f:
        json.dump(names, f)


def send_chunks(lines):
    chunk = ""
    for line in lines:
        if chunk and len(chunk) + len(line) + 1 > CHUNK:
            send_gmt_message(chunk.strip())
            chunk = ""
        chunk += line + "\n"
    if chunk.strip():
        send_gmt_message(chunk.strip())


def check_tpb():
    try:
        current = fetch_names()
    except Exception as e:
        print(f"TPB check failed: {e}")
        return

    if not current:
        print("TPB returned an empty list, skipping.")
        return

    previous = load_previous()
    save_current(current)

    if previous is None:
        print("TPB baseline saved. No notification on first run.")
        return

    if current == previous:
        print("TPB: no changes.")
        return

    prev_set = set(previous)
    lines = ["🎬 Top 15 changed since yesterday:", ""]
    for name in current:
        if MARK_NEW and name not in prev_set:
            lines.append(f"🆕 {name}")
        else:
            lines.append(name)

    send_chunks(lines)


if __name__ == "__main__":
    check_tpb()