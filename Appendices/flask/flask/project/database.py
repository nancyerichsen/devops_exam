import sqlite3
import hashlib
import datetime
import os
import psycopg2
from flask import current_app, has_app_context

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_db_connection(db_name=None):
    if has_app_context():
        database_url = current_app.config.get("DATABASE_URL")
        if database_url:
            print(f"Using PostgreSQL DB: {database_url}")
            return psycopg2.connect(database_url)

        test_dir = current_app.config.get("TEST_DB_DIR")
        if test_dir and db_name:
            full_path = os.path.join(test_dir, db_name)
            print(f"Using TEST DB: {full_path}")
            return sqlite3.connect(full_path)

    if db_name:
        full_path = os.path.join(BASE_DIR, "database_file", db_name)
        print(f"FALLBACK TO REAL DB: {full_path}")
        return sqlite3.connect(full_path)

    raise ValueError("Database name must be provided for SQLite connection.")


# -------------------- User Functions --------------------

def list_users():
    with get_db_connection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users;")
        return [x[0] for x in cursor.fetchall()]


def verify(id, pw):
    with get_db_connection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT pw FROM users WHERE id = %s;" if isinstance(conn, psycopg2.extensions.connection)
            else "SELECT pw FROM users WHERE id = ?;",
            (id,)
        )
        row = cursor.fetchone()
        return row[0] == hashlib.sha256(pw.encode()).hexdigest() if row else False


def delete_user_from_db(id):
    id_tuple = (id,)

    with get_db_connection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE id = %s;" if isinstance(conn, psycopg2.extensions.connection)
            else "DELETE FROM users WHERE id = ?;",
            id_tuple
        )

    with get_db_connection("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM notes WHERE "user" = %s;' if isinstance(conn, psycopg2.extensions.connection)
            else "DELETE FROM notes WHERE user = ?;",
            id_tuple
        )

    with get_db_connection("images.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM images WHERE "owner" = %s;' if isinstance(conn, psycopg2.extensions.connection)
            else "DELETE FROM images WHERE owner = ?;",
            id_tuple
        )


def add_user(id, pw):
    with get_db_connection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (%s, %s);" if isinstance(conn, psycopg2.extensions.connection)
            else "INSERT INTO users VALUES (?, ?);",
            (id.upper(), hashlib.sha256(pw.encode()).hexdigest())
        )


# -------------------- Note Functions --------------------

def read_note_from_db(id):
    with get_db_connection("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT note_id, timestamp, note FROM notes WHERE "user" = %s;' if isinstance(conn, psycopg2.extensions.connection)
            else "SELECT note_id, timestamp, note FROM notes WHERE user = ?;",
            (id.upper(),)
        )
        return cursor.fetchall()


def match_user_id_with_note_id(note_id):
    with get_db_connection("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT "user" FROM notes WHERE note_id = %s;' if isinstance(conn, psycopg2.extensions.connection)
            else "SELECT user FROM notes WHERE note_id = ?;",
            (note_id,)
        )
        row = cursor.fetchone()
        return row[0] if row else None


def write_note_into_db(id, note_to_write):
    current_timestamp = str(datetime.datetime.now())
    note_id = hashlib.sha1((id.upper() + current_timestamp).encode()).hexdigest()

    with get_db_connection("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO notes("user", timestamp, note, note_id) VALUES (%s, %s, %s, %s);'
            if isinstance(conn, psycopg2.extensions.connection)
            else "INSERT INTO notes VALUES (?, ?, ?, ?);",
            (id.upper(), current_timestamp, note_to_write, note_id)
        )


def delete_note_from_db(note_id):
    with get_db_connection("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM notes WHERE note_id = %s;" if isinstance(conn, psycopg2.extensions.connection)
            else "DELETE FROM notes WHERE note_id = ?;",
            (note_id,)
        )


# -------------------- Image Functions --------------------

def image_upload_record(uid, owner, image_name, timestamp):
    with get_db_connection("images.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO images(uid, "owner", name, timestamp) VALUES (%s, %s, %s, %s);'
            if isinstance(conn, psycopg2.extensions.connection)
            else "INSERT INTO images VALUES (?, ?, ?, ?);",
            (uid, owner, image_name, timestamp)
        )


def list_images_for_user(owner):
    with get_db_connection("images.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT uid, timestamp, name FROM images WHERE "owner" = %s;'
            if isinstance(conn, psycopg2.extensions.connection)
            else "SELECT uid, timestamp, name FROM images WHERE owner = ?;",
            (owner,)
        )
        return cursor.fetchall()


def match_user_id_with_image_uid(image_uid):
    with get_db_connection("images.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT "owner" FROM images WHERE uid = %s;' if isinstance(conn, psycopg2.extensions.connection)
            else "SELECT owner FROM images WHERE uid = ?;",
            (image_uid,)
        )
        row = cursor.fetchone()
        return row[0] if row else None


def delete_image_from_db(image_uid):
    with get_db_connection("images.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM images WHERE uid = %s;" if isinstance(conn, psycopg2.extensions.connection)
            else "DELETE FROM images WHERE uid = ?;",
            (image_uid,)
        )


# -------------------- Debug/Test --------------------

if __name__ == "__main__":
    print(list_users())
