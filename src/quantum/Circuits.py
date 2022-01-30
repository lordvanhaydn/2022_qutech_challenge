class Circuits:

    @staticmethod
    def simple_2q(key_a: int,
                  base_a: int,
                  base_b: int) -> str:
        qasm_string = '''version 1.0\nqubits 2'''
        if key_a == 1: qasm_string += "\nX q[0]"
        if base_a == 1: qasm_string += "\nH q[0]"
        qasm_string += "\nswap q[0],q[1]"
        if base_b == 1: qasm_string += "\nH q[1]"
        qasm_string += "\nmeasure_all"
        return qasm_string

    @staticmethod
    def fancy_2q(key_a: int,
                 sender_base_a: int,
                 receiver_base_a: int,
                 key_b: int,
                 sender_base_b: int,
                 receiver_base_b: int) -> str:
        qasm_string = '''version 1.0\nqubits 2'''
        if key_a == 1: qasm_string += "\nX q[0]"
        if key_b == 1: qasm_string += "\nX q[1]"
        if sender_base_a == 1: qasm_string += "\nH q[0]"
        if sender_base_b == 1: qasm_string += "\nH q[1]"
        qasm_string += "\nswap q[0],q[1]"
        if receiver_base_a == 1: qasm_string += "\nH q[0]"
        if receiver_base_b == 1: qasm_string += "\nH q[1]"
        qasm_string += "\nmeasure_all"
        return qasm_string

    @staticmethod
    def final_2q(key_a: int,
                 base_a: int,
                 key_b: int,
                 base_b: int) -> str:
        qasm_string = '''version 1.0\nqubits 2'''
        if key_a == 1: qasm_string += "\nX q[0]"
        if key_b == 1: qasm_string += "\nX q[1]"
        if base_a == 1: qasm_string += "\nH q[0]"
        if base_b == 1: qasm_string += "\nH q[1]"
        if base_a == 1: qasm_string += "\nH q[1]"
        if base_b == 1: qasm_string += "\nH q[0]"
        qasm_string += "\nmeasure_all"
        return qasm_string
