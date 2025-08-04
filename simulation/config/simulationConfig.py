
from dataclasses import dataclass

from simulation.config.terrainConfig import TerrainConfig


@dataclass
class SimulationConfig:
    terrain_conf: TerrainConfig
    name: str
    log_file:str