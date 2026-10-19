# Google ADK Learning

A hands-on learning repository documenting my journey into **Generative AI and Agentic AI** using Google's Agent Development Kit (ADK).

This repository contains small agents and experiments built while learning ADK concepts through the Google Skills learning path.

## Learning Path

**Current learning path:** Develop Agents with Agent Development Kit (ADK)

The goal is to understand how AI agents are created, configured, tested, and extended through practical implementation.

## Projects

| Project | Description | Implementation |
|---|---|---|
| `my_first_agent` | Initial experiments with building an AI agent | Python |
| `my_config_agent` | Exploring configuration-based agent creation | YAML |
| `customer_support_agent` | Customer support agent experiment | Update as implemented |
| `model_comparison` | Experiments involving model comparison | Update as implemented |
| `name_extractor` | Name extraction agent experiment | Update as implemented |
| `personalized_greeter` | Agent for personalized greetings and templating | Python |
| `problem_solver` | Problem-solving agent experiment | Python |
| `product_extractor` | Product extraction agent experiment | Python |

*This project list will evolve as I progress through the learning path. Descriptions will be refined as each agent's implementation develops.*

## Tech Stack

- Python
- Google Agent Development Kit (ADK)
- YAML for configuration-based agents
- Large Language Models (LLMs)

## Repository Structure

```text
google-adk-learning/
├── my_first_agent/
├── my_config_agent/
├── customer_support_agent/
├── model_comparison/
├── name_extractor/
├── personalized_greeter/
├── problem_solver/
├── product_extractor/
├── .gitignore
└── README.md
```

Each project folder contains the code and supporting files relevant to that agent.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/a-dinesh-kumar/google-adk-learning.git
cd google-adk-learning
```

### 2. Create and activate a virtual environment

**Windows — Command Prompt**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Google ADK

```bash
python -m pip install google-adk
```

### 4. Configure environment variables

Create a `.env` file in the relevant agent folder and add the environment variables required by that project.

For example, if the agent uses the Gemini API, configure the appropriate API key variable according to the project's setup.

**Important:** Never commit API keys, passwords, or other secrets to GitHub.

### 5. Run an agent

Navigate to the relevant project folder and use the ADK command appropriate to that project's structure.

For example, for a Python agent named `my_first_agent`, if its `agent.py` defines the required ADK `root_agent`:

```bash
adk run my_first_agent
```

The exact command and configuration may differ depending on the agent's implementation. Refer to the individual project files and the official ADK documentation.

## Key Learning Areas

As this repository grows, it may cover:

- Creating agents using Python
- Defining agents using YAML configuration
- Working with LLM-powered agents
- Prompt design and response generation
- Tools and agent capabilities
- Testing and evaluating agents
- Multi-agent workflows
- Deployment and production concepts

These are learning goals, not a claim that every topic has already been implemented.

## Notes and References

This repository may also contain personal notes, command references, and implementation patterns collected during the learning process.

## Learning in Progress

This is an evolving learning repository. The projects represent practical exercises, experimentation, and incremental progress toward building more capable AI agents.

