init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/project_name/$(name)/g' *.* {} \;
	mv ./project_name ./$(name)

superuser:
	docker exec -it project_name ./manage.py createsuperuser

shell:
	docker exec -it project_name ./manage.py shell

enter:
	docker exec -it project_name bash

makemigrations:
	docker exec -it project_name ./manage.py makemigrations

migrate:
	docker exec -it project_name ./manage.py migrate

initialfixture:
	docker exec -it project_name ./manage.py loaddata initial

testfixture:
	docker exec -it project_name ./manage.py loaddata test

test:
	docker exec -it project_name ./manage.py test

collectstatic:
	docker exec -it project_name ./manage.py collectstatic --noinput

makemessages:
	docker exec -it project_name django-admin makemessages

compilemessages:
	docker exec -it project_name django-admin compilemessages
