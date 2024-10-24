import logging

logger = logging.getLogger(__name__)

def print_adaptor(data: bytes):
    logger.debug("Print Adabtor called")    
    print(f"----------------------")
    print(data)
    print(f"----------------------")


def temp_adaptors(data: bytes) -> None:
    pass
    
