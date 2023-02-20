# chatgpt-flask-server

This is a simple Flask server that uses the [ChatGPT](https://github.com/acheong08/ChatGPT)(Reverse engineered ChatGPT API)

## Configuration

Edit `env/config.yaml` and `docker-compose.yml`

## Usage

Build docker image
```bash
docker build -t chatgpt-flask-server .
```
Run it
```bash
docker-compose up
```

## API

### POST /chat
Request
```json
{
    "message": "Hello"
}
```
Response
* success
```json
{
    "code": 0,
    "data": "Hello! How can I assist you today?"
}
```
* error
```json
{
    "code": 1,
    "message": "empty request body!"
}
```