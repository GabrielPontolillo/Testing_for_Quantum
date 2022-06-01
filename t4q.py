import argparse
import os
import sys
import shutil
from ProgramGeneration.ProgramGenerator import ProgramGenerator


def empty_working_dir():
    relative_path = os.path.join(os.path.dirname(__file__), "WorkingDirectory")
    if not os.path.isdir(relative_path):
        os.makedirs(relative_path)
    paths = os.listdir(relative_path)
    for path in paths:
        if os.path.isdir(path):
            shutil.rmtree(os.path.join(relative_path, path))
        else:
            os.remove(os.path.join(relative_path, path))


parser = argparse.ArgumentParser(description='Generate scripts for quantum programs')

parser.add_argument('--language', '-l', metavar='language', type=str, default='qiskit',
                    help='Specify what language to create examples in')

parser.add_argument('--generate', '-g', action='store_true',
                    help='Generates quantum programs within specification')

parser.add_argument('--number-of-programs', '-p', metavar='programNumber', type=int, default=10,
                    help='Specify the number of programs to generate')

parser.add_argument('--min-qubits', '--', metavar='min qubits', type=int, default=2,
                    help='Specify the minimum number of qubits')

parser.add_argument('--max-qubits', '-+', metavar='max qubits', type=int, default=None,
                    help='Specify the maximum number of qubits')

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
    empty_working_dir()
    ProgramGenerator(args.language, args.min_qubits, args.max_qubits, args.number_of_programs).generate_circuits()

if args.delete:
    empty_working_dir()


