FROM python:3.10-slim as builder

WORKDIR /app

RUN python -m venv .venv

COPY requirements.txt /app/requirements.txt
RUN .venv/bin/pip install -r requirements.txt

FROM python:3.10-slim as runtime

ENV PATH="/app/.venv/bin:$PATH"

COPY --from=builder /app/.venv /app/.venv
COPY bdd /app

WORKDIR /app

CMD ["behave"]
