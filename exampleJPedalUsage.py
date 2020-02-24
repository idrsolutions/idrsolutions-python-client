from IDRSolutions import IDRClient

client = IDRClient('http://localhost:8080/' + IDRClient.JPEDAL)
try:
    # Upload a local file to he specified microservice
    # convert() returns an dictionary with the conversion results.
    conversionResults = client.convert(input=IDRClient.UPLOAD, file='path/to/file.pdf')

    # You can specify other parameters for the API as named parameters, for example
    # here is the use of the callbackUrl parameter which is a URL that you want to
    # be updated when the conversion finishes.
    # See https://github.com/idrsolutions/jpedal-microservice-example/blob/master/API.md
    # conversionResults = client.convert(input=IDRClient.UPLOAD,
    #                            callbackUrl='http://listener.url')

    # Alternatively, you can specify a url from which the server will download the file to convert.
    # conversionResults = client.convert(url='http://link.to/filename',
    #                            input=IDRClient.DOWNLOAD)

    outputURL = conversionResults['downloadUrl']

    # After the conversion you can also specify a directory to download the output to:
    # client.downloadResult(conversionResults, 'path/to/output/dir')

    if outputURL is not None:
        print("Converted: " + outputURL)
except Exception as error:
    print(error)
