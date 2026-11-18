"""Copia la plantilla Ren’Py a un destino vacío y personaliza su identidad."""
import argparse
import json
import re
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path)
    parser.add_argument("--nombre", required=True)
    parser.add_argument("--id", required=True, help="Identificador único en minúsculas y guiones")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.id):
        parser.error("--id debe usar minúsculas, números y guiones")
    if args.destino.exists() and (not args.destino.is_dir() or any(args.destino.iterdir())):
        parser.error("el destino debe estar vacío")
    source = Path(__file__).resolve().parents[1] / "assets" / "renpy"
    shutil.copytree(source, args.destino, dirs_exist_ok=True)
    script = args.destino / "game" / "script.rpy"
    text = script.read_text()
    text = text.replace('"Juego docente"', json.dumps(args.nombre, ensure_ascii=False))
    text = text.replace('"juego-docente-ejemplo"', json.dumps(args.id))
    text = text.replace('"juego_docente"', json.dumps(args.id.replace("-", "_")))
    script.write_text(text)
    print(args.destino.resolve())

if __name__ == "__main__":
    main()
