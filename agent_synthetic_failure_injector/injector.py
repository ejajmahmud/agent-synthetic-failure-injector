"""Core Agent Synthetic Failure Injector implementation."""
import time
import random
from typing import Dict, Any, Callable, Optional


class FaultConfig:
    def __init__(self, failure_rate: float = 0.3, latency_sec: float = 0.0, inject_corrupt_json: bool = False):
        self.failure_rate = failure_rate
        self.latency_sec = latency_sec
        self.inject_corrupt_json = inject_corrupt_json


class AgentSyntheticFailureInjector:
    def __init__(self, config: Optional[FaultConfig] = None):
        self.config = config or FaultConfig()
        self.stats = {"invocations": 0, "faults_injected": 0}

    def execute_with_chaos(self, target_func: Callable, *args, **kwargs) -> Dict[str, Any]:
        self.stats["invocations"] += 1

        # Latency injection
        if self.config.latency_sec > 0:
            time.sleep(self.config.latency_sec)

        # Fault injection
        if random.random() < self.config.failure_rate:
            self.stats["faults_injected"] += 1
            if self.config.inject_corrupt_json:
                return {"error": "MALFORMED_RESPONSE_JSON_{{bad_syntax}"}
            raise ConnectionResetError("Synthetic Chaos: 503 Service Unavailable / Network reset")

        return {"status": "ok", "result": target_func(*args, **kwargs)}
