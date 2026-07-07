from dataclasses import dataclass


@dataclass
class Constraint:

    name: str

    description: str

    hard: bool = True