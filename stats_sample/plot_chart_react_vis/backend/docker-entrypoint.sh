#!/bin/bash

uvicorn backend.app:api --host 0.0.0.0 --port 8000
