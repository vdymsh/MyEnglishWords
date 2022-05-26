import sqlite3 as sq

my_dict = {}

with open(r"data\5000.txt", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip().replace(',', ' - ')
        line = line.replace(r'/', ' - ')
        lst = line.split(' - ')
        for i in range(len(lst)):
            lst[i] = lst[i].strip()
        tmp = my_dict.get(lst[0], [])
        tmp.extend(lst[1:])
        my_dict[lst[0]] = tmp

con = sq.connect("my_english_words.db")
cur = con.cursor()
with open(r"DB_Structure.sql", 'r', encoding="utf-8") as f:
    sql = f.read()
    cur.executescript(sql)

frequent = [" "]
with open(r"data\20k.txt", 'r', encoding="utf-8") as f:
    word_position = 1
    for line in f:
        item = line.strip()
        cur.execute(r"insert into word_frequent_list (word_position, word,  word_type) values(?, ?, ?)",
                    (word_position, item, 0))
        frequent.append(item)
        word_position += 1
con.commit()

# word_meaning_id
# word_position
# meaning
word_position = 0
for fr in frequent:
    meanings = my_dict.get(fr, [])
    for meaning in meanings:
        cur.execute(r"insert into word_meanings (word_position, meaning) values(?, ?)", (word_position, meaning))
    word_position += 1
con.commit()


print("All done!")
