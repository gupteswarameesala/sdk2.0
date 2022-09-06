#!/bin/bash
project={{appName}}
version={{appVersion}}

echo "Building maven project"
mvn clean install -Dmaven.test.skip=true

echo "Building ${project} docker image...!!"
sudo docker build -t us-docker.pkg.dev/gateway-images/gateway-cluster-images/${project}:${version} .
echo "---------------------------------------------"

echo "Pushing ${project} docker image to repo!!"
sudo docker push us-docker.pkg.dev/gateway-images/gateway-cluster-images/${project}:${version}
echo "---------------------------------------------"

export HELM_EXPERIMENTAL_OCI=1

echo "Saving ${project} helm chart"
helm chart save cluster-adapter/app-helm/${project} us-docker.pkg.dev/gateway-images/gateway-cluster-charts/${project}:${version}
#helm package helm_cshart/helloworld-app-python/ -d assets/
echo "---------------------------------------------"

echo "Pushing ${project} helm chart to repo"
helm chart push us-docker.pkg.dev/gateway-images/gateway-cluster-charts/${project}:${version}
#helm package helm_chart/helloworld-app-python/ -d assets/
echo "---------------------------------------------"

echo "pushing jar to maven repo"
curl -v -u admin:revocafo81 --upload-file classic-adapter/target/${project}-classic-adapter-${version}-bin.tar.gz https://mvn01-dev.opsramp.net/repository/opsramp-content/content/${project}/${version}/${project}-${version}.gz
echo "---------------------------------------------"
