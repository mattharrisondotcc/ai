# Student Information

* 1001486942
* mbh6942
* Matthew Harrison

# Program Information

* Language: Python3
* Code is *not* Omega server compatible

# Code Structure

A main() function is called if the program is invoked itself (ie not imported).
The main() function processes the CLI arguments or prints help info using
argparse. A function validates the input file name(s), and another function
reads the files and processes the lines into tokens.

Edges are stored from the input file as a bidrectional defaultdict of
defaultdicts. This is to prevent key errors if a city name is not present or
mistyped for some reason; when the city is used as a key, the default value None
will be returned rather than raising a key error. "Bidirectional" means the city
names can be indexed in either order, ie edges[city1][city2] ==
edges[city2][city1]

There are two search functions, one each for informed search and uninformed
search. Informed search takes a heuristic function data structure (a
defaultdict with default value of 0).

Uninformed search is just a wrapper function for informed search, however it
builds a heuristic where all values are 0, nullifying the "informed" part of
informed search.

# How to run:

Navigate to the directory with "find_route" and execute this:

$ python3 find_route $origin_city $destination_city [heuristic_file.txt]

where $origin_city is the start city and $destination_city is the goal city.

heuristic_file.txt is optional.

Example to find the optimal route between 'Bremen' and 'Kassel' using
'h_kassel.txt' as the heuristic:

$ python3 find_route Bremen Kassel h_kassel.txt

# Additional Information

Help information can be viewed with:

`python3 find_route -h`

The program will print the help info and exit if arguments are entered
improperly.
