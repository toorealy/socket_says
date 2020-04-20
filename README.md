# socket_says
A wrapper for the very common use of the `socket` library.
## Usage
### Importing
```python
>>> from socket_says import SocketSays
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

### Error Behavior
If no connection can be established, a message will be written to stdout.
