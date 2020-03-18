FROM node:12.13.0

ARG BUILD_ENV=production

WORKDIR /frontend
COPY . /frontend
RUN yarn build:${BUILD_ENV}

EXPOSE 3000

CMD ["yarn", "start"]
