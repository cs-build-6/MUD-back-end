# MUD-back-end

back-end now fully live on heroku at this link   (see example queries at bottom of ReadMe)

https://danpatadv.herokuapp.com/

if you want to explore the database via graphql please go to this link

https://danpatadv.herokuapp.com/graphql

# individual curls

## registration

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser555", "password1":"testpassword", "password2":"testpassword"}' https://danpatadv.herokuapp.com/registration/

## login 

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser555", "password":"testpassword"}' https://danpatadv.herokuapp.com/login/

## init (note you need to be a super user)

curl -X GET -H 'Authorization: Token 3d4ca0a2209642365a7b5ad55d9ecff2b4dd73ac' https://danpatadv.herokuapp.com/init/

## move (note only works if direction available)

curl -X POST -H 'Authorization: Token 3d4ca0a2209642365a7b5ad55d9ecff2b4dd73ac' -H "Content-Type: application/json" -d '{"direction":"n"}' https://danpatadv.herokuapp.com/move/

## for a collection of all tested postman requests iin json see:

https://www.getpostman.com/collections/bdfde8bb9a52ec32007d

## example graphql queries

query allrooms {
  rooms {
    x
    y
    floor
    description
    nTo
    eTo
    wTo
    uTo
    dTo
    region
    itemdesc
  }
}

query allitems {
  items {
    noun
    skill
    id
    itemRoom
    itemOwner
  }
}
