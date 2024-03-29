#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sqlite3


def ensure_connection(func):
    def decorator(*args, **kwargs):
        with sqlite3.connect('database.db') as conn:
            result = func(conn, *args, **kwargs)
        return result
    return decorator


@ensure_connection
def return_history(conn, zodiac_name):
    c = conn.cursor()
    c.execute("SELECT zodiac_text FROM users WHERE zodiac_name = ?", (zodiac_name,))
    history = c.fetchall()
    return history

