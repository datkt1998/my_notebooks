# 1 Choose a notebook solution

Có 2 hướng tiếp cận để sử dụng được notebook:

- - **Colab Enterprise**:
    - **Chia sẻ và cộng tác**: Dễ dàng chia sẻ notebook với người dùng khác, nhóm Google hoặc miền Google Workspace.
    - **Quản lý hạ tầng**: Không cần quản lý hạ tầng, Colab Enterprise tự động cung cấp và tắt runtime khi không cần thiết.
    - **Tích hợp dịch vụ Google Cloud**: Tích hợp với các dịch vụ như Vertex AI và BigQuery.
- **Vertex AI Workbench**:
    - **Tùy chỉnh cao**: Hỗ trợ nhiều loại instance Jupyter notebook và có thể thêm môi trường conda.
    - **Tích hợp dữ liệu**: Truy cập dữ liệu từ Cloud Storage và BigQuery trực tiếp trong JupyterLab.
    - **Lập lịch và quản lý chi phí**: Có thể chạy notebook theo lịch trình và tự động tắt khi không hoạt động.



| **Feature**                     | **Colab Enterprise**                | **Vertex AI Workbench**             |
| ------------------------------- | ----------------------------------- | ----------------------------------- |
| *Environment*               | Managed, collaborative              | Customizable, developer-focused     |
| *Infrastructure Management* | Serverless, managed by Google       | User-controlled, flexible           |
| *Collaboration*             | Excellent, with IAM control         | Good, with GitHub integration       |
| *Compute Provisioning*      | Automatic                           | User-configurable                   |
| *Data Integration*          | Seamless with Google Cloud services | Seamless with Google Cloud services |
| *Code Completion*           | Inline                              | Inline                              |
| *Customization*             | Limited                             | Extensive                           |
| *GPU Support*               | ✓                                   | ✓                                   |
| *Conda Environments*        | ✗                                   | ✓                                   |
| *Custom Containers*         | ✗                                   | ✓                                   |
| *Automated Notebook Runs*   | ✗                                   | ✓                                   |
| *Idle Shutdown*             | Automatic                           | Configurable                        |
| *Persistent Storage*        | ✗                                   | ✓                                   |
| *Access to VM*              | ✗                                   | ✓                                   |
| *Original Jupyter UI*       | Modified                            | Retained                            |
**Khi nào nên sử dụng**:
- **Colab Enterprise**: Khi cần chia sẻ và cộng tác dễ dàng, không muốn quản lý hạ tầng.
- **Vertex AI Workbench**: Khi cần tùy chỉnh cao và tích hợp sâu với các dịch vụ dữ liệu của Google Cloud.
## 1.1 Colab Enterprise
([doc](https://cloud.google.com/vertex-ai/docs/colab/create-console-quickstart))

**Key Features:**
- 🔗 **Share and Collaborate:** Easily share notebooks with individuals, Google groups, or entire Google Workspace domains. Access control is handled through Google Cloud’s IAM.
- 🌐 **Managed Compute:** Colab Enterprise takes care of provisioning and managing compute resources. It starts runtimes when needed and shuts them down when not in use.
- ✅ **Google Cloud Integration:** Seamlessly work with Google Cloud services like Vertex AI and BigQuery from within your notebook.
- ✨ **Inline Code Completion:** Write code faster with suggestions that pop up as you type.
- **Runtime**: a compute resource to run code in notebook
- **Runtime template**: configure the template to optimize a runtime's performance, cost, and other characteristics based on demand and problem.
	> Read [**Machine type & disk type**](https://cloud.google.com/compute/docs/machine-resource) to select resources suitable for the purpose

**Cons:**
- **Less efficient with heavy workloads**: extended for long tasks or want the data to persist on the disk of the machine once it's turned off (or released, in this case)
- **Not control the environment**

**Pricing**: base on amount of used resources time include:
- **Compute Engine**: the virtual machine that runs the notebook
- **Storage**: data + source code
- **Networking**: Communication between notebook and other services
## 1.2 Vertex AI Workbench

**Key Features:**
- 👨🏻‍💻 **Access to the VM:** Unlike Colab Enterprise, you get full access to the virtual machine itself, allowing for in-depth configuration tailored to your specific needs. You can integrate more easily with your GCP environment based on IAM.
- 📦 **Persistent Storage:** Data isn't lost when the machine restarts, as the VM's disk is retained, ensuring your data remains intact.
- ☑ **Controlling Instance Types:** Choose from several types of instances, including N2 CPU or any GPU offering that GCP has.
- 🤏 **Preinstalled Packages and GPU Support:** All instances come with JupyterLab and a suite of deep learning packages like TensorFlow and PyTorch, with GPU support available.
- </> **GitHub Integration:** Sync your notebooks with GitHub for version control and collaboration.
- 💾 **Custom Environments and Containers:** Add conda environments or create custom containers to tailor your setup to specific needs, so you don't need to install dependencies every time a team member wants to launch a new machine.
- 👾 **Data Integration:** Access Cloud Storage and BigQuery directly from JupyterLab by identifying either as the user working on the notebook or as a service account.
- 🛠️ **Automated Notebook Runs and Idle Shutdowns:** Schedule notebook runs and automatically shut down idle instances to manage costs effectively.
- 🖥️ **Original Jupyter UI:** Workbench retains more of the original Jupyter UI, providing a cleaner and more familiar interface for users accustomed to Jupyter notebooks.

**Pricing**: base on amount of used resources time include:
- **CPU + RAM + GPU (if used)**: Charge only while running instance and execute code
- **Storage (boot disk + data disk)**: alway charging even if the instance is shutdown, this is because the data is stall stored on the disk
-  **Workbench management fees**: only charge when the instance is running

	*Tips*
	- If there is any scheduled tasks (like running notebook in the instance), those tasks will still execute even if the instance is shutdown, then this would be charged for the resources used during those executions
	- Cost of **Persistent storage** base on the the actual amount of provisioned disk space. Therefore, it's still a good idea to choose a size that's appropriate for needs.
	- The data should be stored in cloud storage (like buckets), you're charged based on the **amount of data you actually store** in the bucket. This is called "used storage" and is a more flexible way to pay for storage.

### 1.2.1 Setup Instances

#### 1.2.1.1 [Create an instance](https://cloud.google.com/vertex-ai/docs/workbench/instances/create#create)

#### 1.2.1.2 Instance shutdown

**Shutdown event:**
- Manual click to `shutdown`
- After the idle inactive period
- There is no kernel activity for the specified time period
> 	running a cell or new output printing to a notebook is activity that resets the idle shutdown timer

**Billing**:
- While your instance is shut down, there are *no CPU or GPU usage charges* except for scheduled executions that run during the shutdown
- *Disk storage charges still apply* while your instance is shut down. For more information, see [Pricing](https://cloud.google.com/vertex-ai/pricing#notebooks).

**Automated shutdown**: Shut down after being idle for a specific time period by default

**Scheduled executions**: Scheduled executions run while instance is shut down

**gcloud CLI config**:
- Create instance
```cmd
gcloud workbench instances create INSTANCE_NAME --metadata=idle-timeout-seconds=86400
```
- Update instance
```cmd
gcloud workbench instances update INSTANCE_NAME --metadata=idle-timeout-seconds=86400
```

#### 1.2.1.3 [Change the machine type and configure GPUs](https://cloud.google.com/vertex-ai/docs/workbench/instances/change-machine-type#change_the_machine_type_and_configure_gpus)

#### 1.2.1.4 [Migrate your data to a new Vertex AI Workbench instance](https://cloud.google.com/vertex-ai/docs/workbench/instances/migrate#migrate-data)

#### 1.2.1.5 [Remote SSH](https://cloud.google.com/vertex-ai/docs/workbench/instances/ssh-access)
#### 1.2.1.6 [Limitation](https://cloud.google.com/vertex-ai/docs/workbench/instances/introduction#limitations)

### 1.2.2 Schedule run noteboook

**Set scheduler**
1. Next to your instance's name, click **Open JupyterLab
2. In the folder **File Browser**, double-click the example notebook file to open it.
3. Click the ![](https://cloud.google.com/static/vertex-ai/docs/workbench/images/icon-executor.png) **Execute** button.
4. In the **Submit notebooks to Executor** dialog, in the **Type** field, select **Schedule-based recurring executions**.
    > By default, the executor runs your notebook file every hour at the `00` minute of the hour.
5. In **Advanced options**, enter a name for your bucket in the **Cloud Storage bucket** field, and then click **Create and select**. The executor stores your notebook output in the Cloud Storage bucket.
6. Click **Submit**. Your notebook file runs automatically on the schedule that you set.

[**View, share, and import an executed notebook file**](https://cloud.google.com/vertex-ai/docs/workbench/instances/schedule-notebook-run-quickstart#view_share_and_import_an_executed_notebook_file)

### 1.2.3 Connect to data

#### 1.2.3.1 [BigQuery Table](https://cloud.google.com/vertex-ai/docs/workbench/instances/bigquery)

##### 1.2.3.1.1 [Browse BigQuery resources](https://cloud.google.com/vertex-ai/docs/workbench/instances/bigquery#browse_resources)
 In ![BigQuery](https://cloud.google.com/static/bigquery/images/bigquery_icon.png) **BigQuery in Notebooks**. The **BigQuery** pane lists available projects and datasets
 <img src = "https://cloud.google.com/static/bigquery/images/international_top_terms.png">
 
##### 1.2.3.1.2 [Query by Bigquery Magic Command](https://cloud.google.com/vertex-ai/docs/workbench/instances/bigquery#query_data_by_using_the_bigquery_magic_command)

To use these magics, you must first register them. Run the `%load_ext` magic in a Jupyter notebook cell.
```python
%load_ext google.cloud.bigquery
```

The `%%bigquery` magic runs a SQL query and returns the results as a pandas `DataFrame`
```python
%%bigquery  
SELECT name, SUM(number) as count  
FROM `bigquery-public-data.usa_names.usa_1910_current`  
GROUP BY name  
ORDER BY count DESC  
LIMIT 10
```

**Assign the query results to a variable**
```python
%%bigquery df
SELECT name, SUM(number) as count  
FROM `bigquery-public-data.usa_names.usa_1910_current`  
GROUP BY name  
ORDER BY count DESC  
LIMIT 10

df
```

**Explicitly specify a project**
```python
project_id = 'your-project-id'

%%bigquery --project $project_id  
SELECT name, SUM(number) as count  
FROM `bigquery-public-data.usa_names.usa_1910_current`  
GROUP BY name  
ORDER BY count DESC  
LIMIT 10
```

**Run a parameterized query**
```python
params = {"limit": 10}

%%bigquery --params $params  
SELECT name, SUM(number) as count  
FROM `bigquery-public-data.usa_names.usa_1910_current`  
GROUP BY name  
ORDER BY count DESC  
LIMIT @limit
```

Get a summary of data
``` python
%bigquery_stats bigquery-public-data.google_trends.top_terms
```
After running for some time, an image appears with various statistics on each of the 7 variables in the `top_terms` table. The following image shows part of some example output:

![International top terms overview of statistics.](https://cloud.google.com/static/bigquery/images/jupyter-overview-of-statistics.png)
##### 1.2.3.1.3 [Query by Bigquery Client Library](https://cloud.google.com/vertex-ai/docs/workbench/instances/bigquery#query_data_by_using_the_client_library_directly)

```python
from google.cloud import bigquery

class BigqueryConnector:
    def __init__(self, project_id):
        self.project_id = project_id
        self.client = bigquery.Client(project_id)

    def read_query(
        self, query: str, chunk_size: int | None = None
    ) -> Union[Iterator[pd.DataFrame], pd.DataFrame]:
        """
        Executes a BigQuery query and returns an iterator of pandas DataFrames if chunk_size is provided,
        otherwise returns a single pandas DataFrame.
        """
        query_job = self.client.query(query)
        result = query_job.result(page_size=chunk_size)
        return (
            result.to_dataframe_iterable()
            if chunk_size
            else result.to_dataframe()
        )

    def read_table(self, table_id):
        table = self.read_query(f"SELECT * FROM `{table_id}`")
        return table

    def write_bq(self, dataframe, table_id, if_exists="append", schema=None):
        write_mode = (
            "WRITE_TRUNCATE" if if_exists == "replace" else "WRITE_APPEND"
        )
        schema = (
            [
                bigquery.SchemaField(
                    name,
                    type_.upper(),
                    "NULLABLE" if mode is None else mode.upper(),
                )
                for name, type_, mode in schema
            ]
            if schema is not None
            else []
        )
        job_config = bigquery.LoadJobConfig(
            schema=schema,
            write_disposition=write_mode,
        )
        job = self.client.load_table_from_dataframe(
            dataframe, table_id, job_config=job_config
        )
        job.result()
        
    # write a function to update value in bigquery
    def update_bq(self, table_id, update_value, conditions={}):
        for k in update_value.keys():
            if isinstance(update_value[k], str):
                update_value[k] = f"'{update_value[k]}'"
        for k in conditions.keys():
            if isinstance(conditions[k], str):
                conditions[k] = f"'{conditions[k]}'"
        set_stasement = ", ".join(
            [f"{k} = {v}" for k, v in update_value.items()]
        )
        conditions = "".join(
            [f" and {k} = {v}" for k, v in conditions.items()]
        )
        sql = f"""
        UPDATE `{table_id}`
        SET
        {set_stasement}
        WHERE
        1 = 1 {conditions}
        """
        # return sql
        job = self.client.query(sql)
        job.result()

    def create_table(
        self, table_id, fields, partition_by=None, cluster_by=None
    ):
        schema = [
            bigquery.SchemaField(
                i["name"],
                i["type"].upper(),
                mode=(i["mode"] if "mode" in i else "NULLABLE"),
            )
            for i in fields
        ]
        table = bigquery.Table(table_id, schema=schema)
        if partition_by:
            partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY,
                field=partition_by,
            )
            table.time_partitioning = partitioning
        if cluster_by:
            table.clustering_fields = cluster_by
        self.client.create_table(table, exists_ok=True)
        print(f"Created table '{table_id}' successfully.")
```

#### 1.2.3.2 [Cloud Storage buckets](https://cloud.google.com/vertex-ai/docs/workbench/instances/cloud-storage)

To mount and then access a Cloud Storage bucket, do the following:
1. In JupyterLab, make sure the folder **File Browser** tab is selected.
2. In the left sidebar, click the ![](https://cloud.google.com/static/vertex-ai/docs/workbench/images/icon-mount-shared-storage.png) **Mount shared storage** button. If you don't see the button, drag the right side of the sidebar to expand the sidebar until you see the button.
    
    ![The Mount shared storage button in the top right corner of the left sidebar](https://cloud.google.com/static/vertex-ai/docs/workbench/instances/images/mount-shared-storage-button.png)
3. In the **Bucket name** field, enter the Cloud Storage bucket name that you want to mount.
4. Click **Mount**.
5. Your Cloud Storage bucket appears as a folder in the **File browser** tab of the left sidebar. Double-click the folder to open it and browse the contents.

### 1.2.4 [Github integration](https://cloud.google.com/vertex-ai/docs/workbench/instances/save-to-github)
### 1.2.5 Maintain

#### 1.2.5.1 [Add a new conda environment](https://cloud.google.com/vertex-ai/docs/workbench/instances/add-environment#add_a_conda_environment)

If to want using `pip`
```cmd
conda install pip
pip install <PACKAGE>
pip install -r requirements.txt
```

#### 1.2.5.2 Modify a conda kernel

Vertex AI Workbench instances come with pre-installed frameworks such as PyTorch and TensorFlow. If you need a different version, you can modify the libraries by using `pip` in the relevant conda environment.

For example, if you want to upgrade PyTorch:
```cmd
# Check the name of the conda environment for PyTorch
conda env list

# Activate the environment for PyTorch
conda activate pytorch

# Display the PyTorch version
python -c "import torch; print(torch.__version__)"

# Make sure to use pip from the conda environment for PyTorch
# This should be `/opt/conda/envs/pytorch/bin/pip`
which pip

# Upgrade PyTorch
pip install --upgrade torch
```

#### 1.2.5.3 Delete a conda kernel

Some conda packages add default kernels to your environment when the packages are installed. For example, when you install R, conda might also add a `python3` kernel. This can cause a duplication of kernels in your environment. To avoid duplicated kernels, delete the default kernel before you create a new kernel with the same name.

```cmd
rm -rf /opt/conda/envs/CONDA_ENVIRONMENT_NAME/share/jupyter/kernels/python3
```
### 1.2.6 [Monitor](https://cloud.google.com/vertex-ai/docs/workbench/instances/monitor-health)

### 1.2.7 Control access

### 1.2.8 [Troubleshooting](https://cloud.google.com/vertex-ai/docs/general/troubleshooting-workbench?component=any#instances)

### 1.2.9 Usage Tips

#### 1.2.9.1 Idle Shutdown 😴

<img src = "https://cdn-images-1.readmedium.com/v2/resize:fit:800/1*CfhsxHPu0hiFhPpJwEFX1A.png">

**Purpose**: automatically turns off your notebook or virtual machine when you haven’t used it for a while
1. **Save Money**: When your notebook sits idle, it’s still using resources that you’re paying for. With auto-shutdown, you avoid those costs by having the system shut down on its own. This can really cut down on expenses (especially when using GPUs like A100).
2. **Make the Most of Resources**: Cloud providers have a limited number of resources to go around. If your notebook is just sitting there doing nothing, it’s using up space that could be used by others. Auto-shutdown helps free up those resources for everyone to use, making the cloud system work better for everyone.
3. **Eco-Friendly:** Less idle notebooks mean less energy is being used. This is good for the environment because it helps reduce the energy needed to run data centers, which in turn lowers the carbon footprint.

#### 1.2.9.2 Add tags/label 🏷️

**Purpose**: Label instance or service in Google Cloud, help to organize resources better
1. **Control Access**: Tags allow you to set specific access controls and permissions based on them.
2. **Save Money:** Tags help you track costs. You can set alerts for stuff with certain tags, so you know how much you’re spending.
3. **Stay Organized**: Tags group things based on where they belong, like “production,” “development,” or by team. It keeps everything in order.
4. **Manage Operations**: Tags make it easier for tools that work with Google Cloud to organize resources. This is especially useful for keeping track of what’s happening, reporting, and watching over resources.
5. **Find Things Quickly**: In the Google Cloud Console or using the `gcloud` tool, tags help you spot things fast.

#### 1.2.9.3 Update the Python version

**Purpose**: change to a different Python version

**Step in Terminal**
1. Open `Terminal`
2. Create the Python environment called `py311` using `conda create` command.
```cmd
conda create -n py311 python=3.11 --y
```
3. Once created activate it as follows:
```cmd
conda activate py311
```
4. Install the IPython kernel (`ipykernel`), that allows users to interactively run Python code and display the output within a notebook
```cmd
conda install ipykernel
```

Install `IPython`
```cmd
ipython kernel install --name "py311" --user
```

**Step by `bash script`**
1. Create a bash file: `create_conda_env.sh`
```bash
#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 environment_name python_version"
    exit 1
fi

ENV_NAME=$1
PYTHON_VERSION=$2

# Create a new conda environment with the provided name and Python version
conda create -n $ENV_NAME python=$PYTHON_VERSION --yes

# Activate the new environment
conda activate $ENV_NAME

# Install ipykernel in the activated environment
conda install ipykernel --yes

# Install the environment as an IPython kernel
ipython kernel install --name "$ENV_NAME" --user
```
2. Execute bash file
```cmd
# give it execute permissions
chmod +x create_conda_env.sh

# run it in a terminal
./create_conda_env.sh py311 3.11

# If you work on a GPU with a preinstalled conda version you can update conda
conda install cudatoolkit=CUDA_VERSON -y
```

### 1.2.10 [Notebook example](https://cloud.google.com/vertex-ai/docs/workbench/notebooks#notebook-list)