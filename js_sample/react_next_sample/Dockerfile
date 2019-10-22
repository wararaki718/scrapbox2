FROM node:12.13.0 as build

WORKDIR /app
COPY app /app
RUN yarn build

CMD ["yarn", "start"]
