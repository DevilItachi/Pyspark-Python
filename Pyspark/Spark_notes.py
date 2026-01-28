- Spark is an open source unified computeing enigne with set of librairies for parallel data processing on compute cluster
- Supports Scala, Python, Java, R. It is built on top of scala
- Process data in RAM, 100 times faster than hadoop MapReduce
- Spark components on high level
        1. Low level API - RDD & Distributed Variables
        2. Strucutered API - Dataframes and Datasets and SQL
        3. Libraries & ecosysytems , strucutral streamiong and advances analytics
- Driver
        - IT is heart if spark
        - Manages information and state of executors
        - Analyse , distribute and schedule work on executors
        - GIves instrucition to executors
        - Cluster manager resides in Driver, which is mostly YARN or Kubernetes
- Executors
        - Execute the actual work
        - Respond the driver with the execution status
        - JVM machine
        - It runs in cluster mechine and consists of cores
- Task
        - Whatever work each executor does is called task
- Stages
        - In how many level the task was performed 
- Shuffle 
        - Shuffle is operation which divides the job in stages or data into partitions.
- Each task can only work on 1 partition of data at a time
- Tasks can execute in parallel
- Executors hosts cores and each core can run 1 task at a time
- Simply , user assign a job to driver, the driver analyzse and distribute  and breaks the job into stages and tasks and assign to executors.
- 1 core -> 1 task -> 1 partition
- Partition
        - To allow every executors  to work in parallel, sparks breaks down the data into chunks called partition
- Transformation
        - Instruction or code to modify and transform data is knows as transformation.
        - eg. select, where, groupby
        - Transformation help in building the logical plan
        - 2 types
            1. Narrow - After appying transformation each parititon contribute to atmoost 1 partition
            2. Wide - After appying transformation each parititon contribute to more than 1 partition
- Action
        - To trigger execution we need to call an action.
        - This basically executes the plan created by transformation
        - Eg. count
        - Actions are of 3 types
            1. View data in console
            2. Collect data to native language
            3. write data to output data source
- Lazy evaluation
        - Spark will wait till the last moment to execute the plan
        - Spark will not execute the plan until an action is called
        - This allows spark to optimze plan and use resources properly for execution.
- Spark Session
        - Driver process is knows as spark session
        - Spark session is the entry point for spark
        - Spark session instance executes code in cluster
        - 1 spark application will have 1 spark session
- Structures API - Dataframes(DF)
        - Dataframes is most common strucutres API , respresented as table inform of rows and columns
        - Dataframes has schema which is metadta for column
        - Data in datframes are in partition
        - Dataframe are immutable , you cant change anything once a df is created
        - Can create a new df from exisiting df
-Execution plan
        - Spark will create a logical plan and physical plan for the code
            1.  Logical plan is created by transformation
            2.  Physical plan is created by action
                Logical Planning 
                    code supplied > Unresoled plan > checks in catalogs > resolve logical plan > catalyst optimizer > optimized plan > DAG 
                - Once optimized logical plan is ready , spark generates multiple physical plan based on cluster & physcial confirguratioin.
                This Physcial plans runs against a cost model whch basically generates cost for each physical plan.
                - Once cost is validated spark selects the best phycial plan
                - That physcial plan is sent to cluster for execution
                - Once executor receives the phycial plan they run it  against the data partition.
- DAG ( Directed Acyclic Graph)

















