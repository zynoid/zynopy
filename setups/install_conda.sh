#!/bin/bash

DOWNLOAD_ROOT=~/Downloads
PROGRAM_ROOT=~/ProgramFiles

if [ ! -d $DOWNLOAD_ROOT ]; then
  mkdir $DOWNLOAD_ROOT
fi
if [ ! -d $PROGRAM_ROOT ]; then
  mkdir $PROGRAM_ROOT
fi
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -P $DOWNLOAD_ROOT
$DOWNLOAD_ROOT/Miniconda3-py39_4.12.0-Linux-x86_64.sh
echo "# conda" >> ~/.bashrc
echo "export PATH=$PROGRAM_ROOT/miniconda3/bin:$PATH" >> ~/.bashrc
source ~/.bashrc