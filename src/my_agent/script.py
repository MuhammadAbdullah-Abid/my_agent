import os
import sys

from streamlit.web import cli

def app():
    sys.argv = ["streamlit", "run", "src/my_agent/global_config.py"]
    cli.main()
