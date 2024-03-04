# https://zenn.dev/junki555/articles/a19f27d1045805
docker-compose up -d
docker-compose exec app bash
bash-4.4# pwd
/srv
# https://qiita.com/Keichan_15/items/7ec1e8d417e273143c34
bash-4.4# microdnf install findutils
bash-4.4# sh gradlew build
bash-4.4# java -jar build/libs/api-0.0.1-SNAPSHOT.jar

curl http://localhost:8080/test -X GET
curl http://localhost:8080/test/json -X GET
curl http://localhost:8080/test/post -X POST -H 'Content-Type: application/json' -d '{"value1":"hoge","value2":"fuga"}'