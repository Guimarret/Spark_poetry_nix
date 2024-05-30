# Spark Environment with Nix and Poetry

Welcome to my personal project repository where I have set up a Spark environment using Nix for general package management and Poetry for Python package management. This setup helps me ensure reproducibility and ease of use across different development environments.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Overview

In this project, I've configured a Spark environment to streamline data processing tasks. Leveraging Nix and Poetry ensures that dependencies are managed efficiently and consistently.

## Prerequisites

Before you start, make sure you have the following installed:

- [Nix](https://nixos.org/download.html): for managing system-wide dependencies.

## Usage

1. **Set up the Nix environment:**

   This repository includes a `default.nix` file for the environment setup.

   ```sh
   nix develop
   ```
    This command initializes a shell with all the dependencies specified in flake.nix.

    Install Python dependencies:

    - While inside the Nix shell, run:

    ```sh
    poetry install
    ```

    This command installs all the Python dependencies listed in pyproject.toml.
2. **Run your Spark application**

    Execute your Spark application using Poetry. For example:
    
    ```sh
    spark-submit src/your_spark_script.py
    ```
    In my repo it would be:
    ```sh
    spark-submit data_extraction/main.py
    ```
    To run in Jupyter notebook files, you can just run the cells normally after initiate the environment and select the correct kernel.

## Project Structure
Here's an overview of the project structure:

```
your-repo-name/
├── pyproject.toml     # Poetry configuration file
├── poetry.lock        # Poetry lock file
├── flake.nix          # Nix environment configuration
├── flake.lock         # Flake lock file
├── src/               # Source code for your Spark application
│   └── your_spark_script.py
└── README.md          # This README file
```

- pyproject.toml: Contains the list of Python dependencies and project metadata.
- poetry.lock: Locked versions of dependencies for reproducibility.
- flake.nix: Describes the Nix environment.
- src/: Directory containing the source code for your Spark application.
- README.md: This file.