#### Description

    {
        "name": "Upload to platform",
        "description": null,
        "image": "platform-upload-worker",
        "data_cache_path": "/data_cache",
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "service_id",
                    "media_type": "text/plain",
                    "is_file": false
                },
                {
                    "name": "source_table",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": null,
        "configs": {
            "user": null,
            "password": null,
            "machine_id": null
        }
    }
