from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

def loadData(jsonFile, name):
    maxRetries = 5
    # http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html tutorial!
    mysession = boto3.session.Session(aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY') # this accesses the keys in the 'credentials' file in ~/.aws/
    #mysession = boto3.session.Session(profile_name="davis2") # for specifying user
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table(name)

    with open(jsonFile) as json_file:
        listings = json.load(json_file, parse_float = decimal.Decimal)
        for listing in listings:
            counter = 0
            URL = listing['URL']
            category = listing['category']
            condition = listing['condition']
            country = listing['country']
            currency = listing['currency']
            endTime = listing['endTime']
            ID = listing['id'] # case not matching because I didn't realize id is a keyword
            price = listing['price']
            inputQuery = listing['inputQuery']
            shipsTo = listing['shipsTo']
            title = listing['title']
            imageURL = listing['imageURL']
            site = listing['site']

            print("Adding listing: ", title)

            while(counter != maxRetries):
                try:
                    table.put_item(
                       Item={
                           'URL': URL,
                           'category': category,
                           'condition': condition,
                           'country': country,
                           'currency': currency,
                           'endTime': endTime,
                           'id': ID,
                           'price': price,
                           'inputQuery': inputQuery,
                           'shipsTo': shipsTo,
                           'title': title,
                           'imageURL': imageURL,
                           'site': site
                        }
                    )
                    counter = 0
                    break
                except:
                    counter = counter + 1
