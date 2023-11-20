# Dataset Integration program

In my final year Research I had to use patients protein data. I found a dataset from Gene Expression Omnibus(GEO) Data repo. Unfortunatly that dataset wasn't in way that i want. 
All 102 samples are stored in separate files. So I had to integrate these data to the one csv file. 

Dataset files have Tab separated 2 columns (Protein Name,Value). 

I created a simple python program to do this boring work.

## How it works
1. Read the dataset files one by one which stored in "data_files" folder
2. Create a python dictionary for the data(Protein name:value)
3. Then create an array with the dataset_ID
4. Write Dictionary data to the new CSV file one by one in following structure [Data_ID,{Protein names}]
