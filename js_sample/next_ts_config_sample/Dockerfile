FROM node:12.13.0

ARG BUILDENV

WORKDIR /app
COPY app /app
RUN yarn build:${BUILDENV}

EXPOSE 3000

CMD ["yarn", "start"]
