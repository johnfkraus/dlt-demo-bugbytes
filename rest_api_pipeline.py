import os
from pathlib import Path

import dlt
from dlt.sources.rest_api import (
    rest_api_source,
)

print(f"working directory: {os.getcwd()=}")
db_path = Path.cwd() / "bugbytes_rest_api.duckdb"

source = rest_api_source({
    'client': {
        'base_url': 'https://jsonplaceholder.typicode.com/',
    },
    'resources': [
        'users',
        'posts'
        ],
    "resource_defaults": {
        "write_disposition": "replace",
    }
})

pipeline = dlt.pipeline(
    pipeline_name="jsonplaceholder_api",
    destination="duckdb",
    # destination=dlt.destinations.duckdb(str(db_path)),
    dataset_name="my_api",
    # destination=dlt.destinations.duckdb("bugbytes_rest_api.duckdb"),
)

if __name__ == "__main__":
    pipeline.run(source)

    with pipeline.sql_client() as client:
        # add primary keys manually

        print(f"ALTER TABLE {pipeline.dataset_name}.users ADD CONSTRAINT users_pk PRIMARY KEY (id);")
        client.execute(f"ALTER TABLE {pipeline.dataset_name}.users ADD CONSTRAINT users_pk PRIMARY KEY (id);")
        client.execute(f"ALTER TABLE {pipeline.dataset_name}.posts ADD CONSTRAINT posts_pk PRIMARY KEY (id);")
