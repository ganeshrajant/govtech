## Split the name field into first_name, and last_name
    - First we split the name by spaces
    - Once the spliting is done, we take the first part of the split as first_name and the last part as last_name

## Remove any zeros prepended to the price field
    - First we convert the price field to string because in case there is any trailing zeros it can be detected with a string
    - Once the Price field is string, we strip the prefix with zeros and store it in a new Price column

## Delete any rows which do not have a name
    - We used pandas dropna() method for the column "name" using the subset parameter

## Create a new field named above_100, which is true if the price is strictly greater than 100
    - First we checked whether the data types of price field is float or not
    - It was object, so we change the datatype to float first
    - Once it is in float format, we apply a condition wherever the price is > 100.0 assign True otherwise Fals and store it in a new column "above_100"

After all preprocessing, we stored the processed csv files into new files named "processed_dataset1.csv" and "processed_dataset2.csv"