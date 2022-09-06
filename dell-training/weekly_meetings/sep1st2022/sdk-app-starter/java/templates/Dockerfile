FROM adoptopenjdk/openjdk11:alpine-jre

RUN apk update ;\
apk upgrade ;\
apk add --upgrade musl-utils;\
mkdir -p /opt/app && mkdir -p /opt/app/config && mkdir -p /opt/app/lib /opt/opsramp/bin

WORKDIR /opt/app

COPY ./cluster-adapter/info.json .
COPY ./cluster-adapter/config.json ./config
COPY ./cluster-adapter/target/{{appName}}.jar ./lib
COPY ./cluster-adapter/dependencies.json ./config/dependencies.json
RUN cp /bin/* /opt/opsramp/bin
RUN rm -rf /bin/

ENTRYPOINT ["java","-XX:VMOptionsFile=/opt/app/config/jvm.properties","-jar","./lib/{{appName}}.jar"]



