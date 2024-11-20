# test_task


Update files by .proto:
```
protoc --python_out=./ --twirpy_out=./ ./haberdasher.proto
```

Run server (without docker):
```
uvicorn twirp_server:app --port=3000
```

Run client:
```
python twirp_client.py
```

Run docker:
```
docker image build -t test_task -f Dockerfile . 
docker run --name test_task_con --restart unless-stopped -p 3000:3000 test_task
```
