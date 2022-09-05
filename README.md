# Description

Behavior-driven development example using Python and BDD framework
[behave](https://behave.readthedocs.io/en/stable/index.html).

# Requirements

Since the entire app is dockerized, you only need to have:

- Docker
- bash
- GNU make

If you are a Linux user, you probably have all of that. If you don't, please install and set up the environment before
reading the rest of this README.

# Running test suite

To build the container and run it, you can use Makefile targets `build` and `run`. For convenience though, there is a
target named `all`, which will build and run the container in one go. To get a list of all available targets and their
descriptions, just run `make` or `make help`:

```console
all                            Build and run the container in one go
prepare-env-file               Prepare local .env file with secrets based on the template
build                          Build the container
run                            Run the container, providing new OTP beforehand
enter                          Enter the container, directly into /app directory
status                         Show status of running containers
clean-docker                   Clean all Docker resources, cached images, etc.
help                           See this help
```

### Secrets

Before building the container for the first time, you will be asked to fill in secret values in `bdd/.env` file (based
on [this template file](bdd/.env.example)).

On the other hand, each time you run the container, you will be asked for a one-time password (OTP) required for 2FA.

Unfortunately using 2FA makes it impossible to run the suite without manual human intervention, because OTP must be
supplied from time to time. From my experiments a once generated OTP can be reused for a couple of minutes, but I don't
know the exact details, so to make testing reliable, you must supply it during each run.
