***Analysis of US Road Accident Data using MapReduce***

**Task 1** - Find record count per hour. Find the number of accidents occuring per hour that satisfy a set of conditions and display them in sorted fashion.

**Task 2** - Find record count per city and state. Find the number of accidents occuring per city and state where the distance between the start coordinates of the accident and a given pair of coordinates - (LATITUDE, LONGITUDE) is within D. You will be using Euclidean Distance to find whether the distance calculated is within D.
For each record, you will be making a request to http://20.185.44.219:5000/ to obtain the city and state information. The IP accepts only POST requests, and expects a JSON payload containing a pair of start coordinates in the following format 

**LINK** - https://cloud-computing-big-data.github.io/A1.html
