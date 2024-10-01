# KAKFA ORDER PROCESSING SYSTEM
You are part of a small startup, and your team is tasked with creating a real-time order processing system. Your goal is to build a pipeline that ingests order data from a REST API, processes the data, and stores it in a PostgreSQL database for further analysis.

## FILE STRUCTURE
├── docker-compose.yml <br>
├── Dockerfile <br>
├── requirements.txt <br>
├── kafka_consumer.py <br>
├── create_connectors.sh <br>
├── postgres_init.sql <br>
├── db.json <br>
└── .gitpod.yml

## STEP BY STEP IMPLEMENTATION

- Using Gitpod,
  - Make an account on Gitpod, using your github/gmail
  - Make a github repository for the required code and clone it on your local PC, use VSCode or a code editor of your choice (most preferred)
  - Create a new gitpod workspace using "https://gitpod.io/#https://github.com/yourusername/my-repository-name"
  - Add the files as per files directory mentioned above after getting into the workspace
- After creating workspace, Gitpod will automatically run the commands specified in .gitpod.yml file
- This will create all the containers needed as specified per problem statement
- If the system is working properly,
  - The JSON server should be generating random order data
  - The Kafka consumer should be processing this data and sending it to the enriched_orders topic
  - The PostgreSQL sink connector should be writing the enriched data to the database.

