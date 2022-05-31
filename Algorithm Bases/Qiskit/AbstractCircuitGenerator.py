from abc import ABC, abstractmethod
import typing


class AbstractCircuitGenerator(ABC):
    """Abstract base class for circuit """

    @abstractmethod
    def generate_circuit(self):
        """code that generates a quantum circuit for a program or algorithm"""
        pass


class AbstractParametricCircuitGenerator(ABC):
    """Abstract base class for circuit that requires a parameter"""

    @abstractmethod
    def generate_circuit(self, parameter: typing.Any):
        """code that generates a quantum circuit that requires an input"""
        pass
