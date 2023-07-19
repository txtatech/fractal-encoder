#!/bin/bash

# Start
python3 afrac-main-mode-8.py

# Wait
wait

# Start
cd outputs

# Wait
wait

# Start
bash afrac-export-meta-hash.sh

# Wait
wait

# Start
cd ..

# Wait
wait

# Start
echo Generating QR Codes and Grid!

# Wait
wait

# Start
python3 afrac-qr.py

# Wait
wait

# Start
python3 afrac-grid.py

# Wait
wait

# Start
echo Done!

# Wait
wait


