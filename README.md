# V 0.1
# Dataset Integration program

In my final year Research I had to use patients protein data. I found a dataset from Gene Expression Omnibus(GEO) Data repo. Unfortunatly that dataset wasn't in way that i want. 
All 102 samples are stored in separate files. So I had to integrate these data to the one csv file. 

Dataset files have Tab separated 2 columns (Protein Name,Value). 

I created a simple python program to do this boring work.

## How it works
1. Read the dataset files one by one which stored in "data_files" folder
2. Create a python dictionary for the data(Protein name:value)
3. Get BPD stages from the GEO database using web scraping
4. Then create an array with the Sample_ID, Protein data values and BPD stages
5. Write Dictionary data to the new CSV file one by one in following structure [Data_ID,{Protein names},BPD_stage]

## How to Run
1. Clone the repo to your Computer
2. ### Create Virtual Environment
    ```
        $ python3 -m venv venv
    ```
    Activate Virtual Environment
    ```
        $ source venv/bin/activate
    ```
3. Install Requests library on venv
    ```
    (venv) $ python -m pip install requests
    ```
4. Install Beautiful Soup on venv
    ```
    (venv) $ python -m pip install beautifulsoup4
    ```
5. create a folder named "data_files" and copy all your dataset files.
6. If your dataset file extension is not ".txt" do the necessary changes in "process_files.py"
7. Run "main.py" file.