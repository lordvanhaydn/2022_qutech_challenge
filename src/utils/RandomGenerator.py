import random

from quantum.CircuitExecutor import CircuitExecutor


class RandomGenerator:

    @staticmethod
    def bit_value_quantum() -> int:
        qasm = f'''version 1.0

            qubits 2

            H q[0]

            Measure_z q[0]
            '''
        return CircuitExecutor().execute_qasm(qasm)[0]

    @staticmethod
    def bit_value() -> int:
        return random.choice([0, 1])
