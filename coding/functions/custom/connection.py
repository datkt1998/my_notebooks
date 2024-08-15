import os
import sqlite3
import cx_Oracle
import pandas as pd
import pymongo
from google.cloud import bigquery
from munch import DefaultMunch
from sqlalchemy import create_engine, types
from tqdm import tqdm as tqdm_
from datetime import datetime
from google.cloud.exceptions import NotFound

# from os.path import exists


def showlog(mylogger=None, level="error"):
    """Lựa chọn muốn print ra trên console hay ghi vào file log
    Returns:
        _type_: _description_
    """
    if mylogger is None:
        return print
    else:
        level = level.lower()
        if level == "error":
            return mylogger.error
        elif level == "warning":
            return mylogger.warning
        elif level == "info":
            return mylogger.info
        elif level == "critical":
            return mylogger.critical


# connect to SQL/noSQL database
class Database:
    """Setup kết nối tới database oracle/sqlite và các thao tác: đọc, ghi, tạo, xóa, phân quyền"""

    def __init__(self, **kwargs):
        self.kwargs = DefaultMunch.fromDict(kwargs)
        self.hostname = self.kwargs["hostname"]
        self.username = self.kwargs["username"]
        self.password = self.kwargs["password"]
        self.port = self.kwargs["port"]
        self.service_name = self.kwargs["service_name"]
        self.path = self.kwargs["path"]
        self.uri = self.kwargs["uri"]
        self.database_name = self.kwargs["database_name"]
        self.collection_name = self.kwargs["collection_name"]
        self.type = self.kwargs["type"]
        self.logger = self.kwargs["logger"]
        self.connect()

    def connect(self, printStatus=True):
        self.conn = None
        try:
            if (self.type == "oracle") or (self.service_name is not None):  # oracle
                try:
                    self.conn = cx_Oracle.connect(
                        user=self.username,
                        password=self.password,
                        dsn=f"{self.hostname}:{self.port}/{self.service_name}",
                    )
                    self.engine = create_engine(
                        f"oracle+cx_oracle://{self.username}:{self.password}@{self.hostname}:{self.port}/?service_name={self.service_name}"
                    )
                    self.type = "oracle"
                    if printStatus:
                        showlog(mylogger=self.logger, level="info")(
                            f"Success to connect to ORACLE {self.hostname}:{self.port}/{self.service_name}"
                        )
                except:
                    self.conn = None

            elif self.type == "sqlite3" or (self.path is not None):
                self.conn = sqlite3.connect(self.path)
                self.engine = sqlite3.connect(self.path)
                self.type = "sqlite3"
                filename = os.path.basename(self.path)
                if printStatus:
                    showlog(mylogger=self.logger, level="info")(
                        f"Success to connect to Sqlite3 {filename}"
                    )

            elif self.conn is None:  # mongodb
                if self.uri is None:
                    hostname = (
                        self.hostname if self.hostname is not None else "localhost"
                    )
                    port = self.port if self.port is not None else "27017"
                    if self.username is not None:
                        self.uri = f"mongodb://{self.username}:{self.password}@{hostname}:{port}/admin?authSource=admin&authMechanism=SCRAM-SHA-1"
                    else:
                        self.uri = f"mongodb://{hostname}:{port}/"
                self.client = pymongo.MongoClient(self.uri)

                if self.database_name is not None:
                    self.database = self.client[self.database_name]
                    if self.collection_name is not None:
                        self.collection = self.database[self.collection_name]
                self.type = "mongodb"
                if printStatus:
                    showlog(mylogger=self.logger, level="info")(
                        f"Success to connect to MongoDB {hostname}:{port}"
                    )

        except Exception as e:
            showlog(mylogger=self.logger, level="error")(
                "Fail to connect to database !"
            )
            raise e


