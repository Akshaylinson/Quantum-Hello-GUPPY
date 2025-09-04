
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile
from circuits.bell_pair import create_bell_pair
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

def run():
    qc = create_bell_pair()

    # Draw the circuit
    print("Quantum Circuit:")
    print(qc.draw())

    simulator = AerSimulator()
    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=100)
    result = job.result()
    counts = result.get_counts()

    print("Quantum Bell State Results:", counts)

    os.makedirs("results", exist_ok=True)
    with open("results/output.txt", "w") as f:
        f.write(str(counts))

    # Plot histogram of results
    plot_histogram(counts)
    plt.show()

if __name__ == "__main__":
    run()
