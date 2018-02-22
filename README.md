# LDS Ward Callings

If you are an LDS Ward Clerk or Bishopric member you may have the need to view all the members of the ward and their callings.
This Python 3 code pulls the data that you are authorized to view from lds.org via the official API, formats it, builds some html pages, and writes a PDF document for printing. All the positions will update with the most current data from the lds.org website every time the code is run.

We have a tri-fold magnetic whiteboard that has a loose organization of Ward members and their callings on magnetic tape. As members move in and out, and callings change, this board must be manually maintained. So far it has not been maintained, and is not a realistically sustainable solution. Now that it is out of date it is not useful. I hope this is more useful and sustainable.

![Demo Web Page](https://github.com/clarkburbidge/lds-ward-callings/blob/master/images/demo.png?raw=true "Demo Web Page")

## Getting Started

For now you will need to run the Python code and install the needed libraries.

If by reading the following steps, it is not clear to you how to do this, my code may not be of help to you. It is much closer to a nice script than a production application. I am however, interested in making this more accessible, so add an issue, and, if I have the time, I'll try and help. Maybe one day this will be an installable application, but for now it is just some scripts. Any help is appreciated. I'm sure my Python could use some love.

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
[Download](https://www.python.org/downloads/) the Python installer. Install Python with the downloaded .exe. Include the options for pip and to add Python to your Windows PATH.

From your favorite commandline tool, (Start >> cmd >> Enter), the following result confirms a valid install:

```commandline
>python -V
Python 3.5.1
>pip -V
pip 9.0.1 from .... (python 3.5)
```

Your versions may vary.

#### VirtualEnv
Optional, but a good idea, use a [Python Virtual Environment](https://docs.python.org/3/library/venv.html)

#### Install [Dominate](https://github.com/Knio/dominate) 
Use pip from the command line:
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
Use pip from the command line:
```
pip install pdfkit
```
#### Install [LDS-org](https://github.com/jidn/lds-org/)
Use pip from the command line:
```
pip install lds-org
```

#### Grab The Code

Download the zip or git clone.

To use the lds-org session you will need to use your lds.org username and password. I have created a Python file that pulls my username and password from a file that is not included in this repository. You will need make some changes to my code, or add the missing file to get the login to work. 

You could get into the files `org_chart.py` and `sub_org.py` and change:
```python
 with lds_org.session(creds.usr, creds.pwd) as lds:
```
`creds.usr` to your lds.org username and `creds.pwd` to your lds.org password, as shown below.

```python
 with lds_org.session('your_lds.org_username', 'your_lds.og_password') as lds:
```

Or, you could create a file named `creds.py` with the following contents:

```python
usr='your_lds.org_username'
pwd='your_lds.og_password'
```
For both methods you actually need to replace the text placeholders with your actual username and password. 

### Use
In the unzipped or git cloned directory you should find the file `html_org_chart.py`. Using cmd.exe navigate to this folder. Type the following:
```commandline
python html_org_chart.py
```

Html pages and the pdf should be in the html folder where ever you git cloned or unzipped the code.

Print the pdf pages and put them up on your out of date magnet board. If your Windows is set up to automatically open .html files with a web browser, you should only need to double click one of the .html files and navigate with the links at the top of each page. This would be great to project onto a wall or use on a larger TV.

### Future

I'd love to turn this into an app that can be used to display a more structured traditional "org chart" rather than the text list. I've been looking at Kivy and may keep trying to implement this there. Also there is a good looking API for Google Slides that might also work and be cross platform via a browser and a Google account.