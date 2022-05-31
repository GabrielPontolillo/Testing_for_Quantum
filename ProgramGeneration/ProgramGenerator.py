import shutil
import os


class ProgramGenerator:
    def __init__(self, size: int, number_of_programs: int) -> None:
        """ Used to specify the qubit size of quantum circuits to be generated"""
        self.size = size
        self.number_of_programs = number_of_programs

    def generate_circuits(self):
        relative_path = os.path.join(os.path.dirname(__file__), '..', "Algorithm Bases\\Qiskit")
        print(relative_path)
        print(os.listdir(relative_path))
        shutil.copy("Algorithm Bases/Qiskit/QuantumFourierTransform.py", "WorkingDirectory")
