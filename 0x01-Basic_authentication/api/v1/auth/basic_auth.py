#!/usr/bin/env python3
"""Basic Auth."""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Inherits from Auth."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return Base64 part of Authorization."""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1] if len(
            authorization_header.split(' ')) > 1 else None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the decoded value of a Base64 string."""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Return the user email and password from the Base64 decoded value."""
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return (None, None)
        elif ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            split_base64 = decoded_base64_authorization_header.split(':')
            if len(split_base64) == 2:
                return (split_base64[0], split_base64[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Return the User instance based on his email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        elif user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
