#!/usr/bin/python3
"""MyInt class documentation"""


class MyInt(int):
    """Create MyInt class"""

    def __eq__(self, other):
        """Change != to =="""
        return int(self) != other

    def __ne__(self, other):
        """Change == to !="""
        return int(self) == other
