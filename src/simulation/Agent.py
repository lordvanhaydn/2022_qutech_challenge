import abc
import logging
import typing
from hashlib import sha3_512

from utils.RandomGenerator import RandomGenerator


class Agent(abc.ABC):

    def __init__(self):
        self._private_key = None
        self._public_key = None

        self._sender_base: typing.List[int] = []
        self._raw_key: typing.List[int] = []

    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value

    def get_private_key_hash(self) -> str:
        return sha3_512(repr(self._private_key).encode('utf-8')).hexdigest()

    def generate_raw_key(self, length: int = 3):
        self._raw_key = [RandomGenerator.bit_value() for _ in range(length)]

    def generate_base(self, length: int = 3):
        self._sender_base = [RandomGenerator.bit_value() for _ in range(length)]

    def encrypt(self, message) -> str:
        elongated_private_key = []
        message_out = ""
        # char wise encrypt or decrypt
        for i in message:
            while len(elongated_private_key) < 8:
                for j in self._private_key:
                    elongated_private_key.append(j)
            scramble = 0
            for j in range(8):
                scramble += elongated_private_key.pop() * 2 ** j
            message_out += chr(ord(i) ^ scramble)
        return message_out

    def send_message(self, receiver, message):
        logging.info(f'Send to {receiver}: {message}')
        encrypted_message = self.encrypt(message)
        logging.info(f'Encrypted message {encrypted_message} sent.')
        return encrypted_message

    def receive_message(self, encrypted_message):
        logging.info(f'Received encrypted message {encrypted_message}')
        message = self.encrypt(encrypted_message)
        logging.info(f'Read message: {message}')
