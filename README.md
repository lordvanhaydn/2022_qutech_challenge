# iQuHack 2022: Quantum Key Distribution Library

## Presentation

Our presentation can be found {here}(https://1drv.ms/p/s!AhmabPzKf3o1hbgXwCDZUexX_k4nCg?e=cwiiCY)

## Team: Qurnalism

Nils, Stefan, Paul, Tobias

## Abstract

Secure messaging is important in multiple sectors. With the rise of quantum computers, the only way to ensure fully
encrypted messaging is to use Quantum Key Distribution. Our library implements a modified version of the BB84 protocol
on a Quantum Inspire system. It also offers the framework for two parties to connect to our interface and exchange
messages. We also included a quantum-based random number generator for truly random numbers and a quantum-secure error
check by comparison of two hash-functions.

## Structure of the repository

- src.quantum
  - CircuitExecutor: Helper class to execute a cirquit on real hardware or emulator
  - Circuits: Circuits are encoded as static methods here
  - EncryptionProtocol: Protocol definition by config
  - ExecutionPipeline: Executes a circuit multiple times from a buffer
- src.simulation
  - Agent: Basic object of an agent (e.g. Alice, Bob)
  - KeyInterface: Interface which simulates the exchange in a quantum internet
  - Simulation: Simulation environment to test agents
- src.utils
  - RandomGenerator: Generates random number, can also use the quantum computer
  - Utils: Utilities to merge keys e.g.
- src.workbench
  - Scripts to test the framework. Have a look into test_setup for the basic usage of the simulation environment

## Details About the Implementation

The classical communication was implemented in python while the quantum information channels were implemented with cQASM
and run on the Quantum inspire platform.

First of all, both Alice and Bob use the Quantum Inspire system to generate random numbers. This can be done by applying
a Hadamard Gate on a qubit in 0 state and measuring the qubit in the z basis, which will give us a completely random
result of either 0 or 1. Alternatively, A classical random number generator can be used. We offer both options that can
be chosen depending on preferences of the user/availability of the quantum hardware. This random number generation is
repeated several times to generate different bitstrings for the key and basis for each Alice and Bob. In our modified
version of the BB84 protocol, both participants of the conversation encode a key which is sent to the other. This
doubles the length of the output key, with only generating 4/3 as many random numbers. Since in a practical application
photons would be exchanged, our
"mirrored" version of BB84 does not increase the runtime significantly. With the algorithm, two private keys are
generated and merged.

The resulting keys can be compared publicly using a quantum-safe hash function such as sha3-512. If they match, the key
exchange was successful, if they do not match, an error occurred (most likely) in the quantum algorithm, so a re-run is
necessary, which our code handles automatically, up to 10 tries.

Once the key hash functions match, a secure connection can be established. We used a symmetric XOR encryption of the
message with an elongated key. The receiving party can then decrypt the message using the same XOR function.

This procedure can be used in any data transfer application, from email to messenger app, as long as a series of qubits
can be exchanged between the communicating parties. Our journalist can now transmit the critical insider information
safely.

## Our personal experience

We all really enjoyed the event and had a lot of fun coding together and discussing concepts of quantum technology.
Besides learning hard skills like Quantum Key Distribution, we also learned how to properly set up and manage a
collaborative project. It was an enrichment to work in a team with members in multiple countries, so that iQuHack 2022
let us grow not only as researchers but also as a team.

## Date

January 30, 2022
