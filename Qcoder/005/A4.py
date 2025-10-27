#https://www.qcoder.jp/ja/contests/QPC005/problems/A4
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import XGate

def solve(n: int) -> QuantumCircuit:
    m, k = QuantumRegister(1,"m"), QuantumRegister(n,"k")
    qc = QuantumCircuit(k, m)
    # Write your code here:
    for i in range(4):
        indexes = []
        for l in range(0,n+1,1 << i):
            indexes.append(l)
        for p in range(len(indexes)):
            if p % 2 == 0 and p + 1 < len(indexes):
                left = indexes[p]
                right = indexes[p + 1]
                qc.swap(left,right) 


    return qc

def true_solve(n: int) -> QuantumCircuit:
    L = n + 1
    qc = QuantumCircuit(L)
 
    for i in range(L.bit_length()):
        for j in range(0, L - (2 ** i), 2 ** (i + 1)):
            qc.swap(j, j + (2 ** i))
 
    return qc

if __name__ == "__main__":
    import os
    qc = solve(10)
    save_dir = "/Users/horiguchitakahiro/hobby/Quantom/QiskitEnv/Qcoder/005/output"
    save_path = os.path.join(save_dir,"A4.png")
    qc.draw('mpl', filename=save_path)