class DatabaseSQL(Database):
    def __init__(self, **kwargs):
        super(DatabaseSQL, self).__init__(**kwargs)

    # @runtime
    def drop(self, tablename, schema=None):
        # Drop table if exists
        cursor = self.conn.cursor()
        tablename = (
            "{}.{}".format(schema, tablename) if schema is not None else tablename
        )
        showlog(mylogger=self.logger, level="warning")(
            f"Droping {tablename.upper()} table if exists."
        )
        cursor.execute(
            f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {tablename.upper()}'; EXCEPTION WHEN OTHERS THEN NULL; END;"
        )
        showlog(mylogger=self.logger, level="warning")(
            f"Droped {tablename.upper()} table if exists."
        )

    def create(self, tablename: str, typeCol: dict, schema=None):
        def check_exists_table(tablename, schema, conn):
            sql = f"""
            select count(*) from user_tables 
            where table_name = '{tablename}'
            and tablespace_name= '{schema}'
            """
            cnt = pd.read_sql_query(sql, conn).iloc[0, 0]
            if cnt == 0:
                showlog(mylogger=self.logger, level="warning")(
                    f"There are no {tablename.upper()} table"
                )
                return False
            else:
                # hp.cfg['log'].info(f'There are no {tablename.upper()} table')
                return True

        if check_exists_table(tablename, schema, self.engine) == False:
            try:
                tablename = (
                    "{}.{}".format(schema, tablename)
                    if (schema is not None)
                    else tablename
                ).upper()
                cursor = self.conn.cursor()
                schemaCol = ", ".join(
                    ["{} {}".format(i, typeCol[i]) for i in typeCol.keys()]
                )
                cursor.execute(f"CREATE TABLE {tablename} ({schemaCol})")
                showlog(mylogger=self.logger, level="info")(
                    f"Created {tablename.upper()} table in {schema.upper()}"
                )
                return True
            except:
                showlog(mylogger=self.logger, level="error")(
                    f"Fail to created {tablename.upper()} table in {schema.upper()}"
                )

    def describe(self, tablename):
        if self.configs_database.type == "oracle":
            return pd.read_sql_query(
                f"Select COLUMN_NAME, DATA_TYPE, DATA_LENGTH from ALL_TAB_COLUMNS where TABLE_NAME = '{tablename}' ",
                self.conn,
            )
        else:
            raise "Not set describe for non-Oracle connection"

    def getdtype(dataSchema):
        """Convert dtype từ dict trên yaml sang sqlalchemy, tạo tham số khi đẩy dữ liệu lên database

        Args:
            dataSchema (_type_): _description_
        """

        def convert_tool(x: str):
            if x.lower() == "date":
                return types.DATE()
            elif x.lower().startswith("varchar2"):
                lenght_varchar2 = int(x[x.index("(") + 1 : x.index(")")])
                return types.VARCHAR(lenght_varchar2)
                # return types.CLOB()
            elif "float" in x.lower():
                return types.FLOAT()
            elif "integer" in x.lower():
                return types.INTEGER()

        return {i: convert_tool(dataSchema[i]) for i in dataSchema.keys()}

    # @logs(logger = hp.cfg['log'])
    def upload(
        self,
        data,
        dataSchema,
        tablename: str,
        schema=None,
        chunksize=5000,
        if_exists="append",
        filename=None,
        logIndex=True,
    ):
        try:
            dty = Database.getdtype(dataSchema) if dataSchema is not None else None
            data.to_sql(
                tablename.lower(),
                schema=schema,
                con=self.engine,
                if_exists=if_exists,
                chunksize=chunksize,
                index=False,
                dtype=dty,
            )

        except Exception as e:
            withIndex = f" from {data.index[0]} to {data.index[-1]}" if logIndex else ""
            showlog(mylogger=self.logger, level="error")(
                f"Fail to upload data {filename}{withIndex} with error: {e}"
            )

    def access(self, toUser, tablename, access="select", schema=None):
        """
        grant select/insert/update/delete on <schema>.<table_name> to <username>;
        """
        cursor = self.conn.cursor()
        tablename = (
            "{}.{}".format(schema, tablename) if schema is not None else tablename
        )
        cursor.execute(f"""grant {access} on {tablename} to {toUser};""")
        self.conn.commit()
        cursor.close()
        print(f"Set {toUser} to {access} in {tablename} !")

    def createIndex(self, indexname, tablename, cols, schema=None):
        """
        CREATE INDEX <indexname> ON <schema.tablename> (cols);
        """
        cursor = self.conn.cursor()
        cols_list = cols if type(cols) != list else ", ".join(cols)
        tablename = (
            "{}.{}".format(schema, tablename) if schema is not None else tablename
        )
        cursor.execute(f"""CREATE INDEX {indexname} ON {tablename} ({cols_list});""")
        self.conn.commit()
        cursor.close()
        # conn.close()
        print(f"Set {indexname} as index to {cols_list} in {tablename} !")

    # @runtime
    def read(
        self,
        table_name_sql: str = None,
        col_name="*",
        offset_rows: int = 0,
        n_records: int = -1,
        chunksize: int = None,
        position=0,
    ):
        self.connect(False)
        if table_name_sql is None:
            if type(self.conn) == cx_Oracle.Connection:
                return pd.read_sql_query(
                    "SELECT OWNER,TABLE_NAME,TABLESPACE_NAME  FROM all_tables",
                    self.engine,
                )
            else:
                return pd.read_sql_query("SELECT *  FROM sqlite_master", self.engine)

        if type(self.conn) == cx_Oracle.Connection:
            offset_clause = " offset {} rows ".format(offset_rows)
            num_records_clause = (
                "" if n_records == -1 else " fetch next {} rows only".format(n_records)
            )
            combine_clause = offset_clause + num_records_clause
        else:  # sqlite3
            offset_clause = (
                "" if offset_rows == 0 else " offset {} ".format(offset_rows)
            )
            num_records_clause = (
                "limit -1" if n_records == -1 else " limit {} ".format(n_records)
            )
            combine_clause = num_records_clause + offset_clause

        if "select " not in table_name_sql.lower():
            cols = col_name if type(col_name) == str else ", ".join(col_name)
            sql = """
            select {} from {} {}
            """.format(
                cols, table_name_sql, combine_clause
            )
        else:
            sql = table_name_sql + " " + combine_clause
        tablename = sql.split(" ")[sql.lower().split(" ").index("from") + 1]
        res = pd.read_sql_query(sql=sql, con=self.engine, chunksize=chunksize)
        if chunksize is not None:
            res = tqdm_(res, desc=tablename, position=position)
        # print("Bảng {} offset {} dòng, {} records".format(table_name,offset_rows,n_records) + ("" if chunksize is None else ", chunksize {}".format(chunksize)))
        return res


