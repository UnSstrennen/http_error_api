# HTTP Error API

[**Star me on GitHub!**](https://github.com/UnSstrennen)

This simple project made for web developers who need to test their apps about correct error handling.

## How to use that?

Just make a request in format like `http://httpme.tk/<status_code>`. **HTTPS is also supported!**

Python example:
```python
from requests import get


get('http://httpme.tk/200')  # <Response [200]>
get('http://httpme.tk/401')  # <Response [401]>
get('http://httpme.tk/404')  # <Response [404]>
get('http://httpme.tk/500')  # <Response [500]>
```

&copy; Un Sstrennen, 2020
