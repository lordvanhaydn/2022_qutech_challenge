from src.simulation.Agent import Agent

agent = Agent()

agent.__setattr__('_private_key', [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0])

message = agent.encrypt('Hello World!')
print(message)
print(agent.encrypt(message))
