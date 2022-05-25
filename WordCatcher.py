import codecs
from googletrans import Translator

known_words = {}
text_sentences = []
alfabet = "abcdefghijklmnopqrstuvwxyz"


def google_translate(word):
    translator = Translator()
    ans = translator.translate(word, src='en', dest='ru')
    return ans.text


def read_cfg_file(conf, conf_file_name="WordCatcher.cfg"):
    try:
        with open(conf_file_name, "r") as ff:
            conf["dict_file"] = ff.readline().strip()
            conf["text_file"] = ff.readline().strip()
            conf["new_words_file"] = ff.readline().strip()
    except IOError:
        print("Error with reading cfg file - using defaults")


def read_known_words(filename):
    try:
#        with codecs.open(filename, "r", encoding="utf-8-sig") as ff:
        with open(filename, "r", encoding="utf-8") as ff:
            for line in ff:
                line = line.strip().lower()
#                print(line)
                n = line.find(' ')
                if n == -1:
                    n = 9999
                m = line.find('\t')
                if m == -1:
                    m = 9999
                pos = min(n, m)
                if pos != 9999:
                    entry = line[:pos]
                    translation = line[pos+1:].lstrip()
                    known_words[entry] = translation
    except FileNotFoundError:
        print("File not found")


def read_sentences(filename):
    try:
#        with codecs.open(filename, "r", encoding="utf-8-sig") as ff:
        with open(filename, "r", encoding="utf-8") as ff:
            text = ff.read()
        text.replace('!', '.')
        text.replace('?', '.')
        tmp_lst = text.split('.')
        for t in tmp_lst:
            s = t.strip()
            if len(s) > 0:
                text_sentences.append(s)
        del tmp_lst
        print(len(text_sentences))
    except FileNotFoundError:
        print("File not found")


def analyse_sentences(known_words_file, unknown_words_file):
    translation = ""

#    ff_unknown = codecs.open(unknown_words_file, "w",  encoding="utf-8-sig")
    ff_unknown = open(unknown_words_file, "w",  encoding="utf-8")
    sentence_was_written = False
    for s in text_sentences:
        if sentence_was_written:
            ff_unknown.write('\n')
            sentence_was_written = False

        sentence_words = s.split()
        sentence_was_written = False
        for w in sentence_words:
            ww = w.lower().strip()
            wrd = ""
            for ch in ww:
                if ch.isalpha():
                    wrd += ch
            if len(wrd) == 0:
                continue
            t = known_words.get(wrd, "")
            if t == "":
                print(wrd)
                print(s)
                translation = input('Translation: (<Enter> for skip, "w/з" for write, "stop" for exit): ')
                if translation == "":
                    continue
                elif translation in "wз":
                    google_trans = ""
                    yandex_trans = ""
                    try:
                        google_trans = google_translate(wrd)
                        print(google_trans)
                    except:
                        pass
                    if not sentence_was_written:
                        ff_unknown.write(s + '\n')
                        sentence_was_written = True
                    ff_unknown.write(wrd + '\n')
                    ff_unknown.write(google_trans + '\n')
                elif translation == "stop":
                    break
                else:
                    known_words[wrd] = translation
#                    ff_known.write(wrd + ' ' + translation + '\n')

        if translation == "stop":
            break

#    ff_known = codecs.open(known_words_file, "w",  encoding="utf-8-sig")
    ff_known = open(known_words_file, "w",  encoding="utf-8")
    for w, t in known_words.items():
        ff_known.write(w + ' ' + t + '\n')
    ff_known.close()
    ff_unknown.close()


def main():
    # configuration defaults
    conf = {"dict_file": "20.txt",
            "text_file": "test.txt",
            "new_words_file": "new_words.txt"}
    read_cfg_file(conf)

    read_known_words(conf["dict_file"])
#    for key, value in known_words.items():
#        print(key, value)

    read_sentences(conf["text_file"])
#    for s in text_sentences:
#        print(s)

    analyse_sentences(conf["dict_file"], conf["new_words_file"])


if __name__ == "__main__":
    main()
