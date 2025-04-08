import time
import torch
import pennylane as qml
import numpy as np
from torch.profiler import profile, ProfilerActivity

# ✅ Dummy classical ML loop (simulating GNN or MLP forward pass)
def classical_loop(n_iterations=100):
    x = torch.randn(100, 3)  # Simulated hit data (100 hits, 3 features: x, y, z)
    w = torch.randn(3, 1)    # Simulated weights
    for _ in range(n_iterations):
        y = torch.matmul(x, w)  # Simple linear layer
    return y

# ✅ Dummy QML circuit (same style as in qml_pipeline.py)
dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def qml_loop(params, edges):
    for i in range(4):  # ✅ FIXED: Explicit loop since dev.wires is not an int
        qml.RY(params[i], wires=i)
    for i, j in edges:
        qml.CNOT(wires=[i, j])
    return qml.expval(qml.PauliZ(0))

# ✅ Benchmarking Function
def benchmark(n_iterations=100):
    edges = [(0, 1), (1, 2), (2, 3)]
    params = np.random.random(4)

    print("🔁 Running Classical Benchmark...")
    start_time = time.time()
    with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
        classical_loop(n_iterations)
    classical_time = time.time() - start_time
    classical_energy = prof.key_averages().table(sort_by="cpu_time_total")  # proxy energy

    print("⚛️ Running Quantum Benchmark...")
    start_time = time.time()
    for _ in range(n_iterations):
        qml_loop(params, edges)
    qml_time = time.time() - start_time
    qml_energy = qml_time * 0.1  # proxy energy

    # ✅ Display Results
    print("\n📊 Benchmark Results:")
    print(f"🧠 Classical Time: {classical_time:.4f} seconds")
    print(f"⚛️ QML Time:       {qml_time:.4f} seconds")
    print(f"⚡ Classical Energy (proxy):\n{classical_energy}")
    print(f"⚡ QML Energy (proxy):       {qml_energy:.4f} units")

# ✅ Run the benchmark
if __name__ == "__main__":
    benchmark(n_iterations=100)
