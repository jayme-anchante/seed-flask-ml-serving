# seed-flask-ml-serving

Dependencies: [docker](https://www.docker.com/)

Building the image: `docker build --file Dockerfile --tag seed-flask-ml-serving .`

Running the image: `docker run --rm -it -v $PWD:/home/ -p 9000:9000 seed-flask-ml-serving`


API routes:

- **/fit**: fit a model and save it to disk, returns a simple "Sucess" message.

Using curl:

```
curl -X POST -H "Content-type: application/json; charset=utf-8" -d@"data.json" "http://0.0.0.0:9000/fit"
```

Using Python:

```
import requests
data = open("data.json", "rb")
endpoint = "fit"
url = f"http://0.0.0.0:9000/{endpoint}"
resp = requests.request(method="POST", url=url, data=data)
resp.json()
>>> "Success"
```

- **/predict**: load a pre-trained model from disk and predicts using the payload.

Using curl:

```
curl -X POST -H "Content-type: application/json; charset=utf-8" -d@"data.json" "http://0.0.0.0:9000/predict"
```

Using Python:

```
import requests
data = open("data.json", "rb")
endpoint = "predict"
url = f"http://0.0.0.0:9000/{endpoint}"
resp = requests.request(method="POST", url=url, data=data)
resp.json()
>>> [{"id": "1", "prediction": 101}, {"id": "2", "prediction": 13}]
```

- **delete**: delete all pre-trained models except the most recent one.

Using curl:

```
curl -X DELETE "http://0.0.0.0:9000/delete"
```

Using Python:

```
import requests
endpoint = "delete"
url = f"http://0.0.0.0:9000/{endpoint}"
resp = requests.request(method="DELETE", url=url)
resp.json()
``` 

Development commands (can be ignored if running):
Comment the `ENTRYPOINT` from the Dockerfile
Running the image: `docker run --rm -it -v $PWD:/home/ -p 8888:8888 -p 9000:9000 seed-flask-ml-serving`
Launch jupyter-lab: `jupyter-lab --allow-root --no-browser --ip 0.0.0.0 --port 8888`
