#!/bin/bash
project=power-flex-dell
version=1.0.0

echo "Building ${project} docker image...!!"
docker build -t us-docker.pkg.dev/gateway-images/gateway-cluster-images/${project}:${version} .
echo "---------------------------------------------"

echo "Pushing ${project} docker image to repo!!"
docker push us-docker.pkg.dev/gateway-images/gateway-cluster-images/${project}:${version}
echo "---------------------------------------------"

export HELM_EXPERIMENTAL_OCI=1

echo "Saving ${project} helm chart"
#helm chart save assets/charts/${project}/ us-docker.pkg.dev/gateway-images/gateway-cluster-charts/${project}:${version}
helm package assets/charts/${project}
echo "---------------------------------------------"

echo "Pushing ${project} helm chart to repo"
#helm chart push us-docker.pkg.dev/gateway-images/gateway-cluster-charts/${project}:${version}
helm push ${project}-${version}.tgz oci://us-docker.pkg.dev/gateway-images/gateway-cluster-charts/
echo "---------------------------------------------"
