import sqlite3 as sq

with sq.connect(r"data\Thesaurus.db") as con:
    cur = con.cursor()
    cur.execute("select * from Dictionary where Expression='got'")
    result = cur.fetchall()
    for r in result:
        print(f"{r[0]} -> {r[1]}")

    cur.execute("SELECT COUNT(*) FROM Dictionary")
    result = cur.fetchall()
    print(result[0][0])
