from _config import SERVER_ADDRESS
from create_query_classes import create_query_classes

if __name__ == '__main__':
    # create_data_classes(f"{SERVER_ADDRESS}/api-docs/openapi.json", "data_classes")
    create_query_classes(f"{SERVER_ADDRESS}/api-docs/openapi.json", "query_classes", "data_classes")
