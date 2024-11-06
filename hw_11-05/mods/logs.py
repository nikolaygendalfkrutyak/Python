import logging
lg_products = logging.getLogger("log_products")
lg_products.setLevel(logging.DEBUG)

format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# file_handler = logging.FileHandler("main.log")
# file_handler.setLevel(logging.ERROR)
# file_handler.setFormatter(format)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(format)

# lg_products.addHandler(file_handler)
lg_products.addHandler(stream_handler)
