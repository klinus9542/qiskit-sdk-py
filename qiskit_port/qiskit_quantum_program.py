import sys
from qiskit import QuantumProgram

qp = QuantumParogram()
qp.set_api(
    sys.argv[1],
    'https://quantumexperience.ng.bluemix.net/api')
backend = sys.argv[2]
coupling_map = eval(sys.argv[3])
qp.load_qasm_file(sys.argv[4], 'qiskit')
result = qp.execute(["qiskit"], backend=backend, coupling_map=coupling_map, shots=int(sys.argv[5]))
if result.get_status() == 'COMPLETED':
     print(result.get_counts("qiskit"))