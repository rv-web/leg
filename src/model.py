from __future__ import annotations

from dataclasses import field, dataclass
from enum import Enum


@dataclass
class LegoSet:
    """
    Represents LEGO sets.
    """

    number: str = field(hash=True)
    """number of the set"""
    name: str = field(compare=False)
    """name of the set"""
    pieces: int = field(compare=False)
    """number of pieces in the set"""
    minifigures: list[Minifigure] = field(compare=False, repr=False, default_factory=lambda: [])
    """minifigures of the set"""
    theme: Theme = field(compare=False, default_factory=lambda: LegoSet.Theme.HARRY_POTTER)
    """theme of the set"""

    class Theme(Enum):
        """
        Represents themes of LEGO sets.

        * CITY = "City"
        * HARRY_POTTER = "Harry Potter"
        * STAR_WARS = "Star Wars"
        * CREATOR_EXPERT = "Creator Expert"
        """
        CITY = "City"
        HARRY_POTTER = "Harry Potter"
        STAR_WARS = "Star Wars"
        CREATOR_EXPERT = "Creator Expert"

    @dataclass
    class Minifigure:
        """
        Represents minifigures.
        """
        id: str = field(hash=True)
        """ID of the minifigure"""
        name: str = field(compare=False)
        """name of the minifigure"""
        quantity: int = field(compare=False)
        """quantity of the minifigure"""
