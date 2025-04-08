import pennylane as qml
import numpy as np

# 4-qubit quantum device
dev = qml.device("default.qubit", wires=4)

def ising_hamiltonian(params, edges):
    cost = 0
    for i, j in edges:
        cost += params[0] * qml.PauliZ(i) @ qml.PauliZ(j)
    return cost

@qml.qnode(dev)
def qml_circuit(params, edges):
    for i in range(4):  # ✅ Hard-coded since we know it's 4 qubits
        qml.RY(params[i], wires=i)
    for i, j in edges:
        qml.CNOT(wires=[i, j])
    return qml.expval(ising_hamiltonian(params, edges))

# Dummy edge list and parameters
edges = [(0, 1), (1, 2), (2, 3)]
params = np.random.random(4)

result = qml_circuit(params, edges)
print(f"✅ QML Circuit Output (Expectation Value): {result}")
