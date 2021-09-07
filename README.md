# metathesis
Application for selling your products <br />
Here you create your account and you can post ads with descriptions and pictures, as well as edit them <br />

After setting env variables <br />
create folder metathesis/application/static/uploads
```
docker-compose build
docker-compose up
```

Seed DB
```
docker exec -it {container} flask seed
```
