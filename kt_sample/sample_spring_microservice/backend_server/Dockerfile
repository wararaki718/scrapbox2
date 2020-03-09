## build stage
FROM openjdk:8 as build

ENV BUILD_HOME=/work
WORKDIR ${BUILD_HOME}
COPY build.gradle.kts ${BUILD_HOME}
COPY settings.gradle.kts ${BUILD_HOME}
COPY gradlew ${BUILD_HOME}
COPY gradle.properties ${BUILD_HOME}
COPY gradle ${BUILD_HOME}/gradle

RUN ./gradlew clean build

## application stage
FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=build /work/build/libs/backend_server-1.0-SNAPSHOT.jar .

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "backend_server-1.0-SNAPSHOT.jar" ]
