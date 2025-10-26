#https://www.qcoder.jp/ja/contests/QPC005/problems/A4
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import XGate

def solve(n: int) -> QuantumCircuit:
    m, k = QuantumRegister(1), QuantumRegister(n)
    qc = QuantumCircuit(m, k)
    # Write your code here:
    for i in range(n):
        qc.swap(m[0],k[i])

    return qc

if __name__ == "__main__":
    import os
    qc = solve(2)
    save_dir = "/Users/horiguchitakahiro/hobby/Quantom/QiskitEnv/Qcoder/005/output"
    save_path = os.path.join(save_dir,"A4.png")
    qc.draw('mpl', filename=save_path)
