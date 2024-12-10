from datetime import datetime
from typing import Literal

import yaml
from pydantic import BaseModel

__all__ = ["dump_yaml", "load_yaml", "SimulationConfig"]


def dump_yaml(data: BaseModel) -> str:
    """Dump a pydantic model to a yaml string."""
    return yaml.safe_dump(data.model_dump(), default_flow_style=False)


def load_yaml(data: str, model: BaseModel) -> BaseModel:
    """Load a yaml string into a pydantic model."""
    return model.model_validate(yaml.safe_load(data))


class SimulationConfig(BaseModel):
    """A model for the configuration file."""
    kernel: Literal["no-beaching", "instant-beaching", "proba-beaching"]
    n_particles: int
    start_time: datetime

    def get_folder_name(self) -> str:
        """This can be customized by the user"""
        return datetime.now().strftime("%Y%m%d-%H%M%S")
