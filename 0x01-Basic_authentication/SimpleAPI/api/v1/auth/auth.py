#!/usr/bin/env python3
"""User authentication."""
from typing import List, TypeVar
from flask import request


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None."""
        return None
