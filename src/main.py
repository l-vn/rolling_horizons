import logging
import time

from orchestrator.orchestrator import Orchestrator
from tools.run_configuration import RunConfiguration

def main() -> None:
    logger = logging.getLogger()
    start_time = time.process_time()
    
    run_configuration = RunConfiguration("","")
    orchestrator = Orchestrator(run_configuration)
    orchestrator.run()
    
    end_time = time.process_time()
    logger.info(f"Time to process: {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()