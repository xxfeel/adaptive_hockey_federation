FROM python:3.11-slim-bullseye AS builder

RUN mkdir /app
WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev --with test

FROM python:3.11-slim-bullseye

COPY --from=builder /app /app
COPY adaptive_hockey_federation/ ./
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/app/.venv/bin/gunicorn", "adaptive_hockey_federation.wsgi:application", "--bind", "0:8000" ]