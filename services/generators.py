from parsers import DefinitionEntryResult
from typing import List
import os


def generate_migration(output_dir: str, table: str, column_definitions: List[DefinitionEntryResult]):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #postgresql table filename
    pgsql_table_file = os.path.join(output_dir, f"{table}.sql")
    oracle_select_file = os.path.join(output_dir, f"select_{table}.py")
    pgsql_insert_file = os.path.join(output_dir, f"insert_{table}.py")

    if os.path.exists(pgsql_table_file):
        os.remove(pgsql_table_file)

    if os.path.exists(oracle_select_file):
        os.remove(oracle_select_file)

    if os.path.exists(pgsql_insert_file):
        os.remove(pgsql_insert_file)

    





