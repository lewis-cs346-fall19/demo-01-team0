net_server.py acts as a server and listens on port 25252.  It takes the original
message and sends it back to the receiver with the message "Here's the data:
Original message END" It closes the socket when done.

net_client.py acts as a client for the server.  It sends the message as h's. It
sends 1 through 10 h's and it adds an h to each message.  It then receives the message 
back from the server and prints out the modified message.
