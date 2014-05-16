pyglab
======

A Python wrapper for the [GitLab API
v3](http://doc.gitlab.com/ce/api/README.html).


Requirements<a name="requirements"></a>
------------

* Python 3 (<http://www.python.org>)
* `requests` library (<http://docs.python-requests.org/>)


Installation
------------

First, satisfy the [requirements](#requirements). Currently, there is only
the `requests` library, which you can get for Python 3 by executing

    pip3 install requests

For more information see the [install
page](http://docs.python-requests.org/en/latest/user/install/#install).

Then, clone the `pyglab` repository to a path of your liking and add the
location to the
[PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
variable.


Quick start
-----------

Right now, this section has not much content yet. Please refer to the source
code for how to use it :-/

In order to query a GitLab repository, create a `Pyglab` instance as easily as

    p = Pyglab(url, private_token)

If you do not know the private token, you can also login with a
username/password combination:

    p = Pyglab.login(username, password)

You can then use the `pyglab` instance to access the full API. For example,  to
show the current user, execute

    p.user.get()


Disclaimer
----------

No animals were harmed during the development of this library :)
