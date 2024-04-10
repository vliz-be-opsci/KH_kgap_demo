# K-GAP DEMO for FRDN KnowledgHub community day 

### Running this project - steps:

Steps:  
1. Clone github repository
```
git clone git@github.com:vliz-be-opsci/KH_kgap_demo.git
```
2. Build services 

```
.$ cp dotenv-example .env             # make sure you have an .env file
.$ docker-compose build  # use docker to build the services 
```
3. Start up services
```
.$ docker compose up
```

Open the Jupyter notebook and/or GraphDB environments:
```
.$ xdg-open $(docker/jupyter_url.sh)  # this gets the url for the service and opens a browser to it
.$ xdg-open http://localhost:7200     # opens the web ui in a browser
```