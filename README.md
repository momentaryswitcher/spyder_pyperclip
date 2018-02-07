# spyder_pyperclip
Using Pyperclip to provide a cross-platform Python module for copying text from the clipboard.

I am using elementary OS Loki 0.4 which is built on the top of Ubuntu 16.04.

I encountered this issue while working in an anaconda environment and using spyder as my IDE (spyder installed through conda).

The exception is raised while using pandas and implementing read_clipboard method on it.

The error: Pyperclip could not find a copy/paste mechanism for your system. For more information, please visit https://pyperclip.readthedocs.org

To resolve this, I installed pyperclip in the conda environment using the command:

>conda install -c conda-forge pyperclip

Also, run the following commands to fix the "Not Implemented Error":

sudo apt-get install xsel to install the xsel utility.
sudo apt-get install xclip to install the xclip utility.

I didn't use the following since I don't use pip:

pip install gtk
pip install PyQt4

You can install the above in conda environment using:

conda install -c ostrokach gtk
and
conda install -c anaconda pyqt

It is important to restart the entire system after installation. Becuase the install might work in the Jupyter Notebook but can't work in Spyder.

Copy something (the copied text will be in the clipboard) and run the code provided in the sample.py file.
