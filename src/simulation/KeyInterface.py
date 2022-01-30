from quantum.CircuitExecutor import CircuitExecutor
from quantum.ExecutionPipeline import ExecutionPipeline
from simulation.Agent import Agent
from utils.Utils import Utils


class KeyInterface:

    def __init__(self, protocol_config):
        self._protocol_config = protocol_config

    def simulate_key_exchange(self, agent_1: 'Agent', agent_2: 'Agent'):
        protocol = self._protocol_config()

        circuit_parameters = [agent_1.__getattribute__(attr) for attr in protocol['circuit_parameters']['agent_1']] \
                             + [agent_2.__getattribute__(attr) for attr in protocol['circuit_parameters']['agent_2']]

        executor = CircuitExecutor(backend=protocol['backend'])
        pipeline = ExecutionPipeline(executor, protocol['circuit'])
        result = pipeline.apply_on(*circuit_parameters)
        measurement_2 = [x[0] for x in result]
        measurement_1 = [0 if len(x) <= 1 else x[1] for x in result]
        if not protocol['swap']:
            agent_1_private_key = Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                   agent_2.__getattribute__('_sender_base'),
                                                   agent_1.__getattribute__('_raw_key'))
            agent_2_private_key = Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                   agent_2.__getattribute__('_sender_base'),
                                                   measurement_2)
        else:
            agent_1_private_key = Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                   agent_2.__getattribute__('_sender_base'),
                                                   agent_1.__getattribute__('_raw_key')) \
                                  + Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                     agent_2.__getattribute__('_sender_base'),
                                                     measurement_1)
            agent_2_private_key = Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                   agent_2.__getattribute__('_sender_base'),
                                                   measurement_2) \
                                  + Utils.merge_keys(agent_1.__getattribute__('_sender_base'),
                                                     agent_2.__getattribute__('_sender_base'),
                                                     agent_2.__getattribute__('_raw_key'))
        agent_1.__setattr__('_private_key', agent_1_private_key)
        agent_2.__setattr__('_private_key', agent_2_private_key)
