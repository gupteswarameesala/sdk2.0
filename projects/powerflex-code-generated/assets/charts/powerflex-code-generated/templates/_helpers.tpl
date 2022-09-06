{{/*
Expand the name of the chart.
*/}}
{{- define "sdkApp.name" -}}
{{- default .Release.Name .Values.nameOverride | trunc 63 | trimSuffix "-" | kebabcase -}}
{{- end -}}
{{- define "image.channel" -}}
{{- if eq $.Values.imageChannel "latest" -}}
gateway-images/gateway-cluster-images
{{- else if eq $.Values.imageChannel "pre-release" -}}
gateway-images/gateway-cluster-images
{{- else if eq $.Values.imageChannel "stable" -}}
opsramp-registry/gateway-cluster-images
{{- end -}}
{{- end -}}
