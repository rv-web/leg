from abc import abstractmethod, ABC

from model import LegoSet


class Queries(ABC):
    """
    Defines queries that deal with LEGO sets.
    """

    @abstractmethod
    def count_of_theme(self, theme: LegoSet.Theme) -> int:
        """
        Returns the count of LEGO sets that belong to the given theme.

        :param theme: the theme
        :return: the count
        """

    @abstractmethod
    def order(self) -> list[LegoSet]:
        """
        Returns a copy of LEGO sets ordered by:

        * the count of their minifigures in descending order
        * the number of their pieces in ascending order

        :return: the sorted list
        """

    @abstractmethod
    def group_by_theme(self) -> dict[LegoSet.Theme, list[LegoSet]]:
        """
        Groups the sets by their themes.

        :return: the grouping
        """

    @abstractmethod
    def distinct_minifigure_ids(self) -> set[str]:
        """
        Returns the IDs of all the minifigures.

        :return: the IDs
        """

    @abstractmethod
    def set_having_the_greatest_number_minifigures(self) -> LegoSet:
        """
        Returns the set that contains the greatest number of minifigures.

        :return: the set
        """
