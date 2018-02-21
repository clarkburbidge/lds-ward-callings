# LDS Ward Callings

If you are an LDS Ward Clerk or Bishopric member you may have the need to view all the members of the ward and their callings.
This Python 3 code pulls the data that you are authorized to view from lds.org via the official API, formats it, builds some html pages, and writes a PDF document for printing.

![Demo Web Page](/demoimg.png?raw=true "Demo Web Page")

## Getting Started

For now you will need to use the run the Python code and install the needed libraries.

If it is not clear to you how to do this, my code may not be of help to you. I am interested in making this more accessible, so add an issue and if I have the time I'll try and explain better and add to this README. Maybe one day it ill be an installable application, but for now it is just some scripts.

### Prerequisites

1. An lds.org account
2. A calling in the Bishopric with the correct access permissions. 
3. Python 3
4. [Dominate](https://github.com/Knio/dominate)
5. [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
6. pdfkit
lds-org - 

### Installation
#### Python 3
[Download](https://www.python.org/downloads/) the Python installer 

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
You will need to get into the code and change:
```
creds.usr
```
to your lds.org username and
```
creds.pwd
```
to your lds.org password.

Optionally, you could create a file named creds.py with the following contents:
```python
usr='your_lds.org_username'
pwd='your_lds.og_password'
```
Where you replace the text placeholders with your actual username and password.

#### Grab The Code

Download the zip or git clone.

### Use

