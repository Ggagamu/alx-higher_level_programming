#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """Prevents dynamic intatiation except, first_name"""
    __slots__ = ['first_name']
