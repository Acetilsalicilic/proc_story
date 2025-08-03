import os
import unittest

from sim_logging.ProcLogger import ProgressLogger, SimAbortLogger, SimReportLogger
from proc.ProceduralSimulation import ProceduralSimulation

class TestSimulation(unittest.TestCase):
    def test_ten_steps(self):
        # loggers
        log_file = os.getcwd() + '/results.log'
        mod_name = __name__

        progress = ProgressLogger(log_file, mod_name)
        report = SimReportLogger(log_file, mod_name)
        abort = SimAbortLogger(log_file, mod_name)

        simulation = ProceduralSimulation(1, proc_logger=progress, report_logger=report, abort_logger=abort)
        simulation.simulate(3)
        simulation.report_simulation()