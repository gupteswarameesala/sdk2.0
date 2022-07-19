FROM adoptopenjdk/openjdk11:alpine-jre

RUN apk update ;\
apk upgrade ;\
apk add --upgrade musl-utils;\
mkdir -p /opt/app && mkdir -p /opt/app/config && mkdir -p /opt/app/lib /opt/opsramp/bin

WORKDIR /opt/app

COPY ./info.json .
COPY ./config.json ./config
COPY target/{{appName}}.jar ./lib
COPY ./dependencies.json ./config/dependencies.json
RUN cp /bin/* /opt/opsramp/bin
RUN rm -rf /bin/

ENTRYPOINT ["java","-XX:VMOptionsFile=/opt/app/config/jvm.properties","-jar","./lib/{{appName}}.jar"]



