'''
This is a single cell.

It represents the spatial logic unit of the world.
'''

from dataclasses import dataclass


@dataclass
class Cell:
    elevation: float
    humidity: float