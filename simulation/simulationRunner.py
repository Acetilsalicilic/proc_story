from own_logging.simulation.simulationLogger import SimulationLogger
from own_logging.simulation.simulationRunnerLogger import SimulationRunnerLogger
from simulation.config.simulationConfig import SimulationConfig
from simulation.simulation import Simulation


class SimulationRunner:
    __configs: list[SimulationConfig]
    __simulations: list[Simulation]

    __logger: SimulationRunnerLogger


    def __init__(self, sim_config: list[SimulationConfig], logger: SimulationRunnerLogger):
        self.__logger = logger
        self.__configs = sim_config
        self.__simulations = list()
    

    def create_simulations(self):
        for number, config in enumerate(self.__configs):
            logger = SimulationLogger(config.log_file, number, config.name, config.name, __name__)
            self.__simulations.append(Simulation(config, logger))


    def run_simulations(self):
        for simulation in self.__simulations:
            print(simulation.get_name() + ':')
            simulation.simulate()