class GcpConnector:

    def __init__(self, project_id="ext-pinetree-dw"):
        self.project_id = project_id
        self.authen()
        self.client = bigquery.Client(self.project_id)

    def authen(self):

        def oper():
            os.system("gcloud auth application-default login")
            with open(os.path.join(pathcf, "gcp_authen_date.txt"), "w") as file:
                file.write(today)

        today = datetime.today().strftime("%Y%m%d")
        pathcf = os.path.dirname(os.path.abspath(__file__))
        file_exists = os.path.exists(os.path.join(pathcf, "gcp_authen_date.txt"))
        try:
            if not file_exists:
                oper()
            else:
                with open(os.path.join(pathcf, "gcp_authen_date.txt"), "r") as file:
                    line = file.readline()
                if today != line:
                    oper()
        except:
            oper()

    def estimate_query_size(self, sql, end="\n", name=None):

        def convert_byte_to_MB_or_GB(byte_amount):
            MB = byte_amount / (1024 * 1024)
            if MB >= 1024:
                GB = MB / 1024
                return f"{GB:,.2f} GB"
            else:
                return f"{MB:,.2f} MB"

        job_config = bigquery.QueryJobConfig()
        job_config.dry_run = True
        job_config.use_query_cache = False
        query_job = self.client.query(
            (sql),
            job_config=job_config,
        )
        size = convert_byte_to_MB_or_GB(query_job.total_bytes_processed)
        cost = round((query_job.total_bytes_processed / 1024**4) * 5.5, 4)
        name = "" if name is None else f"({name}) | "
        tex = (
            name
            + f"Query size: {size}, estimated cost: ${cost} ({cost*25000:,.0f} VND)"
        )
        return tex

    def query(self, sql, chunk_size=None, check_size=False, name=None):

        tex = self.estimate_query_size(sql, name=name)
        if check_size:
            check_size = (
                False
                if input(tex + ". --> Continue query? (y/n): ").lower() == "y"
                else True
            )
        else:
            print(tex)

        if not check_size:
            job = self.client.query(sql)
            # size = chunk_size if isinstance(chunk_size, int) else 50000
            res = job.result(page_size=chunk_size)
            if chunk_size is None:
                return res.to_dataframe()
            return res.to_dataframe_iterable()

    def get_table_schema(self, table_id):
        table = self.client.get_table(table_id)
        # convert Table object to dict (so we can change things)
        table_def = table.to_api_repr()
        return table_def["schema"]["fields"]

    def change_table_schema(self, table_id, table_field_schema):
        table = self.client.get_table(table_id)
        # convert Table object to dict (so we can change things)
        table_def = table.to_api_repr()
        # change new description of fields
        table_def["schema"]["fields"] = table_field_schema
        # convert the dict back to a Table object
        table = table.from_api_repr(table_def)
        # call patch with just the values under "schema"
        self.client.update_table(table, ["schema"])

    def create_table(self, table_id, table_field_schema, partition_by=None):
        def if_tbl_exists(client, table_ref):
            try:
                client.get_table(table_ref)
                return True
            except NotFound:
                return False
            
        table_name = table_id.split(".")[-1]
        if not if_tbl_exists(self.client, table_id):
            schema = [
                bigquery.SchemaField(i, table_field_schema[i].upper())
                for i in table_field_schema
            ]
            table = bigquery.Table(table_id, schema=schema)
            table.time_partitioning = bigquery.TimePartitioning(
                type_="DAY",
                field=partition_by,
                expiration_ms=1000 * 24 * 60 * 60 * 90,  # 90 days
            )
            table = self.client.create_table(table)
            print(
                f"Created table \'{table_name}\'"
                + (
                    f" with partition by \'{partition_by}\'"
                    if partition_by is not None
                    else ""
                ),
            )
        else:
            print(f"Table \'{table_name}\' already exists",)

    def write_df_to_bigquery(self, df, table_id, if_exists="append", column_datatype=None):
        write_mode = "WRITE_TRUNCATE" if if_exists == "replace" else "WRITE_APPEND"
        column_datatype = (
            [bigquery.SchemaField(i, column_datatype[i].upper()) for i in column_datatype]
            if column_datatype is not None
            else []
        )
        job_config = bigquery.LoadJobConfig(schema=column_datatype, write_disposition=write_mode)
        job = self.client.load_table_from_dataframe(
            df,
            table_id,
            job_config=job_config,
        )
        job.result()
        print("Loaded {:,.0f} rows into \'{}\'".format(job.output_rows, table_id.split(".")[-1]))
