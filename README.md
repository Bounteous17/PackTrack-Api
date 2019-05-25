Check out the Wiki first!
https://github.com/bounteous/PackTrack-Api/wiki

# PackTrack-Api

The purpose of this APP is to provide the necessary services so that customers can send the encrypted content on the client side to another recipient of the content. On the client side before starting a chat, two private keys are generated using AES-256. During the course of message exchange between users, they make use of these individual secret keys to transmit the content through this API.

# Technologies

## Flask (Python 3.7.3)

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`\_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

## MongoDB

MongoDB is a database, the part of the application responsible for storing and retrieving information. MongoDB is a NoSQL database. Under the NoSQL umbrella we put all those databases that do not use the SQL language for querying the data.

## Redis

Redis in the NoSQL ecosystem. ... Redis (REmote DIctionary Server) is key-value in-memory database storage that also supports disk storage for persistence. It supports several data types: Strings, Hashes, Lists, Sets and Sorted Sets; implements publish/subscribe messaging paradigm and has transactions.

# Install guide

## Pip

#### ArchLinux / Manjaro

```bash
$ sudo pacman -Syu python-pip
```

#### Gentoo

```bash
$ sudo eix --sync
$ sudo emerge --ask dev-python/pip
```

#### Debian >= 8 / Ubuntu >= 16

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3-pip
```

#### Fedora >= 22

```bash
$ dnf update
$ dnf upgrade
$ dnf install python3-pip
```

## Running the app

```bash
$ git clone https://github.com/bounteous/PackTrack-Api.git
$ cd PackTrack-Api
```

#### Create the virtual environment

```bash
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
```

#### Activating the virtual environment

```bash
$ source env/bin/activate
```

#### Install dependencies

```bash
$ pip install -r requirements.txt
```

#### Build Docker container

```bash
$ docker-compose up --build
```

### Choose how you want to start the app (CLI or VScode)

#### CLI

```bash
$ python3 index.py
```

![alt text](https://imgur.com/MuNapAB.png)

#### VScode (debug)

![alt text](https://i.imgur.com/4gkwgDC.png)

# Links

- Personal blog: https://www.thelinuxsect.com
