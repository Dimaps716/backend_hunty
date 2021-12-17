# Api

this project is a small tech shop 🚀

_This is an API. The cell will allow you to view information on vacancies and companies. It receives requests and returns information about them._

_These will allow you to get a copy of the working project on your local machine for development and testing ._

See Implementation to learn how to implement the project.


### Prerequisites  📋


```
docker-compose
ubuntu o wsl

```

### Instalación 🔧

In the terminal located in the folder where you want to save this project, execute the following.
```
git clone https://github.com/Dimaps716/
```
move to developer branch.
```
git checkout developer
```
run project dependencies
```
docker-compose build
```
run project
```
docker-compose up -d
```
run migrations

```
docker-compose run --rm web python manage.py makemigrations

docker-compose run --rm web python manage.py migrate

```
for now the database is empty
```
docker-compose ps
```
add information to the database
```
docker-compose run --rm web python manage.py loaddata fixtures/company.json
```
```
docker-compose run --rm web python manage.py loaddata fixtures/vacancy.json
```
here you can see the images and their status
```
docker-compose up
```
this will activate the servers

```
http://localhost:8000/
```
check the documentation
```
http://localhost:8000/docs
```
enter a couple of categories and a couple of products and you're done
## Built with 🛠️


* [Docker] (https://docs.docker.com/compose/reference/run/)
* [Django] (https://www.djangoproject.com/)
* [python] (https://www.python.org/)


## Authors ✒️


* ** Dimanso perez ** - * Initial Work * - [Dimaps716] (https://github.com/Dimaps716)


## License 📄

This project is under the License (Your License) - see the  (LICENSE.md) file for details

## Expressions of Gratitude 🎁

* Tell others about this project 📢
* Invite a beer 🍺 or a coffee ☕ to someone on the team.
* Give thanks publicly 🤓.




---
⌨️ with ❤️ by [Dimaps716] (https://github.com/Dimaps716) 😊