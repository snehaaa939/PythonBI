#Read file nobel_prize_speech.txt and display most repeated word on it.
with open(r"C:\Users\User\Downloads\nobel_prize_speech.txt", "r", encoding="utf-8", errors="ignore") as file:
     content = file.read().lower()
