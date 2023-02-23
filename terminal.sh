python -m pip list                      # List packages
python -m pip install --upgrade pip     # Update pip in virtual environment
python -m pip check                     # Check requirements
/usr/bin/python3.7 -m pip               # Using pip with other Python interpreters

# DO NOT install into your global Python interpreter! 
# ALWAYS try to use an environment when developing locally!
# Unless you are developing in a container.

apt-get install python3-pip             # Download and install pip
pip3 install <package name>             # Download modules from PyPI
pip3 show <package name>                # Detailed info about the package
python setup.py install                 # Install package directly

# Generate required libraries list

pip freeze > requirements.txt           # Generate required packages file

# Formatter - use black instead of autopep8 that does minimal work