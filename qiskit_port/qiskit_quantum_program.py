import sys
from qiskit import QuantumProgram

qp = QuantumProgram()
qp.set_api(
    sys.argv[1],
    'https://quantumexperience.ng.bluemix.net/api')
backend = sys.argv[2]
coupling_map = eval(sys.argv[3])
qp.load_qasm_file(sys.argv[4], 'qiskit')
result = qp.execute(["qiskit"], backend=backend, coupling_map=coupling_map, shots=int(sys.argv[5]), wait=50, timeout=600)
if str(result) == 'COMPLETED':
    print(result.get_counts("qiskit"))
    print(result.get_ran_qasm("qiskit"))
else:
    print(result)
