import json
import sqlite3 as sq

with sq.connect(r"data\Thesaurus.db") as con:
    cur = con.cursor()
    cur.execute("drop table if exists Dictionary")
    cur.execute("""create table if not exists Dictionary (
        Expression text not null,
        Definition text not null
    )""")

    data = json.load(open(r"data\data.json"))
    for k, v in data.items():
        for d in v:
            cur.execute("insert into Dictionary (Expression, Definition) values(?, ?)", (k, d))
    con.commit()
