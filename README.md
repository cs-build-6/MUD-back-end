# MUD-back-end

back-end now fully live on heroku at this link

https://danadventure.herokuapp.com/

if you want to explore the database via graphql please go to this link

https://danadventure.herokuapp.com/graphql

for a collection of all tested postman requests see:

https://www.getpostman.com/collections/bdfde8bb9a52ec32007d

# individual curls

## registration

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser555", "password1":"testpassword", "password2":"testpassword"}' https://dashboard.heroku.com/registration/

## login 

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser555", "password":"testpassword"}' https://dashboard.heroku.com/login/

## init (note you need to be a super user)

curl -X GET -H 'Authorization: Token 3d4ca0a2209642365a7b5ad55d9ecff2b4dd73ac' https://dashboard.heroku.com/init/

## move (note only works if direction available)

curl -X POST -H 'Authorization: Token 3d4ca0a2209642365a7b5ad55d9ecff2b4dd73ac' -H "Content-Type: application/json" -d '{"direction":"n"}' https://dashboard.heroku.com/move/
