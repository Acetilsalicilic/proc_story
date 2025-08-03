from simulation.config.simulationConfig import SimulationConfig
from simulation.simulation import Simulation


class SimulationRunner:
    __configs: list[SimulationConfig]
    __simulations: list[Simulation]


    def __init__(self, sim_config: list[SimulationConfig]):
        self.__configs = sim_config
        self.__simulations = list()
    

    def create_simulations(self):
        for config in self.__configs:
            self.__simulations.append(Simulation(config))


    def run_simulations(self):
        for simulation in self.__simulations:
            print(simulation.get_name() + ':')
            simulation.simulate()