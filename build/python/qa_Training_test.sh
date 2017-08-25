#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/abhishek/GNURadio/python_test/gr-SVM/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/abhishek/GNURadio/python_test/gr-SVM/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/abhishek/GNURadio/python_test/gr-SVM/build/swig:$PYTHONPATH
/usr/bin/python2 /home/abhishek/GNURadio/python_test/gr-SVM/python/qa_Training.py 
