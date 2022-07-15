# Provision new VM with below Gateway OVA link

https://opsramp-gateway.s3.us-east-2.amazonaws.com/Gateway+Cluster/Nextgen-gw-202207140245.ova

# Copy all the necessary certificates to Node

File location: /usr/local/share/ca-certificates/

    dell-101.crt 
    dell.crt 
    emc.crt 
    emcd.crt


# Nextgen Gateway DOC

https://confluence.opsramp.net/display/PA/Next-gen+gateway

# Install K3S and required binaries
opsramp-collector-start setup init

# Adding mirrors to fetch the images and charts

sudo vi /etc/rancher/k3s/registries.yaml

mirrors:
  artifact.registry:
    endpoint:
      - "https://us-docker.pkg.dev"

# Restart K3S after adding mirrors

sudo service k3s restart

# Registering Gateway with thirdparty enabled

opsramp-collector-start install -e k8s -u dell-sdk-lab.api.opsramp.net -k 5560c768-e390-41ef-9f3d-dbccdb3a02f1 --thirdPartyApp enable 
--imageChannel pre-release

# Registering Gateway with thirdparty app and proxy enabled

opsramp-collector-start install -e k8s -u dell-sdk-lab.api.opsramp.net -k 5560c768-e390-41ef-9f3d-dbccdb3a02f1 --thirdPartyApp enable 
--imageChannel pre-release --proxy-protocol http --proxy-ip 172.22.11.33 --proxy-port 1234 --proxy-username test --proxy-password test@123

# Add certificates to vProbe to pull third party charts and images

## Add all the certificates to single file  ca-certificates-custom.crt
cat dell*.crt > ca-certificates-custom.crt

## Create Configmap
kubectl create configmap root-certs-cm --from-file=ca-certificates-custom.crt

## Update vprobe stateful set
kubectl edit statefulset nextgen-gw

### Append the following under volumeMount section in vprobe container
- mountPath: /etc/ssl/certs/ca-certificates-custom.crt
  name: root-certs-volume  
  subPath: ca-certificates-custom.crt

### Append the following under volumes section
- configMap:      
    name: root-certs-cm  
  name: root-certs-volume

# Add proxy to vProbe to pull third party charts and images

## Create configmap 
kubectl create configmap proxy-env-cm --from-file=/etc/environment

## Update vprobe stateful set
kubectl edit statefulset nextgen-gw

### Append the following under volumeMount section in vprobe container
- mountPath: /etc/environment
  name: proxy-env-volume  
  subPath: environment

### Append the following under volumes section
- configMap:      
    name: proxy-env-cm  
  name: proxy-env-volume
  
 
