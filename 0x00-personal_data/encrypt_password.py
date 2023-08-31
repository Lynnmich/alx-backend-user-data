#!/usr/bin/env python3
"""Functions for handling user passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that takes a str argument and encodes it and returns a
    hashed password which is a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
