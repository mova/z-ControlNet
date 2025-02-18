#!/bin/bash
# turn on bash's job control
set -x
# Start the fastapi server and put it in the background
uvicorn server_fastapi:app --host 0.0.0.0 --port 8000 &
# Start the gradio UI server 
python3 server_ui_demo.py &
wait %1 %2
