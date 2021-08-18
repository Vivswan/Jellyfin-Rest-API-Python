from create_query_classes import create_query_classes

if __name__ == '__main__':
    # create_data_classes("http://localhost:8096/api-docs/openapi.json", "data_classes")
    create_query_classes("http://localhost:8096/api-docs/openapi.json", "query_classes", "data_classes")
