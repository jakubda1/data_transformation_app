## How to Run In Docker:

    Flask app is setup to port 8080 and broadcast on 0.0.0.0 due to dockerization
    
    Build it
        docker build -t aggregator .

    Run it
        docker run -p 8080:8080 aggregator

    Test it
        test_curl_with_full_data.sh

## How to run in CLI

    cat input_data.json | python data_aggregator_cli.py currency country
    cat input_data.json | python data_aggregator_cli.py currency country city

## How to run without docker

    python aggregator_flask_app.py

Flask need authentication (see [test_curl_with_full_data.sh](tests/test_curl_with_full_data.sh) )

Or in the source :)

## Future Improvements

Application could have register endpoint for registering tokens and save it locally or to database

Create minimal database to contain data and result for future retrieving of the data.
Alternatively grabs results from filesystem under requests ip address (substitution for user)

## Approach

During the development I have applied TDD in order to ensure and fast test of desired outputs.
In the [test](tests/test_datatransformations.py) are classes three classes.
Two of those are to test classes described bellow and third as integration test that is bound
to [input_data.json](data/input_data.json)

In file [datahandler](core/datahandler.py) I have created two classes:

    OriginData
    DataHandler

Each of those classes has a responsibility, going bottom-up

### OriginData

Is class to elemental data such as:
{
"country": "US",
"city": "Boston",
"currency": "USD",
"amount": 100
}
inside a class where is stored, class has a function to handle loading input data and transformation to desired state
according to input keys parameters

### DataHandler

Is class that contains list of the OriginData, handles loading the data from multiple inputs and feeding it in correct
state into the OriginData (not validated hardly enough to be called exactly **robust**, but it is what it is).

Also handles the aggregation of the data into according to the keys desired from input.

This approach was chosen to have multiple classes that has single responsibility of handling the data. It was used as
this is open to future implementations and changes to more seamlessly integrate into system if in the future will be
request to handle data in different way and to still contain old functionality

## Conclusion

In this task I have implemented a functionality of data transformation and aggregation accordingly to keys in the input
json.
There is a CLI version of the application that handles file input from stdin and keys for transformation. As there is no
exact specification for number of aggregation keys I have decided that there should be at least two.
Another working solution is web application written in Flask with only single POST endpoint /api/v1/parse-me/ .
Try/see [test_curl_with_full_data.sh](tests/test_curl_with_full_data.sh). This application is also dockerizable

Another approach to handle the data transformation was with using pandas library, where instead of classes will be one
transformation function to achieve same result and would be faster in implementation than painfully transform the nested
dicts in desired conditions. Also app is lightweight and only dependency is Flask.
