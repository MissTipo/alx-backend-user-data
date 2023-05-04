#!/usr/bin/env python3
"""Session authentication module."""
from api.v1.auth.auth import Auth


class SessionAuth():
    """Inherits from Auth."""
    user_id_by_session_id = {}
    pass
