from numpy import double
from AbstractCircuitGenerator import  AbstractParametricCircuitGenerator
from QuantumFourierTransform import QuantumFourierTransform
from qiskit import QuantumCircuit
from math import pi


class QuantumPhaseEstimation(AbstractParametricCircuitGenerator):
    """

    """
    def __init__(self, size: int = 4):
        self.size = size

    def generate_circuit(self, phase: float):
        return self.generalised_qpe(self.size - 1, phase)

    def generalised_qpe(self, amt_estimation_qubits: int, angle: double):
        qc = QuantumCircuit(amt_estimation_qubits+1, amt_estimation_qubits)
        
        for qubit in range(amt_estimation_qubits):
            qc.h(qubit)

        qc.x(amt_estimation_qubits)

        repetitions = 1
        for counting_qubit in range(amt_estimation_qubits):
            for i in range(repetitions):
                qc.cp(angle, counting_qubit, amt_estimation_qubits)
            repetitions *= 2

        self.qft_inverse_swap(qc, amt_estimation_qubits)
        return qc

    @staticmethod
    def qft_inverse_swap(qc: QuantumCircuit, n: int):
        for qubit in range(n//2):
            qc.swap(qubit, n-qubit-1)
        qc.append(QuantumFourierTransform(n).generate_circuit().inverse(), [i for i in range(n)])


if __name__ == "__main__":
    print(QuantumPhaseEstimation().generate_circuit(pi))
