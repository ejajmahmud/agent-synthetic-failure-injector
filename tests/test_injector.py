"""Tests for agent-synthetic-failure-injector."""
import unittest
from agent_synthetic_failure_injector.injector import AgentSyntheticFailureInjector, FaultConfig


class TestFailureInjector(unittest.TestCase):
    def test_guaranteed_failure(self):
        inj = AgentSyntheticFailureInjector(FaultConfig(failure_rate=1.0))
        with self.assertRaises(ConnectionResetError):
            inj.execute_with_chaos(lambda: "ok")

    def test_guaranteed_success(self):
        inj = AgentSyntheticFailureInjector(FaultConfig(failure_rate=0.0))
        res = inj.execute_with_chaos(lambda: "ok")
        self.assertEqual(res["result"], "ok")
