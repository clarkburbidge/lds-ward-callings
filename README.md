# LDS Ward Callings

If you are an LDS Ward Clerk or Bishopric member you may have the need to view all the members of the ward and their callings.
This Python 3 code pulls the data that you are authorized to view from lds.org via the official API, formats it, builds some html pages, and writes a PDF document for printing.

![Demo Web Page](https://github.com/clarkburbidge/lds-ward-callings/blob/master/demo.png?raw=true "Demo Web Page")

## Getting Started

For now you will need to run the Python code and install the needed libraries.

If it is not clear to you how to do this, my code may not be of help to you. I am interested in making this more accessible, so add an issue and if I have the time I'll try and explain better and add to this README. Maybe one day it ill be an installable application, but for now it is just some scripts.

I'm using Windows, so the instructions are focused there. If you are on Linux, this should be easy for you. For Apple users, I am happy to help, but am least familiar with this OS. In theory, this should work on all 3 platforms.

### Prerequisites

1. An lds.org account
2. A calling in the Bishopric with the correct access permissions
3. Python 3 
4. Dominate - Python HTML Builder
5. wkhtmltopdf - Qt WebKit HTML to PDF rendering engine
6. pdfkit - Python wrappers for wkhtmltopdf
7. lds-org - Python wrapper for the lds.org API

### Installation
#### Python 3
[Download](https://www.python.org/downloads/) the Python installer. Install Python with the downloaded .exe. Include the option to add Python to your Windows PATH.
From your favorite commandline tool, (Start >> cmd >> Enter), the following result confirms a valid install:
```commandline
>python -V
Python 3.5.1
```
Your version may vary.

#### VirtualEnv
Optional, but a good idea, use a [Python Virtual Environment](https://docs.python.org/3/library/venv.html)

#### Install [Dominate](https://github.com/Knio/dominate) 
Use pip:
```
pip install dominate
```
#### Install wkhtmltopdf

[Download](https://wkhtmltopdf.org/downloads.html) the install file for your OS. Run the install and then add the location to the .exe to your Windows PATH.
For me the path to add was:
```
C:\Program Files\wkhtmltopdf\bin
```
[Here is a PATH how to.](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)

#### Install pdfkit
Use pip:
```
pip install pdfkit
```
#### Install LDS-org
Use pip:
```
pip install lds-org
```
You will need to get into the org_chart.py and sub_org.py and change:
```python
 with lds_org.session(creds.usr, creds.pwd) as lds:
```
to your lds.org username and password, as shown.
```python
 with lds_org.session('your_lds.org_username', 'your_lds.og_password') as lds:
```

Optionally, you could create a file named creds.py with the following contents:
```python
usr='your_lds.org_username'
pwd='your_lds.og_password'
```
For both methods you actually need to replace the text placeholders with your actual username and password.

#### Grab The Code

Download the zip or git clone.

### Use
In the unzipped or git cloned directory you should find the file html_org_chart.py. Using cmd.exe navigate to this folder. Type the following:
```commandline
python html_org_chart.py
```

Html pages and the pdf should be in the html folder where ever you git cloned or unzipped the code.