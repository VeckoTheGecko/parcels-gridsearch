from models import SimulationConfig, dump_yaml
from pathlib import Path
from loguru import logger
import sys
import time
from  contextlib import contextmanager
from typing import Generator


DATA_FOLDER = Path("data")
DATA_FOLDER.mkdir(exist_ok=True)

def NoBeachingKernel():
    ...

def InstantBeachingKernel():
    ...

def ProbaBeachingKernel():
    ...

KERNELS = {
    "no-beaching": NoBeachingKernel,
    "instant-beaching": InstantBeachingKernel,
    "proba-beaching": ProbaBeachingKernel,
}

@contextmanager
def redirect_stdout(path: Path) -> Generator[None, None, None]:
    """Instead of having print going to the console, redirect it to a file."""
    orig_stdout = sys.stdout
    f = open(path, 'w')
    sys.stdout = f
    yield
    sys.stdout = orig_stdout
    f.close()

@contextmanager
def add_logger_source(path: Path) -> Generator[None, None, None]:
    source = logger.add(path)
    yield
    logger.remove(source)

def run_simulation(config: SimulationConfig, folder: Path) -> None:
    kernel = KERNELS[config.kernel]
    logger.debug(f"Running simulation {config!r}")
    logger.debug(f"Doing simulation things with kernel {kernel}")
    print("Redirected print statement")

    # Running simulation
    time.sleep(3)

    zarr_path = folder / "output.zarr"

    ...

    logger.debug(f"Saving data to {zarr_path}")

    return


def main():
    simulations = [
        SimulationConfig(kernel="no-beaching", n_particles=100, start_time="2021-01-01T00:00:00"),
        SimulationConfig(kernel="instant-beaching", n_particles=100, start_time="2021-01-01T00:00:00"),
        SimulationConfig(kernel="proba-beaching", n_particles=100, start_time="2021-01-01T00:00:00"),
    ]
    for sim in simulations:
        sim_folder = DATA_FOLDER / sim.get_folder_name()
        sim_folder.mkdir()

        # Save configuration to a file
        with open(sim_folder / "config.yaml", "w") as f:
            f.write(dump_yaml(sim))
        
        with redirect_stdout(sim_folder / "simulation_stdout.txt"), add_logger_source(sim_folder / "simulation.log"):
            try:
                run_simulation(config=sim, folder=sim_folder)
            except Exception as e:
                logger.exception(e)


if __name__ == "__main__":
    main()