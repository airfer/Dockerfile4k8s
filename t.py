#!/bin/python
#encoding=utf-8
import os
images_list=[
"gcr.io/google_containers/kube-apiserver-amd64:v1.6.7",
"gcr.io/google_containers/kube-controller-manager-amd64:v1.6.7",
"gcr.io/google_containers/kube-proxy-amd64:v1.6.7",
"gcr.io/google_containers/kube-scheduler-amd64:v1.6.7",
"gcr.io/google_containers/kubernetes-dashboard-amd64:v1.6.1",
"gcr.io/google_containers/k8s-dns-sidecar-amd64:1.14.4",
"gcr.io/google_containers/k8s-dns-kube-dns-amd64:1.14.4",
"gcr.io/google_containers/k8s-dns-dnsmasq-nanny-amd64:1.14.4",
"gcr.io/google_containers/etcd-amd64:3.0.17",
"gcr.io/google_containers/heapster-grafana-amd64:v4.0.2",
"gcr.io/google_containers/heapster-influxdb-amd64:v1.1.1",
"gcr.io/google_containers/heapster-amd64:v1.3.0",
"gcr.io/google_containers/pause-amd64:3.0"]

for images in images_list:
	directory_name=images.split(':')[0].split('/')[2]
	print directory_name
	cmd_make_directory='mkdir ./'+ directory_name
	os.system(cmd_make_directory)
	file_name=directory_name + "/Dockerfile"
	with open(file_name,'w+') as fr:
		str="FROM " + images
		fr.write(str)
