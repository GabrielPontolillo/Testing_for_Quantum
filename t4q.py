import argparse

import os
import sys
from ProgramGeneration.ProgramGenerator import ProgramGenerator

parser = argparse.ArgumentParser(description='Generate scripts for quantum programs')

parser.add_argument('--language', '-l', metavar='language', type=str, default='qiskit',
                    help='Specify what language to create examples in')

parser.add_argument('--generate', '-g', action='store_true',
                    help='Generates quantum programs within specification')

parser.add_argument('--number-of-programs', '-p', metavar='programNumber', type=int, default=2,
                    help='Specify the number of programs to generate')

parser.add_argument('--number-of-input-qubits', '-q', metavar='inputQubits', type=int, default=4,
                    help='Specify the number of input qubits')

parser.add_argument('--test', '-t', action='store_true',
                    help='Executes test')

parser.add_argument('--delete', '-d', action='store_true',
                    help='Deletes everything from working directory')

args = parser.parse_args()

if args.language:
    if args.language.lower() == 'qiskit':
        pass
    if args.language.lower() == 'cirq':
        pass
    if args.language.lower() == 'q#':
        pass    
else: 
    raise(RuntimeError("Please specify a programming language to generate tests with"))

if args.generate:
    print(args.number_of_input_qubits)
    print(args.number_of_programs)
    ProgramGenerator(args.number_of_input_qubits, args.number_of_programs).generate_circuits()

