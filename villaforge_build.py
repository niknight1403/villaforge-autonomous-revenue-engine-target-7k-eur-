#!/usr/bin/env python3
# Build-Nachweis: uebersetzt jede Python-Quelle und bricht bei Syntaxfehlern ab.
import pathlib, sys

ROOTS = sys.argv[1:] or ["."]
SKIP = {"venv", ".venv", "node_modules", "__pycache__", ".git", "build", "dist"}
fehler = 0
geprueft = 0
for wurzel in ROOTS:
    basispfad = pathlib.Path(wurzel)
    if not basispfad.exists():
        print("Pfad fehlt: " + wurzel)
        fehler += 1
        continue
    for datei in sorted(basispfad.rglob("*.py")):
        if SKIP.intersection(datei.parts):
            continue
        geprueft += 1
        try:
            compile(datei.read_text(encoding="utf-8"), str(datei), "exec")
        except SyntaxError as fehl:
            fehler += 1
            print("Syntaxfehler in " + str(datei) + ": " + str(fehl.msg) + " (Zeile " + str(fehl.lineno) + ")")
        except UnicodeDecodeError:
            fehler += 1
            print("Nicht lesbar: " + str(datei))
print(str(geprueft) + " Dateien uebersetzt, " + str(fehler) + " Fehler")
if geprueft == 0:
    print("Keine Python-Quellen gefunden - dieser Build prueft nichts und gilt nicht als Nachweis")
    sys.exit(2)
sys.exit(0 if fehler == 0 else 1)
