FROM node:12.13.0 as build

WORKDIR /app
COPY app /app
RUN yarn build


FROM nginx:latest

COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
