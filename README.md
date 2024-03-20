**What to Use**

Refer "ppt_overview.pdf" file. Study the structure of the input "help_all_class.txt", map the structure of your API. Ensure you have a similarly structured input. Download the script "classes_code.ipynb", make edits according to your API structure and specify the DTD files as per your organization. Run the script.

**Summary of the topic** 

A software has around 140+ APIs which are available in a python dictionary. These APIs are well structured and have a short description about their usage, keys, arguments etc. Currently, the help for these APIs are only available through the tool GUI or command prompt. The user does not have a PDF/HTML document. 

**Solution**

A tool command dumps the compiled information for all APIs in a python file (help.py). 

This project has a series of python scripts:
Using script one (get_help.py), you can process the help file from your tool (help.py) to segregate text files having tree-like structured information for containers, cont1.txt and cont2 (help_all_class.txt). 

Another script (classes_code.ipynb) parses the text information, help_all_class.txt, into XML format. 

**Results** 

The automated script uses the text files as input and creates individual chapter files in XML format (one for each of the APIs). 
You can import these XML files in your directory structure and compile them into a bookmap. 
After fixing a few validation errors, you can get a 1000+ page PDF, ready to review and release.

**Impact** 

Saves a one-time effort of 4-6 weeks for the API documentation team. Using the script, one can create a reference API manual in half a day’s time.
Saves the subsequent effort for every release when new APIs are added, or existing ones are updated. 
Other py-based software APIs could use this script and create a PDF/HTML for documentation. The total result is a savings of months of effort over subsequent releases. 

Currently, about 10% post-processing and formatting involved in the authoring environment. Subsequent updates to the project will have cleaner output.

**Current Dummy Project - Sample Work**

The dummy project replaces the content for these 140+ APIs with 11 dummy APIs (A,B,C,D,E,F,G,H,I,J,K). This example has the script2 which parses the content of help_all_class.txt into individual XML files. Sample outputs are placed under the Output folder.
