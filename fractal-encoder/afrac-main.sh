#!/bin/bash

# Start afrac-main.py
python3 afrac-main.py

# Wait for afrac-main.py to finish
wait

# Start afrac-qr.py
python3 afrac-qr.py

# Wait for afrac-qr.py to finish
wait

# Start afrac-grid.py
python3 afrac-grid.py

# Wait for afrac-grid.py to finish
wait


