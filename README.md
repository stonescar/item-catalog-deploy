# Item catalog app (deploy)

Deployment version of the [Item Catalog App](https://github.com/stonescar/item-catalog). Project 5 for my Full Stack Nanodegree at [udacity.com](http://udacity.com). The project is hosted on a Lightsail Ubuntu server from [Amazon Web Services](https://lightsail.aws.amazon.com/)

**The project is live at [http://35.158.71.73/](http://35.158.71.73/)**

## Installed software
- [Apache2](https://httpd.apache.org/) w/ mod_wsgi
- [postgreSQL](https://www.postgresql.org/)
- [python2.7](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [SQLalchemy](https://www.sqlalchemy.org/)

## Configurations
- Set up custom sudo user
- Enable key-based SSH authentication
- Use non-standard port for SSH
- Configure firewall to only allow SSH, HTTP and NTP
- Customize the [Item Catalog App](https://github.com/stonescar/item-catalog) to be hosted using Apache2 and mod_wsgi
- Configure a custom user in postgreSQL to limited read/write privileges

For more information about the Item Catalog App, visit the [project repository](https://github.com/stonescar/item-catalog)

## Licencing
This project is licensed under the [MIT License](LICENSE)
