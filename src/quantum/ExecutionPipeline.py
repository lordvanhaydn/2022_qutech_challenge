import typing

from quantum.CircuitExecutor import CircuitExecutor
from quantum.Circuits import Circuits


class ExecutionPipeline:

    def __init__(self, circuit_executor: 'CircuitExecutor', circuit: str):
        self._circuit_executor = circuit_executor
        self._circuit = circuit

    def apply_on(self, *circuit_params: typing.List[int]):
        results = []
        for circuit_param in list(zip(*circuit_params)):
            circuit = getattr(Circuits, self._circuit)
            if callable(circuit):
                results.append(self._circuit_executor.execute_qasm(circuit(*circuit_param)))
        return results
