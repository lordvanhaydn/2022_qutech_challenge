import coreapi
from quantuminspire.api import QuantumInspireAPI

qi = QuantumInspireAPI(
    authentication=coreapi.auth.TokenAuthentication("c39a14a77f691765d2eed16742afe945ccaf572f", scheme="token"))


def gen_qasm_circuits_1q(m, b1, b2):
    for i in range(len(m)):
        string = '''version 1.0
qubits 1'''
        if m[i] == 1: string += "\nX q[0]"
        if b1[i] == 1: string += "\nH q[0]"
        if b2[i] == 1: string += "\nH q[0]"
        string += '''
measure_all'''

        yield string


# for s in gen_qasm_circuits_1q([0, 1], [1, 0], [1, 1]):
#     print(s)
#     print('----')


backend_type = qi.get_backend_type_by_name('Spin-2')  # backend_type = qi.get_backend_type_by_name('Spin-2')

results = []
data = []
for cirquit in gen_qasm_circuits_1q([0, 1], [1, 0], [1, 1]):
    results.append(qi.execute_qasm(qasm_basis, backend_type=backend_type, number_of_shots=1))

    if results[-1].get('histogram', {}):
        data.append(results[-1]['histogram'])
    #         print(results[-1]['histogram'])
    else:
        reason = results[-1].get('raw_text', 'No reason in result structure.')
        print(f'Result structure does not contain proper histogram data. {reason}')

r1 = []  # 01
r2 = []  # 10
for d in data:
    keys = list(d.keys())
    maxkey = keys[0]
    for k in keys:
        if d[k] > d[maxkey]: maxkey = k
    r1.append(int(maxkey) & 1)
    r2.append((int(maxkey) & 2) / 2)

print(r1)
print(r2)
