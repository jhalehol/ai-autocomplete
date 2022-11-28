FROM python:3.9

EXPOSE 9000

WORKDIR /app

COPY ./requirements/requirements.txt /app/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY autocomplete_api/ /app/
COPY bin/entrypoint /app/entrypoint

CMD ["/app/entrypoint"]
