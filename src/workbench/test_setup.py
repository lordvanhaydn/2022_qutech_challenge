import logging

from simulation.Simulation import Simulation

logging.basicConfig(level=logging.INFO)

sim = Simulation()

sim.add_agent('Alice')
sim.add_agent('Bob')

sim.generate_keys('Alice', 'Bob', protocol_name='final_simulator', key_length=6)

sim.send_message('Alice', 'Bob', 'Hello World!')
