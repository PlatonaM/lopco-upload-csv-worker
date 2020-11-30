#### Description

    {
        "name": "Upload CSV to platform",
        "image": "platonam/lopco-upload-csv-worker:latest",
        "data_cache_path": "/data_cache",
        "description": "MQTT upload worker.",
        "configs": {
            "usr": null,
            "pw": null,
            "mqtt_server": null,
            "mqtt_port": "18883",
            "mqtt_keepalive": "15",
            "delimiter": null
        },
        "input": {
            "type": "multiple",
            "fields": [
                {
                    "name": "service_id",
                    "media_type": "text/plain",
                    "is_file": false
                },
                {
                    "name": "source_file",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": null
    }
