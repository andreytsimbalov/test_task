# test_task

Запуск сервера: через `Run server` либо через `Run docker`. Для проверки работоспособности - запуск `Run client`.

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

___

Update files by .proto:
```
protoc --python_out=./ --twirpy_out=./ ./haberdasher.proto
```