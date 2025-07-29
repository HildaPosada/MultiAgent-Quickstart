# How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol

This guide provides a step-by-step guide to build and run a complete **multi-agent system** using [Coral Protocol](https://github.com/Coral-Protocol), open-source agents, and Coral Studio so you can view all the interactions visually.

## Introduction

### What is Coral?

Coral Protocol provides a collaboration infrastructure for AI agents. It allows agent developers to publish agent advertisements that any other agent or any multi-agent application can immediately use on demand.

Agent developers earn incentives when their agents are used.
Application developers can mix and match from Coral’s growing library of agents to assemble advanced systems faster and without vendor lock-in.

In this scenario, you would be an application developer, using Coral Protocol's local mode to build a multi-agent system by bringing together existing open source agents.


---

## Prerequisites

Before you set up and run Coral, make sure your local environment has the following tools installed.

These are required to run agents, Coral Server, Coral Studio, and external LLMs like OpenAI.

### Required Tools & Versions

| Tool | Version | Why You Need It                                             |
|------|---------|-------------------------------------------------------------|
| **Python** | 3.10+ | Needed for the agents in this guide         |
| **uv** | latest | Python environment & dependency manager ([install guide](https://docs.astral.sh/uv/getting-started/installation/)) |
| **Node.js** | 18+ | Required to run Coral Studio (the UI)                       |
| **npm** | Comes with Node | Used to install and run Studio dependencies                 |
| **Git** | latest | To clone agent and Coral repos                              |
| **OpenAI API Key** | Any | Needed for agents using OpenAI models (GPT)                 |

### Recommended Tools

| Tool | Reason |
|------|--------|
| **Visual Studio Code** | IDE for editing agent code and config |

---

## Note on Docker
All of these components are possible to run in Docker containers, but for this guide we will be running them locally.

See our Docker guide for more details on how to run Coral in Docker: [Coral Docker Guide](./docker-guide.md)

## Note on Windows
If you're on Windows, you may need to use Git Bash or WSL (Windows Subsystem for Linux) to run the commands in this guide. PowerShell may not work correctly with some of the commands.

WSL 2 works, but WSL1 performs better.

Alternatively, you may use Docker, but Windows users may suffer from performance issues with Docker Desktop since windows forces all containers to run in WSL2.

# Getting Started
First clone this repository:
```bash
git clone https://github.com/Coral-Protocol/MultiAgent-Quickstart.git
```

## Run Coral Server

**Coral Server** is the engine that runs your multi-agent sessions, executes agent logic, and facilitates communication between agents.

In this step, you'll set up and start Coral Server locally, with the config path pointed at the repository root, so it uses our provided `application.yaml` config.

### 1. Run the Coral Server from source

```bash
cd coral-server
CONFIG_PATH=.. ./gradlew run
```

> **NOTE**: this will appear to get stuck at 86% - this is a gradle quirk, if the logs say the server has started then it has started.

This will launch the server,
which acts as a control plane that manages networks of agents, and facilitates their communication and collaboration.

The application.yaml file is at coral-server/src/main/resources/application.yaml. This is where the agents are defined, think of it like a docker image registry, but for agents that might be running outside docker or in docker, or via another runtime.

---

## Start Coral Studio (UI)

**Coral Studio** is a web-based UI for managing sessions, agents, and threads visually.

This step walks you through installing and running Coral Studio locally on your machine.

### 1. Run coral studio

Open your terminal (Git Bash or PowerShell) and run:

```bash
npx @coral-protocol/coral-studio
```

This will start the Studio UI at [`http://127.0.0.1:3000`](http://127.0.0.1:3000)

Open this URL in your web browser to access the Coral Studio interface.

### 2. Confirm It's Working
You should see:
- A dashboard for Coral Studio
- An option to create a session or connect to Coral Server
- A visual interface to observe and interact with threads and agents

[//]: # (Coral-UI should look like this)

[//]: # (<img width="957" alt="Image" src="https://github.com/user-attachments/assets/819ce48e-b740-459f-a0aa-9eb23ec66c1f" />)

---

## Creating a Session
After editing your `application.yaml` file, the server will have hot-reloaded the changes, and you can now create a session to connect your agents.

> You can check the coral server logs in the terminal where you started it. You should see messages indicating that the agents have been loaded successfully.

![Creating Session in UI](./assets/gifs/creating_session.gif)

### Creating a session via Coral Studio
In production, you would typically just make a POST request using your preferred HTTP client library from your application code.

For development purposes it makes sense to use Curl, Postman, or the Coral Studio UI to create sessions.

Let's use the Coral Studio UI to create a session.

First, we need to connect to our Coral Server:

- Click on the server selector, and press 'Add a server'
[TODO: add screenshot of 'Add a server' option]
- For the host, enter `localhost:5555`, and press 'Add'.

Now we can create the session:

- Click on 'Select session', and then 'New session'
- Make sure 'Application ID' and 'Privacy Key' match what you have in your `application.yaml`
    - If you're using our provided config, `app` and `priv` work.

Now we pick our agents:

- Click the 'New agent' under, and select 'interface'
- Fill in the needed API keys
    - For OpenAI, see [this page](https://platform.openai.com/api-keys)
    - For Firecrawl, see [their website](https://www.firecrawl.dev/)
    - For GitHub, see [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) (make sure to only allow read-only permissions!)
- For the 'interface' agent specifically, we need to add the user input custom tools:
    - Go to the 'Custom Tools' section, and in the dropdown, select both 'request-question' and 'answer-question'
- Feel free to add some extra prompts to finetune agent behaviour

With all our agents ready, we need to make a group - to indicate that all of these agents can interact:

- Go to the 'Groups' section, and click 'New group'
- Click on 'Empty group', and select all of our agents

> You can also copy the resulting JSON from the 'Export' section - to easily import all of these settings again in future.


Click on 'Create', and your session should spin up!

When the interface agent is ready, it'll call our custom 'request-question' tool, and a notification will appear in the 'Tools > User Input' tab in your sidebar.
