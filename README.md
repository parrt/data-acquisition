Data acquisition
=======


There are lots of exciting and interesting problems in analytics, such as figuring out what the right question is, selecting features, training a model, and interpreting results. But all of that presupposes a tidy data set that is suitable for analysis or training models. Industry experts all agree that data collection and cleaning is roughly 3/4 of any analysis effort.  This course teaches how to collect, coalesce, and clean data from multiple sources in preparation for your analysis work. 

This certificate course is part of the [Data Institute at the University of San Francisco](http://www.sfdatainstitute.org/).


# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Analytics program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES.** 101 Howard Street, Room 153 (main floor behind the elevators). As you walk in, cut to the left just before the elevators.

**TEMPORAL COORDINATES.** 1-4:30pm Saturdays, March 18 - April 29 (6 sessions). No meeting Apr 15, Easter weekend.

**INSTRUCTION FORMAT**. Class runs for 3.5 hours. Instructor-student interaction during lecture is encouraged and we'll do lots of mini-exercises / labs during class. All programming will be done in the Python 2 programming language, unless otherwise specified.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**STUDENT EVALUATION**.  Letter grades will not be assigned, though I'm happy to give you private feedback about how well you did. Those attending at least 5 out of 6 classes will get the official certificate. I will assign projects that you can work on outside of class and I will go over the solutions.

**ON DISABILITIES.** If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact USF Student Disability Services (SDS) at 415/422-2613 within the first week of class, or immediately upon onset of the disability, to speak with a disability specialist. If you are determined eligible for reasonable accommodations, please meet with your disability specialist so they can arrange to have your accommodation letter sent to me, and we will discuss your needs for this course. For more information, please visit http://www.usfca.edu/sds/ or call 415/422-2613.

# Syllabus

## Python refresher

* [Say Hello](https://github.com/parrt/msan501/blob/master/lightning/hello.md)
* (Optional) ['Bash' your way to victory](https://github.com/parrt/msan501/blob/master/notes/bash-intro.md) 
* [Simple statements and functions](https://github.com/parrt/msan501/blob/master/notes/area.md)
* [Lists and loops](notes/lists.md)
* [Matrices](notes/matrix.md)
* [Importing library code](https://github.com/parrt/msan501/blob/master/notes/imports.md)
* [Importing your own code](notes/myimport.md)
* [Reading and writing files](https://github.com/parrt/msan501/blob/master/notes/files.md)

## Data formats

* (Optional) [representing text in a computer](https://github.com/parrt/msan692/blob/master/notes/text.md); see also [7-bit ascii codes](http://www.asciitable.com/), [unicode vs ascii in python](https://docs.python.org/2/howto/unicode.html) 
* [Data conversion](https://github.com/parrt/data-acquisition/blob/master/hw/pipeline.md) (Converting stock history from Yahoo finance to various formats) (**project**)
	* reading delimited data; tsv, csv
	* reading/generating XML
	* reading/generating json
* [Excel](https://github.com/parrt/msan692/blob/master/notes/excel.md) (Saving as CSV, stripping non-ASCII stuff, loading into Python)
* [PDF using pdf2txt.py](https://github.com/parrt/msan692/blob/master/notes/pdf.md) (Parsing documents from Eisenhower's presidential library)
* [HTML](https://github.com/parrt/msan692/blob/master/notes/html.md) (Parsing Tesla's IPO prospectus)
* (Optional) [Parsing web access log files](https://github.com/parrt/msan692/blob/master/notes/logs.md)

## How the web works

* [Network sockets](https://github.com/parrt/msan692/blob/master/notes/sockets.md), DNS, email
* [client/server architecture](https://github.com/parrt/msan692/blob/master/notes/client-server.md)
* [HTTP](https://github.com/parrt/msan692/blob/master/notes/http.md)
* [flask](https://github.com/parrt/msan692/blob/master/notes/flask.md)
* [Web analytics](https://github.com/parrt/msan692/blob/master/notes/webanalytics.md)
* [Cookies](https://github.com/parrt/msan692/blob/master/notes/cookies.md), logging in/out
* [Building web servers](https://github.com/parrt/data-acquisition/blob/master/hw/server.md) (**project**)

## Data sources

* files
* [Pulling data from (open) REST APIs](https://github.com/parrt/msan692/blob/master/notes/openapi.md)
 * yahoo
 * openpayments.us
 * IMDB movie data
* Pull data from sites requiring an ID
 * [Zillow](https://github.com/parrt/msan692/blob/master/notes/zillow.md)
 * [Youtube](https://github.com/parrt/msan692/blob/master/notes/youtube.md)
* [APIs requiring authentication/identification](https://github.com/parrt/msan692/blob/master/notes/authapi.md)
 * [LinkedIn](https://github.com/parrt/msan692/blob/master/notes/linkedin.md)
 * [Facebook](https://github.com/parrt/msan692/blob/master/notes/facebook.md)
* [Extracting data from web pages](https://github.com/parrt/msan692/blob/master/notes/scraping.md)
  * [Crawling](https://github.com/parrt/msan692/blob/master/notes/crawling.md)
  * [buzzfeed](https://github.com/parrt/msan692/blob/master/notes/buzzfeed.md)
  * [Amazon](https://github.com/parrt/msan692/blob/master/notes/amazon.md)
  * [Scraping data from tables](https://github.com/parrt/msan692/blob/master/notes/scraping-tables.md)
* [Selenium](https://github.com/parrt/msan692/blob/master/notes/selenium.md)

## Feature extraction

* [Computing TFIDF](https://github.com/parrt/msan692/blob/master/notes/tfidf.pdf)
* [TFIDF document summarization](https://github.com/parrt/data-acquisition/blob/master/hw/tfidf.md) (**project**)
* regex
* Unix commands for extracting web content: wget, grep, awk, cut, paste, join, sed
* k-means for compression, color selection

## Misc

* Running shell commands from Python
* [San Francisco police incidents word clouds and heat maps](https://github.com/parrt/msan692/blob/master/notes/sfpd.md)
