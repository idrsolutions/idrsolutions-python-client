IDRSolutions Python Client with JPedal
======================================

Convert PDF to Images with Python, using the IDRSolutions Python Client to
interact with IDRsolutions' `JPedal Microservice Example`_.

The JPedal Microservice Example is an open source project that allows you to
convert PDF to Images by running `JPedal`_ as an online service.

IDR Solutions offer a free trial service for running JPedal with Python,
more infomation on this can be found `here.`_

--------------

Installation
------------

Using PIP:
~~~~~~~~~~

::

    pip install IDRCloudClient

For other methods / ways to install, check out the `Python Docs`_.

--------------

Usage
-----

Basic:
~~~~~~

First, import IDRCloudClient and setup the converter details by creating a new
``IDRCloudClient`` object :

::

    from IDRSolutions import IDRCloudClient
    client = IDRCloudClient('http://localhost:8080/' + IDRCloudClient.JPEDAL)

You can now convert files by calling the methods available. ``convert()`` will
start the conversion process. For example to convert to images :

::

    # Convert the file with the input method specified
    results = client.convert(input=IDRCloudClient.UPLOAD, file='path/to/file.pdf')

    # Return a URL where you can view the converted output.
    print(results['downloadUrl'])

Alternatively, you can specify a url from which the server will download the
file to convert.

::

    # Convert the file with the input method specified
    results = client.convert(input=IDRCloudClient.DOWNLOAD, url="http://link.to/filename")

    # Return a URL where you can download the converted output.
    print(results['downloadUrl'])

Once you have converted the file you can also specify a directory to download
the converted output to:

::

    # Download the converted output to a specified directory:
    client.downloadResult(results, 'path/to/output/dir')

Additional parameters can be used in ``convert()``, they are defined in our
`API`_

--------------

Changes for docker version
--------------------------

If your JPedal service requires authentication, you can set the username and password by passing an additional tuple argument as shown below:
::

    from IDRSolutions import IDRCloudClient
    client = IDRCloudClient('http://localhost:8080/' + IDRCloudClient.JPEDAL, auth=("username","password"))


--------------

Who do I talk to?
=================

Found a bug, or have a suggestion / improvement? Let us know through the
Issues page.

Got questions? You can contact us `here`_.

--------------

Code of Conduct
===============

Short version: Don't be an awful person.

Longer version: Everyone interacting in the IDRSolutions Python Client
project's codebases, issue trackers, chat rooms and mailing lists is
expected to follow the `code of conduct`_.

--------------

Copyright 2018 IDRsolutions

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. _JPedal Microservice Example: https://github.com/idrsolutions/jpedal-microservice-example
.. _JPedal: https://www.idrsolutions.com/jpedal/
.. _Python Docs: https://packaging.python.org/tutorials/installing-packages
.. _here: https://idrsolutions.zendesk.com/hc/en-us/requests/new
.. _code of conduct: CODE_OF_CONDUCT.md
.. _API: https://github.com/idrsolutions/jpedal-microservice-example/blob/master/API.md
.. _here.: https://www.idrsolutions.com/jpedal/convert-pdf-in-python/
