fout = open("PlanetEarth_1.txt", "w")
with open("PlanetEarth_1.srt", "r") as fin:
    for line in fin:
        line = line.strip()
        if len(line) == 0 or ':' in line[:2]:
            continue
        fout.write(line + '\n')
print("All done!")
fout.close()