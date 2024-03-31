# TCP Server and Client Implementation

This repository contains Python scripts for implementing a TCP server and client for handling multiple client connections concurrently.

## Server

### Description
- The server script (`server.py`) creates a TCP server that listens for incoming connections from clients.
- It utilizes threading to handle multiple client connections simultaneously, allowing each client to communicate with the server without blocking others.
- For each connection, the server receives a message from the client, prints it to the console, and echoes the message back to the client.
- The server can handle a special message, "quit", which instructs it to close the connection with the client that sent it.

### Usage
- Run the server script using Python: `python server.py`.
- By default, the server listens on `localhost` (127.0.0.1) and port `65432`. You can modify these parameters in the script if needed.

## Client

### Description
- The client script (`client.py`) connects to the TCP server using the specified host and port.
- After establishing a connection, the client prompts the user to enter messages to send to the server.
- Upon receiving a response from the server, the client prints this response to the console.
- If the user enters "quit", the client sends this message to the server and then closes the connection.

### Usage
- Run the client script using Python: `python client.py`.
- The client will prompt you to enter messages. Type your message and press Enter to send it to the server.
- If you want to exit, type "quit" and press Enter.

## Dependencies
- The scripts require Python 3.x to run.

## Note
- Make sure to run the server before running the client.
- You can customize the host and port parameters in both the server and client scripts to match your requirements.

