"""CLI for agent-synthetic-failure-injector."""
import sys
import argparse
from .injector import AgentSyntheticFailureInjector, FaultConfig


def main():
    parser = argparse.ArgumentParser(description="Agent Synthetic Failure Injector")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        injector = AgentSyntheticFailureInjector(FaultConfig(failure_rate=0.5, inject_corrupt_json=False))
        for i in range(5):
            try:
                res = injector.execute_with_chaos(lambda: f"Success on run {i}")
                print(f"Run {i}: {res['result']}")
            except Exception as e:
                print(f"Run {i}: Intercepted chaos error: {e}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
