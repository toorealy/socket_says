# socket_says [![CircleCI](https://circleci.com/gh/toorealy/socket_says.svg?style=svg)](https://circleci.com/gh/toorealy/socket_says)
A wrapper for the very common use of the `socket` library.

## `socket_says` Class Usage
### Importing
```python
>>> from socket_says.socket_says import SocketSays
```
### Assigning
```python
>>> simon = SocketSays(<address>, <port>)
>>> simon = SocketSays() <-- Uses Defaults
```
The defaults are:
- Address: `127.0.0.1`
- Port: `80`
- Text: `'Hello'` <-- Because it's friendly
```python
>>> str(simon)
"You are telling 127.0.0.1 on port 80 'Hello'"
>>> repr(simon)
'<SocketSays(127.0.0.1,80,Hello)>'
```

### Usage

#### Sending
On your end...
```python
>>> simon.says(<text>)
>>> simon.says() #<-- Uses Default 'Hello'
>>> simon.says('SocketSays is easy')
```
And on the receiving end...
```
Hello
SocketSays is easy
```
#### Receiving
On the receiving end...
```
simon says touch your custom_errors
```
On your end...
```python
>>> simon.listens()
simon says touch your custom_errors

```

## `cliSocketSays` Usage
```bash
user@computer:~$ python3 cliSocketSays.py -a <addr> -p <port> -t <text>
user@computer:~$ python3 cliSocketSays.py -a 192.168.150.136 -p 7357 -t """Hello
old
friend
"""
```

### Error Behavior
If no connection can be established, a message will be written to stdout.
