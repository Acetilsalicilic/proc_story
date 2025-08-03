'''
This dataclass holds the terrain genertion configuration
'''

from dataclasses import dataclass

@dataclass(frozen=True)
class TerrainConfig:
    size_x: int
    size_y: int

    seed: int
    frequency: float

    sea_level: float