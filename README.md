# test_task


Update files by .proto:
```
protoc --python_out=./ --twirpy_out=./ ./haberdasher.proto
```

Run server:
```
uvicorn twirp_server:app --port=3000
```