# Exercises
1. Perform steps outlined in assignment, in the [README.md](./README.md) file in this directory. Submit your progress, along with a description of how far you got, and where you got stuck. You will have an opportunity to submit with all tests correct in the next module. 
2. Participate in the Discord Channel on Construction and Testing, helping your course mates when they get "stuck", or soliciting mutual aid when you are "stuck". If you have not already joined, here is a link: https://discord.gg/ACMShYGn 

## Progress
First, let me say that I did complete the 10 given tests as requested. I still need to figure out what other tests I should write. I made RestoreData.py a function that runs for each test to ensure data integrity and so I didn't have to run it between running pytest. 

## Issues
I struggled to get a virtual environment to work on the Linux subsystem on Windows. I used pytest without it, but I don't think that will be an issue. At first I thought we had to use the given functions to access json data, but once I realized I was supposed to access the different layers of data as though it was a dictionary, it was a lot easier. I also realize that for comparisons, lists are easier to use, but it was unexpected that functions such as view_assignments returned a list instead of a dict.