import os
import json
import zipfile
import sqlite3
import argparse
from typing import *


UNZIP_PATH = "."
DIFFERENCE_FILE = os.path.join(UNZIP_PATH, "difference.json")
ADD_REQUEST = "INSERT INTO \"{table}\" {columns} VALUES {values};"


def make_change(dbs_path: str, dif_archive: str) -> NoReturn:
    with zipfile.ZipFile(dif_archive, 'r') as zip_ref:
        zip_ref.extractall(UNZIP_PATH)
    with open(DIFFERENCE_FILE, "r", encoding='utf-8') as dif_file:
        difference = json.load(dif_file)
    for new_values in difference["to_add"]:
        db = new_values["db"]
        table = new_values["table"]
        this_db_path = os.path.join(dbs_path, f"{db}", f"{db}.sqlite")
        try:
            conn = sqlite3.connect(this_db_path)
            conn.text_factory = lambda b: b.decode(errors='ignore')
            cursor = conn.cursor()
            for values in new_values["rows"]:
                sql_request = ADD_REQUEST.format(table=table, columns=new_values["columns"], values=values)
                cursor.execute(sql_request)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Some problem with DB \"{db}\", table \"{table}\"")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--db_path', type=str, default="spider/database",
                        help='Path to folders with databases')
    parser.add_argument('--dif_archive', type=str, default="difference.zip",
                        help='Path to file with difference (difference.zip)')

    args = parser.parse_args()
    db_path = args.db_path
    dif_archive = args.dif_archive
    make_change(db_path, dif_archive)
