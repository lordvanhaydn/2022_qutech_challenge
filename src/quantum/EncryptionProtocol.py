class EncryptionProtocol:

    @staticmethod
    def simple():
        return {
            'backend': 'Spin-2',
            'circuit': 'simple_2q',
            'circuit_parameters': {
                'agent_1': ['_raw_key', '_sender_base'],
                'agent_2': ['_sender_base']
            },
            'swap': False
        }

    @staticmethod
    def simple_simulator():
        return {
            'backend': 'QX single-node simulator',
            'circuit': 'simple_2q',
            'circuit_parameters': {
                'agent_1': ['_raw_key', '_sender_base'],
                'agent_2': ['_sender_base']
            },
            'swap': False
        }

    @staticmethod
    def final():
        return {
            'backend': 'Spin-2',
            'circuit': 'final_2q',
            'circuit_parameters': {
                'agent_1': ['_raw_key', '_sender_base'],
                'agent_2': ['_raw_key', '_sender_base']
            },
            'swap': True
        }

    @staticmethod
    def final_simulator():
        return {
            'backend': 'QX single-node simulator',
            'circuit': 'final_2q',
            'circuit_parameters': {
                'agent_1': ['_raw_key', '_sender_base'],
                'agent_2': ['_raw_key', '_sender_base']
            },
            'swap': True
        }
