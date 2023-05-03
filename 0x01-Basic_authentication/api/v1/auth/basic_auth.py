#!/usr/bin/env python3
"""Basic Auth."""
from api.v1.auth.auth import Auth
import base64


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
        '''else:
            if len(authorization_header.split(' ')) > 1:
                return authorization_header.split(' ')[1]
            return None'''
