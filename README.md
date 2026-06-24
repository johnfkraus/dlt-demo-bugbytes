# dlt-demo-bugbytes

dlt (data load tool) - Python data extraction / loading tool!


In this video, we'll look at dlt (data load tool) for extracting and loading data in Python. dlt comes with various integrations and can help standardize your ELT pipelines.

📌 𝗖𝗵𝗮𝗽𝘁𝗲𝗿𝘀:
00:00 Intro to dlt
01:05 Installing dlt
03:00 dlt pipeline example
04:44 Creating our own dlt REST API pipeline
10:10 Inspecting data with dlt and streamlit
13:26 Working with pipeline SQL client
18:18 dlt filtering and transformations

𝗦𝗼𝗰𝗶𝗮𝗹 𝗠𝗲𝗱𝗶𝗮:
📖 Blog: https://bugbytes.io/posts/
👾 Github: https://github.com/bugbytes-io/

📚 𝗙𝘂𝗿𝘁𝗵𝗲𝗿 𝗿𝗲𝗮𝗱𝗶𝗻𝗴 𝗮𝗻𝗱 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
dlt: https://dlthub.com/
dlt pipelines: https://dlthub.com/docs/build-a-pipel... 
dlt REST APIs:  http://dlthub.com/docs/dlt-ecosystem/...
dlt & streamlit: https://dlthub.com/docs/general-usage... 

#python #dlt #dataengineering


https://www.youtube.com/watch?v=iNxRemknAdQ


dlt init rest_api duckdb

 dlt init rest_api duckdb
Creating a new pipeline with the dlt core source rest_api (Generic API Source)
NOTE: Beginning with dlt 1.0.0, the source rest_api will no longer be copied from the verified sources repo but imported from dlt.sources. You can provide the --eject flag to revert to the old behavior.
Do you want to proceed? [Y/n]: y

Your new pipeline rest_api is ready to be customized!
* Review and change how dlt loads your data in rest_api_pipeline.py
* Add credentials for duckdb and other secrets to ./.dlt/secrets.toml
* requirements.txt was created. Install it with:
pip3 install -r requirements.txt
* Read https://dlthub.com/docs/walkthroughs/create-a-pipeline for more information


pip install "dlt[duckdb]"


https://jsonplaceholder.typicode.com/


Running youtube bugbytes DLT tutorial with duckdb destination. When I run the rest_api_pipeline.py code, I get:
<class 'dlt.load.exceptions.LoadClientJobFailed'>
Job with `job_id=users.4dd08c969e.insert_values.gz` and `load_id=1782290523.779166` failed terminally with message: Constraint Error: Duplicate key "id: 1" violates primary key constraint.. The package is aborted and cannot be retried.
No duckdb files exists.

My code says:
destination=dlt.destinations.duckdb("bugbytes_rest_api.duckdb"),

but still no duckdb file is created. Why not?

add path fixed it.


uv pip install streamlit

dlt pipeline jsonplaceholder_api show

WARNING: Install dlt[hub] for workspace dashboard and mcp support
(dlt-demo-bugbytes) (.venv) blauerbock dlt-demo-bugbytes % 

uv pip install "dlt[hub]"

dlt pipeline jsonplaceholder_api show



You must install additional dependencies to run `Workspace Dashboard`. If you use pip you may do the following: 
 
uv pip install "marimo"
uv pip install "pyarrow" 
uv pip install "ibis-framework" 
 
NOTE: Please refer to our docs at 'https://dlthub.com/docs/reference/command-line-interface#dlt-pipeline' for further assistance. 

dlt pipeline jsonplaceholder_api show


Duckdb doesn't create primary keys automatically.

Delete database file before running sql to create PKs.

