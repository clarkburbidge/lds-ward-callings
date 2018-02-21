# LDS Ward Callings

If you are an LDS Ward Clerk or Bishopric member you may have the need to view all the members of the ward and their callings.
This Python 3 code pulls the data that you are authorized to view from lds.org via the official API and then formats it, builds some html pages and writes a PDF document for printing.

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

### Installation
####Python 3
[Download](https://www.python.org/downloads/) the Python installer 

####VirtualEnv
Optional, but a good idea, use a [Python Virtual Environment](https://docs.python.org/3/library/venv.html)

####Install [Dominate](https://github.com/Knio/dominate) 
Use pip:
```
pip install dominate
```

https://wkhtmltopdf.org/downloads.html

####Install pdfkit
Use pip:
```
pip install pdfkit
```