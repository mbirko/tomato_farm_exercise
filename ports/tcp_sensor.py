import socket
import logging

logger = logging.getLogger(__name__)

def handle(adaptor, conn: socket.socket, cli) -> None:
    while True: 
        logger.info(f"Connection from {cli}")
        try: 
            data = conn.recv (32)

            adaptor(data)
            if not data: 
                conn.close()
        except:
            return 

def startTCPServerThread(adaptor, HOST: str, PORT: int) -> None: 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, PORT))

    tcp_socket.listen(1)
    
    while(True):
        logger.info("Waiting for connection")
        conn, cli = tcp_socket.accept()
         
        try: 
            handle(adaptor, conn, cli)
        finally: 
            conn.close()
