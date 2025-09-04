
from qiskit import QuantumCircuit

def create_bell_pair():
    # Create a circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)

    # Apply Hadamard to qubit 0
    qc.h(0)

    # Apply CNOT with control=0, target=1
    qc.cx(0, 1)

    # Measure both qubits
    qc.measure([0, 1], [0, 1])

    return qc
