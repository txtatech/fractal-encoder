#!/bin/bash

directories=(
    "outputs/bintext"
    "outputs/integrity"
    "outputs/binimages"
    "outputs/binimgdecode"
    "outputs/blob"
    "outputs/converted1"
    "outputs/converted2"
    "outputs/crawl"
    "outputs/fractals"
    "outputs/grid1"
    "outputs/grid2"
    "outputs/ledgers"
    "outputs/qrs"
)

for directory in "${directories[@]}"
do
    if [ -d "$directory" ]; then
        find "$directory" -type f -delete
        echo "Contents of $directory removed."
    else
        echo "Directory $directory does not exist."
    fi
done

