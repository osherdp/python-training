# Chat Exercise

## Goals

1. Learning about client-server communication
2. Learning about the `socket` and `select` APIs
3. Experience integration testing

## Introduction

In this exercise, you'll write a program that enables two users to send text messages from one the the other.
The program should be console-based. No need in fancy, overrated GUI :).

> :warning: Consulting with others regarding technical work is generally a good idea. With regular work, it's encouraged to pair programming and helping each other.
  **However**, when it comes to learning a language, this is not the case. Attempting to tackle exercises alone is a hugh part of learning, even if the result is not perfect. If you'll get something wrong, the reviewer will let you know.
  Please refrain from consulting with others when working on training exercises.

## Point-to-point client

The program should:

* receive messages from the other client and print them
* get input from the user and send messages to the other client.

Configuration given to the client should allow:

* configuring the point they connect to by hostname/IP address and port
* configuring the port to connect to
* choosing a desired nickname for the user

## Interface

Usage example:

```
$ python chat.py --help
Run the client component of the chat.

Usage:
    chat.py <local-port> <remote-host> <remote-port> [--username <name>]
    chat.py (-h | --help)

Options:
    -u <name>, --username <name>    The user nickname [default: guest].
    -h, --help                      Show this message and exit.
```

## Recommendations

* **A MUST** - [Sockets how-to](https://docs.python.org/3/howto/sockets.html) from the official Python documentation.
* The built-in modules `socket` and `select`
* The third party library `docopt` (hint: the interface given above is highly compatible with `docopt`)
