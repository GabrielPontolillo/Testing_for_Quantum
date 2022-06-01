import shutil
import os
import string
import json


class ProgramGenerator:

    def __init__(self, language: string, min_qubits: int, max_qubits: int, number_of_programs: int) -> None:
        """ Used to specify the qubit size of quantum circuits to be generated"""
        self.language = language
        self.min_qubits = min_qubits
        self.max_qubits = max_qubits
        self.number_of_programs = number_of_programs

    def generate_circuits(self):
        if self.language == "qiskit":
            relative_path = os.path.join(os.path.dirname(__file__), '..', "Algorithm Bases\\Qiskit\\Algorithms.json")
            file = open(relative_path, "r")
            algorithm_data = json.loads(file.read())
            copied_programs = 0
            for algorithm in algorithm_data['Algorithms']:
                if copied_programs < self.number_of_programs:
                    qubit_min = algorithm['qubit-min']
                    qubit_max = algorithm['qubit-max']
                    # I'm pretty sure this logic is slightly off come back later
                    if qubit_min <= self.min_qubits:
                        if qubit_max is None or self.max_qubits is None or qubit_max >= self.max_qubits:
                            path_to_algorithm = os.path.join(relative_path, '..', algorithm['filename'])
                            shutil.copy(path_to_algorithm, "WorkingDirectory")
                            copied_programs += 1
            file.close()
