# Simple HTTPD Echo Server for Openshift Router
## About
- Runs a simple Python app deployment containing a trivial webserver
- tested with Openshift 4.16
- Note: HTTP/2 is disabled on Openshift router (by default)

## Build
Build the dockerfile and push to some registry. I used:
```
docker buildx build server -t quay.io/thikade/echo-server:latest --push
```

## Deploy
```
oc apply -k k8s/
```

