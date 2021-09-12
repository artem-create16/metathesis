# Metathesis
## Description
Here you can show everyone your ad for the sale of something
## Installation
```
git clone https://github.com/artem-create16/metathesis.git
cd metathesis
```
Rename .env.example file to .env and fill all rows

create folder metathesis/application/static/uploads
```
docker-compose build
docker-compose up
```

(Optional. To populate the database with random values)

```
docker ps
docker exec -it {container id "metathesis_db_1"} flask seed 
```
## Usage
Open http://localhost/ in your browser <br />
Click "Sign up" if you want to register or "Sign in" if you already have account <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/reg.png?raw=true) <br />
After registration you will be taken to the main page, where you can create your ad <br />
Just click "Create ad" <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/create.png?raw=true) <br />
Fill all rows, add images and click "Create" <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/create_post.png?raw=true) <br />
You should see your ad <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/nice_cat.png?raw=true) <br />
Click "Delete" and your ad will be deleted or "Edit", here you can edit your post. Rename rows or delete and add new photos <br />
On main page you can see all ads that has anyone ever created or by clicking on your nickname you can see only your ads<br />
Apply filters to show categories and ad names that interest you <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/filters.png?raw=true) <br />
Open the ad you like by clicking on the ad name <br />
![alt text](https://github.com/artem-create16/metathesis/blob/master/asserts/images/open.png?raw=true) <br />

Click "Sign Out" if you want to sign out from your account

# Api
If you want to get a certain ad make get request
````
curl http://localhost/api/ad/number_ad
````
For example 
````
curl http://localhost/api/ad/1
````

If you want to create new ad make post request
````
curl http://localhost/api/ad/create-ad -d "title=new&description=d_new&category=animals&connection=c_new&user_id=your_id" -X POST -v

````

If you want to delete a certain ad do
````
curl http://localhost/api/ad/number_ads -X DELETE -v
````
If you want to update a certain ad do
````
curl --request PATCH http://localhost/api/ad/54 -d "title=new&description=d_new&user_id=1" -v
````