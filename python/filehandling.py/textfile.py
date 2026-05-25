with open(r'C:\Users\User\Downloads\nobel_prize_speech.txt', 'r', encoding='utf-8') as  file_obj:
    content=file_obj.read()
and_count=content.lower().count("and")
print(content)
print(and_count)
