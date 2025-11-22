# bw-to-datasphere-converter

## project structure
```
├── api
│   ├── http_api
│   │   ├── __init__.py
│   │   ├── app_details_route.py
│   │   ├── app_fetch_route.py
│   │   ├── app_list_route.py
│   │   ├── app_migration_route.py
│   │   ├── app_push_route.py
│   │   ├── app_qa_route.py
│   │   └── app_stats_route.py
│   ├── websocket_api
│   │   ├── __init__.py
│   │   └── app_run_status_route.py
│   └── __init__.py
├── clients
│   ├── Postman
│   │   └── neo-to-cf-migrator-BAS.postman_collection.json
│   └── REST Client
│       └── neo-to-cf-migrator-BAS.postman_collection.http
├── db_architecture
│   ├── db_architecture.drawio.png
│   └── db_architecture.png
├── migrator
│   ├── nodes
│   │   ├── __init__.py
│   │   ├── planner.py
│   │   ├── transformer.py
│   │   └── writer.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── file_ops.py
│   └── graph.py
├── models
│   ├── __init__.py
│   ├── clone_request.py
│   └── push_request.py
├── services
│   ├── __init__.py
│   ├── git_service.py
│   ├── hana_service.py
│   └── ws_service.py
├── .cfignore
├── .gitignore
├── Procfile
├── README.md
├── main.py
├── manifest.yml
├── requirements.txt
└── runtime.txt
```