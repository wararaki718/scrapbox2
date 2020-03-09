FROM node:12.13.0

WORKDIR /app
COPY . /app
RUN yarn build

EXPOSE 3000
CMD ["yarn", "start"]