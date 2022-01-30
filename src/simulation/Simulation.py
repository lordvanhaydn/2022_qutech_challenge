import logging
import typing

from quantum.EncryptionProtocol import EncryptionProtocol
from simulation.Agent import Agent
from simulation.KeyInterface import KeyInterface


class Simulation:

    def __init__(self):
        self._agents: typing.Dict[str, 'Agent'] = {}

    def add_agent(self, name):
        self._agents[name] = Agent()

    def generate_keys(self, agent_1_name, agent_2_name, protocol_name: str = 'simple', key_length: int = 3):
        agent_1 = self._agents[agent_1_name]
        agent_2 = self._agents[agent_2_name]

        protocol_config = getattr(EncryptionProtocol, protocol_name)
        if callable(protocol_config):
            for _ in range(10):
                agent_1.generate_raw_key(length=key_length)
                agent_1.generate_base(length=key_length)
                agent_2.generate_raw_key(length=key_length)
                agent_2.generate_base(length=key_length)

                interface = KeyInterface(protocol_config)
                interface.simulate_key_exchange(agent_1, agent_2)

                if agent_1.get_private_key_hash() == agent_2.get_private_key_hash():
                    logging.info('Hashes match! Connection established')
                    break
                else:
                    logging.info('Keys do not match! Trying again...')

    def send_message(self, sender, receiver, message):
        sending_agent = self._agents[sender]
        receiving_agent = self._agents[receiver]

        encrypted_message = sending_agent.send_message(receiver, message)
        receiving_agent.receive_message(encrypted_message)
