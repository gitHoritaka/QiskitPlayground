#problem https://www.qcoder.jp/ja/contests/QPC005/problems/A2
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import HGate

def solve(n: int) -> QuantumCircuit:
    m, k = QuantumRegister(1), QuantumRegister(n)
    qc = QuantumCircuit(m, k)
    # Write your code here:
    qc.x(k)
    h_gate = HGate()
    ch_gate = h_gate.control(n)
    qc.append(ch_gate,k[:] + m[:]) 
    qc.x(k)
    return qc

if __name__ == "__main__":
    import os
    qc = solve(2)
    save_dir = "/Users/horiguchitakahiro/hobby/Quantom/QiskitEnv/Qcoder/005/output"
    save_path = os.path.join(save_dir,"A2.png")
    qc.draw('mpl', filename=save_path)
