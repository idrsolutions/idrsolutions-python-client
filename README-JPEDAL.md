# IDRSolutions Python Client for JPedal #

Convert PDF to Images with Python, using the IDRSolutions Python Client to
interact with IDRsolutions' [JPedal Microservice Example](https://github.com/idrsolutions/jpedal-microservice-example).

The JPedal Microservice Example is an open source project that allows you to
convert PDF to Images by running [JPedal](https://www.idrsolutions.com/jpedal/) as an online service.

IDR Solutions offer a free trial service for running JPedal with Python,
more infomation on this can be found [here.](https://www.idrsolutions.com/jpedal/convert-pdf-in-python/)

-----

# Installation #

```
pip install IDRCloudClient
```
For other methods / ways to install, check out the [Python Docs](https://packaging.python.org/tutorials/installing-packages).

-----

# Usage #

## Basic: (Upload) #

```python
from IDRSolutions import IDRCloudClient
client = IDRCloudClient('http://localhost:8080/' + IDRCloudClient.JPedal)

# Convert the file with the input method specified
results = client.convert(input=IDRCloudClient.UPLOAD, file='path/to/file.pdf')

# Return a URL where you can view the converted output.
print(results['downloadUrl'])

# Download the converted output to a specified directory:
client.downloadResult(results, 'path/to/output/dir')
```

## Basic: (Download) #
```python
from IDRSolutions import IDRCloudClient
client = IDRCloudClient('http://localhost:8080/' + IDRCloudClient.JPedal)

# Convert the file with the input method specified
results = client.convert(input=IDRCloudClient.DOWNLOAD, url='http://link.to/filename')

# Return a URL where you can view the converted output.
print(results['downloadUrl'])

# Download the converted output to a specified directory:
client.downloadResult(results, 'path/to/output/dir')
```

The parameters object should contain the parameters that are sent to the API
See the [API](https://github.com/idrsolutions/jpedal-microservice-example/blob/master/API.md) for more details.

See `exampleJPedalUsage.py` for examples.

-----

# Who do I talk to? #

Found a bug, or have a suggestion / improvement? Let us know through the Issues page.

Got questions? You can contact us [here](https://idrsolutions.zendesk.com/hc/en-us/requests/new).

-----

# Code of Conduct #

Short version: Don't be an awful person.

Longer version: Everyone interacting in the JPedal Python Client project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](CODE_OF_CONDUCT.md).

-----

Copyright 2018 IDRsolutions

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
