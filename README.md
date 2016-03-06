
# Internsheep Project

<img src="media/project_picture.jpg" alt="Sheep your internsheep" width="200">


Ce projet requiert d'avoir déjà installé PostgreSQL.

Pour rentrer dans l'env virtuel :
```bash
$ source internsheep_env/bin/activate
```

Pour initialiser la bdd, les tables et les données initiales :
```bash
$ ./manage.py initdb
```

Pour lancer le serveur :
```bash
$ ./manage.py runserver
```

The server is now live at `http://localhost:5000/`



Pour réinitialiser l'env virtuel :
```bash
$ ./deploy.sh
```
