#!/bin/bash

uvicorn poet_docker.app:app --host 0.0.0.0 --port 8000
