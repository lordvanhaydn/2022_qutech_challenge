#!/usr/bin/env python
# coding: utf-8

# # Which key exchange method yields the smaller error
# 
# In this note book, the error for exchanging keys using three different methods is discussed. All of them realize the BB84 protocol, but the exact implementation on the quantum inspire network is varied in the spirit of this hackathon.

# In[1]:


import coreapi

# In[19]:


from quantuminspire.api import QuantumInspireAPI

auth = coreapi.auth.TokenAuthentication("c39a14a77f691765d2eed16742afe945ccaf572f", scheme="token")
qi = QuantumInspireAPI(authentication=auth)

# In[3]:


qasm_basis = '''version 1.0

qubits 2

X q[0]
H q[0]

swap q[0],q[1]

measure_all

'''


# In[58]:


def gen_qasm_circuits_2qsimple(m, b1, b2):
    for a, b, c in zip(m, b1, b2):
        string = '''version 1.0\nqubits 2'''
        if a == 1: string += "\nX q[0]"
        if b == 1: string += "\nH q[0]"
        string += "\nswap q[0],q[1]"
        if c == 1: string += "\nH q[1]"
        string += "\nmeasure_all"
        yield string


# In[5]:


def gen_qasm_circuits_2qfancy(mA, bA1, bA2, mB, bB1, bB2):
    for i in range(len(mA)):
        string = '''version 1.0\nqubits 2'''
        if mA[i] == 1: string += "\nX q[0]"
        if mB[i] == 1: string += "\nX q[1]"
        if bA1[i] == 1: string += "\nH q[0]"
        if bB1[i] == 1: string += "\nH q[1]"
        string += "\nswap q[0],q[1]"
        if bA2[i] == 1: string += "\nH q[0]"
        if bB2[i] == 1: string += "\nH q[1]"
        string += "\nmeasure_all"
        yield string


# In[73]:


def gen_qasm_circuits_nqsimple(n, m, b1, b2):
    for i in range(len(m)):
        string = [f'version 1.0', f'qubits {n}']

        if m[i] == 1: [string.append(f"X q[{j}]") for j in range(n)]
        if b1[i] == 1: [string.append(f"H q[{j}]") for j in range(n)]

        if b2[i] == 1: [string.append(f"H q[{j}]") for j in range(n)]
        string.append("measure_all")
        yield "\n".join(string)


def gen_qasm_circuits_2nqfancy(n, mA, bA1, bA2, mB, bB1, bB2):
    for i in range(len(mA)):
        string = [f'version 1.0', f'qubits {n}']
        if mA[i] == 1: [string.append(f"X q[{j}]") for j in range(n)]
        if mB[i] == 1: [string.append(f"X q[{j + n}]") for j in range(n)]
        if bA1[i] == 1: [string.append(f"H q[{j}]") for j in range(n)]
        if bB1[i] == 1: [string.append(f"H q[{j + n}]") for j in range(n)]

        [string.append(f"swap q[{j}],q[{j + n}]") for j in range(n)]

        if bA2[i] == 1: [string.append(f"H q[{j}]") for j in range(n)]
        if bB2[i] == 1: [string.append(f"H q[{j + n}]") for j in range(n)]
        string.append("measure_all")
        yield "\n".join(string)


def gen_qasm_circuits_nqentagnled(n, m, b1, b2):
    assert n > 1, "n needs to be bigger than 1"
    for i in range(len(m)):
        string = [f'version 1.0', f'qubits {n}']
        if m[i] == 1: string.append(f"X q[0]")
        if b1[i] == 1: string.append(f"H q[0]")
        [string.append(f"cnot q[0],q[{j}]") for j in range(1, n)]

        if b2[i] == 1: [string.append(f"H q[{j}]") for j in range(n)]
        string.append("measure_all")
        yield "\n".join(string)


# In[6]:


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


# In[88]:


for s in gen_qasm_circuits_2nqfancy(5, [0, 1], [1, 0], [1, 1], [0, 1], [1, 0], [1, 1]):
    print(s)
    print('----')

# In[77]:


backend_type = qi.get_backend_type_by_name('Spin-2')

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

# In[78]:


r1 = []  # 01
r2 = []  # 10
for d in data:
    keys = list(d.keys())
    maxkey = keys[0]
    for k in keys:
        if d[k] > d[maxkey]: maxkey = k
    #     v = d[maxkey]
    r1.append(int(maxkey) & 1)
    r2.append((int(maxkey) & 2) / 2)

# In[79]:


r1

# In[80]:


r2

# In[86]:


results

# In[81]:


results[0]

# In[48]:


client = coreapi.Client(auth=auth)

# In[85]:


client.get(
    f'https://api.quantum-inspire.com/results/7111615/histogram/4f0c4eee218d4487c8f1ee5f52d4adba147bf6999935f8963c92100ff1bfedf6/')

# In[50]:


client.get(f'{results[0]["calibration"]}')

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[36]:


client.get(
    f'https://api.quantum-inspire.com/results/7107766/quantum-states/54d8d2b26681e09cc12b355b4964b4dd8ece2a0fee26a113ce0591715feecacb')

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
