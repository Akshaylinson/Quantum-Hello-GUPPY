Quantum Hello (Qiskit Project)

This project demonstrates a simple **quantum program** using [Qiskit](https://qiskit.org/) and the **Aer Simulator**.  
It creates a **Bell State** — one of the most famous examples of **quantum entanglement**.  

---

## 📂 Project Structure

quantum-hello-qiskit/
│── main.py # Entry point to run the simulation
│── circuits/
│ └── bell_pair.py # Defines the Bell State circuit
│── results/
│ └── output.txt # Stores simulation results
│── README.md # Project documentation
│── .venv/ # Python virtual environment (not included in repo)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Install Python
Make sure you have **Python 3.10+** installed.  
[Download Python here](https://www.python.org/downloads/release/python-3100/).

### 2. Create a Virtual Environment
```bash
python -m venv .venv
Activate it:

Windows (PowerShell):

powershell
Copy code
.venv\Scripts\activate
Linux/Mac:

bash
Copy code
source .venv/bin/activate
3. Install Dependencies
Inside the activated venv:

bash
Copy code
pip install qiskit qiskit-aer matplotlib
▶️ Running the Project
bash
Copy code
python main.py
Expected Output (Terminal)
yaml
Copy code
Quantum Circuit:
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘   
q_1: ─────┤ X ├─╫────
          └───┘ ║    
c: 2/═══════════╩════
                00    

Quantum Bell State Results: {'00': 52, '11': 48}
Output Files
results/output.txt → Contains the measured results (counts of 00 and 11).

Visualization
A histogram will pop up showing the distribution of measurement results.
Example:


📖 Concepts Covered
Quantum Circuits → Building circuits with Qiskit.

Superposition → Created using the Hadamard gate (H).

Entanglement → Created using the CNOT gate (cx).

Measurement → Collapsing qubits into classical bits.

Simulation → Running on AerSimulator (no real quantum hardware needed).

🔮 Next Steps
You can extend this project to include:

Grover’s Algorithm → Quantum search.

Quantum Teleportation → Transferring qubit states.

Shor’s Algorithm → Quantum factorization.

📝 Requirements
Python 3.10+

Qiskit 1.x

Qiskit Aer

Matplotlib

