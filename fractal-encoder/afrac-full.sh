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
python3 afrac-qr.py

# Wait
wait

# Start
python3 afrac-grid.py

# Wait
wait

# Start
bash lazycopy.sh

#Wait
wait

echo QR code ASCII art text generating...

# Wait
wait

# Start
python3 afrac-frac-grid.py

# Wait
wait

# Start
cd outputs

# Wait
wait

# Start
bash qr-png-ascii-convert.sh

# Wait
wait

# Start
bash qr-png-text-embed-qr.sh

# Wait
wait

# Start
bash ablob-no-pad.sh

# Wait
wait

# Start
bash ablob-padding.sh

# Wait
wait

echo Fractal encoding has finished and all files have been generated!

# Wait
wait
