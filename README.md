# Create simulation configs for your project

When running multiple simulations at the same time its important to do the following:

- **Isolation of runs**: This can be done by saving info about a run to a separate directory. These items can be
  - Data output
  - Run configuration (for documentation and reproducibility)
  - Run logs
- **Error handling**: If a run fails, it should exit gracefully saving error messages and logs. It should not affect the other runs.
