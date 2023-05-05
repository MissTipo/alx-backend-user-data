#!/usr/bin/env python3
"""User authentication."""
from typing import List, TypeVar
from flask import request
from os import getenv


class Auth():
    """Manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return a boolean."""
        if not path or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path\
                    or path.startswith(excluded_path + '/')\
                    or (excluded_path.endswith('/')
                        and path.startswith(excluded_path[:-1])):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return None."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None."""
        return None

    def session_cookie(self, request=None):
        """Return None."""
        if request is None:
            return None
        session_id = getenv('SESSION_NAME')
        return request.cookies.get(session_id)
