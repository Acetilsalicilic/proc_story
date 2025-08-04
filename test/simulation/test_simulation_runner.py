import unittest

from own_logging.configLogger import ConfigLogger
from own_logging.simulation.simulationRunnerLogger import SimulationRunnerLogger
from simulation.config.mainConfigLoader import MainConfigurationLoader
from simulation.simulationRunner import SimulationRunner

class TestSimRuner(unittest.TestCase):
    def test_simulation_runer(self):
        # load the configs
        main_logger = ConfigLogger("load.log", "main_loader", __name__)
        config_loader = MainConfigurationLoader('test_config.json', main_logger)

        configs = config_loader.get_sim_config()

        main_runner_logger = SimulationRunnerLogger("main.log", "runner", __name__)
        runner = SimulationRunner(configs, main_runner_logger)

        # run it!
        runner.create_simulations()
        runner.run_simulations()