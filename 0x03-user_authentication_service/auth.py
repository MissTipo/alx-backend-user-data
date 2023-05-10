#!/usr/bin/env python3
"""Authenticates the user."""
import bcrypt


def _hash_password(password):
    """Hashes a password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
