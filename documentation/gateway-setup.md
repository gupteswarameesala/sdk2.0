# Gateway setup


## Provision new VM with below Gateway OVA link

https://opsramp-gateway.s3.us-east-2.amazonaws.com/Gateway+Cluster/Nextgen-gw-202207140245.ova


## Copy all the necessary certificates to the provisioned Gateway VM

**Folder path**: /usr/local/share/ca-certificates/

    dell-101.crt 
    dell.crt 
    emc.crt 
    emcd.crt
  
## Run the below command to update CA certificates after adding

**update-ca-certificates**

## If proxy is required, add proxy setting 

**File path**: /etc/environment

**export HTTP_PROXY=http://ipAddress:port**


## Install K3S and required binaries
Run the opsramp collector tool to setup gateway

**opsramp-collector-start** setup init

## Add repo details to fetch the thirdparty images

Edit the below file add the following configuration

sudo vi /etc/rancher/k3s/registries.yaml

```yaml
mirrors:
  artifact.registry:
    endpoint:
      - "https://us-docker.pkg.dev"
```

## Restart K3S after adding repo details

**sudo service k3s restart**

## Register Gateway to cloud with thirdPartyApp flag enabled to run python Apps

**opsramp-collector-start** install -e k8s -u dell-sdk-lab.api.opsramp.net -k 5560c768-e390-41ef-9f3d-XXXXXXXXX --thirdPartyApp enable 
--imageChannel pre-release

## Register Gateway to cloud with thirdPartyApp flag enabled through proxy

**opsramp-collector-start** install -e k8s -u dell-sdk-lab.api.opsramp.net -k 5560c768-e390-41ef-9f3d-XXXXXXX --thirdPartyApp enable 
--imageChannel pre-release --proxy-protocol http --proxy-ip 172.22.11.33 --proxy-port 1234 --proxy-username test --proxy-password test@123

## Add certificates to vProbe to pull third party charts and images

### Add all the certificates to single file  ca-certificates-custom.crt
cat dell*.crt > ca-certificates-custom.crt

### Create Configmap
kubectl create configmap root-certs-cm --from-file=ca-certificates-custom.crt

### Update vprobe stateful set
kubectl edit statefulset nextgen-gw

#### Append the following under volumeMount section in vprobe container
```yaml
- mountPath: /etc/ssl/certs/ca-certificates-custom.crt
  name: root-certs-volume  
  subPath: ca-certificates-custom.crt
```

#### Append the following under volumes section
```yaml
- configMap:      
    name: root-certs-cm  
  name: root-certs-volume
```

## Add proxy info to vProbe to pull third party charts

### Create configmap 
kubectl create configmap proxy-env-cm --from-file=/etc/environment

### Update vprobe stateful set
kubectl edit statefulset nextgen-gw

#### Append the following under volumeMount section in vprobe container
```yaml
- mountPath: /etc/environment
  name: proxy-env-volume  
  subPath: environment
```

#### Append the following under volumes section
```yaml
- configMap:      
    name: proxy-env-cm  
  name: proxy-env-volume
```
  
 
