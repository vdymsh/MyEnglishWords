import sqlite3 as sq
import os


def read_cfg_file(conf, conf_file_name="engine.cfg"):
    try:
        with open(conf_file_name, "r") as ff:
            conf["text_file"] = ff.readline().strip()
    except IOError:
        print("Error with reading cfg file - using defaults")


def db_connect():
    con = None
    try:
        con = sq.connect("my_english_words.db")
    except Exception as e:
        print(e)
        con = None
    finally:
        return con


def read_sentences(filename):
    text_sentences = []
    try:
        with open(filename, "r", encoding="utf-8") as ff:
            text = ff.read()
        text = text.replace("\"", "\'")
        text = text.replace("!", "!<")
        text = text.replace("?", "?<")
        text = text.replace(".", ".<")
        tmp_lst = text.split("<")
        for t in tmp_lst:
            s = t.replace('\n', ' ').strip()
            if len(s) > 0:
                text_sentences.append(s)
        del tmp_lst
#        print(len(text_sentences))
    except FileNotFoundError:
        print("File not found")
    finally:
        return text_sentences


def analyse_sentences(text_sentences):
    os.system("cls")
    try:
        con = db_connect()
        cur = con.cursor()
        for s in text_sentences:
            sentence_words = s.split()
            for w in sentence_words:
                ww = w.lower().strip()
                wrd = ""
                for ch in ww:
                    if ch.isalpha():
                        wrd += ch
                if len(wrd) == 0:
                    continue
                cur.execute(r"SELECT * from word_frequent_list where word =:Id", {"Id": wrd})
                res = cur.fetchall()
                if len(res) >= 1 and len(res[0]) >= 3:
                    print(res[0][0], res[0][1], res[0][2])
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


def main():
    conf = {}
    read_cfg_file(conf)
    text_sentences = read_sentences(conf["text_file"])
    # for t in text_sentences:
    #     print(t)
    analyse_sentences(text_sentences)
    con = db_connect()
    cur = con.cursor


if __name__ == "__main__":
    main()
