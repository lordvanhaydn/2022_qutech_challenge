import typing

from quantuminspire.api import QuantumInspireAPI
from quantuminspire.credentials import save_account


class CircuitExecutor:

    def __init__(self, backend: str = 'Spin-2'):
        save_account('c1fa8cbfd9b0f60668392b5fbf57d26ba4a59d95')
        self._qi = QuantumInspireAPI()
        self._backend = backend

    def execute_qasm(self, qasm: str) -> typing.List[int]:
        backend_type = self._qi.get_backend_type_by_name(self._backend)
        result = self._qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1)

        if result.get('histogram', {}):
            binary_string = [format(int(x), 'b') for x in result['histogram'].keys()]
            return [[int(character) for character in x] for x in binary_string][0]

        else:
            reason = result.get('raw_text', 'No reason in result structure.')
            print(f'Result structure does not contain proper histogram data. {reason}')
            return []
