# metathesis
####After setting env variables <br />
create folder metathesis/application/static/uploads
```
docker-compose build
docker-compose up
```

####Seed DB
```
docker exec -it {container} flask seed
```
