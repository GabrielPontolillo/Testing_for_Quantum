from AbstractCircuitGenerator import AbstractCircuitGenerator
from qiskit import QuantumCircuit, Aer, execute
from math import pi


class QuantumFourierTransform(AbstractCircuitGenerator):
    """

    """
    def __init__(self, size: int = 4):
        self.size = size

    def generate_circuit(self):
        qc = QuantumCircuit(self.size)
        return self.qft_recursive_loop(qc, self.size)

    def qft_recursive_loop(self, circuit: QuantumCircuit, n: int):
        if n == 0:
            return circuit
        n -= 1
        circuit.h(n)
        for qubit in range(n):
            circuit.cp(pi/2**(n-qubit), qubit, n)
        return self.qft_recursive_loop(circuit, n)


if __name__ == "__main__":
    print(QuantumFourierTransform().generate_circuit())
