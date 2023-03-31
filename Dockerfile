ARG VARIANT="3.11-alpine3.17"
FROM python:${VARIANT}

RUN apk add --no-cache bash
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD src /src

ENTRYPOINT ["./entrypoint.sh"]
