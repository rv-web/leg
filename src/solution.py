from __future__ import annotations

from itertools import chain
from typing import cast

from model import LegoSet
from queries import Queries
from common.repository import Repository


class Solution(Repository, Queries):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> LegoSet | LegoSet.Minifigure:
        match values:
            case {"number": _}:
                lego_set = LegoSet(**values)
                lego_set.theme = next(
                    LegoSet.Theme[entry.name]
                    for entry in LegoSet.Theme
                    if entry.value == lego_set.theme
                )
                return lego_set
            case {"quantity": _}:
                return LegoSet.Minifigure(**values)

    @property
    def entities(self) -> list[LegoSet]:
        return cast(list[LegoSet], super().entities)

    def group_by_theme(self) -> dict[LegoSet.Theme, list[LegoSet]]:
        return {
            theme: [
                lego_set
                for lego_set in self.entities
            ]
            for theme in {
                lego_set.theme
                for lego_set in self.entities
            }
        }

    def count_of_theme(self, theme: LegoSet.Theme) -> int:
        return len(
            [
                lego
                for lego in self.entities
                if lego.theme == theme
            ]
        )

    def order(self) -> list[LegoSet]:
        return sorted(
            self.entities,
            key=lambda lego: (-len(lego.minifigures), lego.pieces)
        )

    def distinct_minifigure_ids(self) -> set[str]:
        return {
            minifigure.id
            for minifigure in chain.from_iterable(
                [
                    lego_set.minifigures
                    for lego_set in self.entities
                ]
            )
        }

    def set_having_the_greatest_number_minifigures(self) -> LegoSet:
        return next(
            lego
            for lego in self.entities
            if len(lego.minifigures) == max(
                [
                    len(lego.minifigures)
                    for lego in self.entities
                ]
            )
        )


def main() -> None:
    repository = Solution(r"../data/legosets.json")

    for lego_set in repository.entities:
        print(lego_set)


if __name__ == "__main__":
    main()
