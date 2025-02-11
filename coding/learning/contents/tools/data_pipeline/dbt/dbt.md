# DBT - Data Build Tool

## DBT overview

- Modeling changes are easy to follow and revert
- Explicit dependencies between models
- Explore dependencies between models
- Data quality tests
- Error reporting
- Incremental load or fact tables
- Track history of dimension tables
- Easy to access documantation

---
## DBT setup

### For Windows

#### Python
This is the Python installer you want to use: 

[https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe ](https://www.python.org/downloads/release/python-3113/)

Please make sure that you work with Python 3.11 as newer versions of python might not be compatible with some of the dbt packages.

#### Virtualenv setup
Here are the commands we executed in this lesson:
```
cd Desktop
mkdir course
cd course

virtualenv venv
venv\Scripts\activate
```

### For Mac

#### iTerm2
We suggest you to use _iTerm2_ instead of the built-in Terminal application.

https://iterm2.com/

#### Homebrew
Homebrew is a widely popular application manager for the Mac. This is what we use in the class for installing a virtualenv.

https://brew.sh/

Here are the commands we execute in this lesson:

```sh
mkdir course
cd course
virtualenv venv
. venv/bin/activate
```

### [dbt installation](https://docs.getdbt.com/docs/core/pip-install) 
```shell
pip install dbt-core dbt-ADAPTER_NAME
# or : pip install dbt-core dbt-bigquery
# or (run local): pip íntall dbt
#On Linux/Mac: which dbt
```

**dbt setup**

Initialize the dbt profiles folder on Mac/Linux:
```sh
mkdir ~/.dbt
```

Initialize the dbt profiles folder on Windows:
```sh
mkdir %userprofile%\.dbt
```

Create a dbt project (all platforms):
```sh
dbt init <dbt project path>
```

Then config the DBT connection

Let's check DBT connection after config

```shell
dbt debug
```

---
### About dbt projects / Folder structure

| Resource                                                              | Description                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [models](https://docs.getdbt.com/docs/build/models)                   | Each model lives in a single file and contains logic that either transforms raw data into a dataset that is ready for analytics or, more often, is an intermediate step in such a transformation.                                                                               |
| [snapshots](https://docs.getdbt.com/docs/build/snapshots)             | A way to capture the state of your mutable tables so you can refer to it later.                                                                                                                                                                                                 |
| [seeds](https://docs.getdbt.com/docs/build/seeds)                     | CSV files with static data that you can load into your data platform with dbt.                                                                                                                                                                                                  |
| [data tests](https://docs.getdbt.com/docs/build/data-tests)           | SQL queries that you can write to test the models and resources in your project.                                                                                                                                                                                                |
| [macros](https://docs.getdbt.com/docs/build/jinja-macros)             | Blocks of code that you can reuse multiple times.                                                                                                                                                                                                                               |
| [docs](https://docs.getdbt.com/docs/build/documentation)              | Docs for your project that you can build.                                                                                                                                                                                                                                       |
| [sources](https://docs.getdbt.com/docs/build/sources)                 | A way to name and describe the data loaded into your warehouse by your Extract and Load tools.                                                                                                                                                                                  |
| [exposures](https://docs.getdbt.com/docs/build/exposures)             | A way to define and describe a downstream use of your project.                                                                                                                                                                                                                  |
| [metrics](https://docs.getdbt.com/docs/build/build-metrics-intro)     | A way for you to define metrics for your project.                                                                                                                                                                                                                               |
| [groups](https://docs.getdbt.com/docs/build/groups)                   | Groups enable collaborative node organization in restricted collections.                                                                                                                                                                                                        |
| [analysis](https://docs.getdbt.com/docs/build/analyses)               | A way to organize analytical SQL queries in your project such as the general ledger from your QuickBooks.                                                                                                                                                                       |
| [semantic models](https://docs.getdbt.com/docs/build/semantic-models) | Semantic models define the foundational data relationships in [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) and the [dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl), enabling you to query metrics using a semantic graph. |
| [saved queries](https://docs.getdbt.com/docs/build/saved-queries)     | Saved queries organize reusable queries by grouping metrics, dimensions, and filters into nodes visible in the dbt DAG.                                                                                                                                                         |

```bash  
dbtlearn/              
├── README.md          
├── dbt_project.yml    # Configuration file for the dbt project, specifying project settings and configurations. 
│── profiles.yml         # Cấu hình kết nối tới Snowflake, BigQuery, Redshift, v.v.
│── packages.yml         # Quản lý các package dbt (tương tự requirements.txt của Python)
├── models/            # Contains SQL files that define dbt models, which are SQL queries that transform raw data into the desired format.  
│   ├── staging/         # Các bảng tạm (staging tables) trước khi chuyển đổi
│   ├── marts/           # Các bảng đầu ra (final data marts)
│   ├── intermediate/    # Các bảng trung gian (dùng cho transformation)
│   ├── sources.yml      # Định nghĩa nguồn dữ liệu (source tables)
│   └── schema.yml       # Định nghĩa schema, kiểm tra và tài liệu mô hình
├── snapshots/         # Contains SQL files that define dbt snapshots, which capture the state of a table at a specific point in time.  
├── tests/             # Contains SQL files that define dbt tests, which are used to validate the data and ensure data quality.  
├── macros/            # Contains SQL files that define dbt macros, which are reusable SQL snippets that can be used in models, tests, and other dbt files.  
├── seeds/             # Contains CSV files that are used to seed data into the database, providing static data that can be referenced in models.  
├── analysis/          # Contains SQL files for analysis purposes, allowing for ad-hoc queries and analysis outside of the main models.  
├── logs/              # Contains log files generated by dbt operations, useful for debugging and tracking the execution of dbt commands.  
│   └── dbt.log        # Log file for dbt operations  
└── target/            # Contains compiled files and artifacts generated by dbt, including the manifest file which contains metadata about the dbt project.  
    └── manifest.json  # JSON file containing the dbt manifest
```

---

## Configs & Properties

### Project configuration

`dbt_project.yml`: defines the directory of the dbt project and other project configurations.

|YAML key|Value description|
|---|---|
|[name](https://docs.getdbt.com/reference/project-configs/name)|Your project’s name in [snake case](https://en.wikipedia.org/wiki/Snake_case)|
|[version](https://docs.getdbt.com/reference/project-configs/version)|Version of your project|
|[require-dbt-version](https://docs.getdbt.com/reference/project-configs/require-dbt-version)|Restrict your project to only work with a range of [dbt Core versions](https://docs.getdbt.com/docs/dbt-versions/core)|
|[profile](https://docs.getdbt.com/reference/project-configs/profile)|The profile dbt uses to connect to your data platform|
|[model-paths](https://docs.getdbt.com/reference/project-configs/model-paths)|Directories to where your model and source files live|
|[seed-paths](https://docs.getdbt.com/reference/project-configs/seed-paths)|Directories to where your seed files live|
|[test-paths](https://docs.getdbt.com/reference/project-configs/test-paths)|Directories to where your test files live|
|[analysis-paths](https://docs.getdbt.com/reference/project-configs/analysis-paths)|Directories to where your analyses live|
|[macro-paths](https://docs.getdbt.com/reference/project-configs/macro-paths)|Directories to where your macros live|
|[snapshot-paths](https://docs.getdbt.com/reference/project-configs/snapshot-paths)|Directories to where your snapshots live|
|[docs-paths](https://docs.getdbt.com/reference/project-configs/docs-paths)|Directories to where your docs blocks live|
|[vars](https://docs.getdbt.com/docs/build/project-variables)|Project variables you want to use for data compilation|

For complete details on project configurations, see [dbt_project.yml](https://docs.getdbt.com/reference/dbt_project.yml).
> Chú ý sử dụng đúng naming convention: https://docs.getdbt.com/reference/dbt_project.yml#naming-convention

---

### Models config [](https://docs.getdbt.com/reference/configs-and-properties)

**Model configs có thể định nghĩa theo 3 cách:** ^886e82
- `dbt_project.yml`: nơi tổng hợp config của project và từng resource files (top-level)
- `properties.yml`: đặt trong từng resources để apply config cho resource đó (mid-level , ghi đè top-level)
- `config()` block trong từng file `.sql` (low-level, ghi đè mid-level và top-level)

**Một số properties chỉ được cài đặt trong `properties.yml`:**
- [`description`](https://docs.getdbt.com/reference/resource-properties/description)
- [`tests`](https://docs.getdbt.com/reference/resource-properties/data-tests)
- [`docs`](https://docs.getdbt.com/reference/resource-configs/docs)
- [`columns`](https://docs.getdbt.com/reference/resource-properties/columns)
- [`quote`](https://docs.getdbt.com/reference/resource-properties/quote)
- [`source` properties](https://docs.getdbt.com/reference/source-properties) (e.g. `loaded_at_field`, `freshness`)
- [`exposure` properties](https://docs.getdbt.com/reference/exposure-properties) (e.g. `type`, `maturity`)
- [`macro` properties](https://docs.getdbt.com/reference/macro-properties) (e.g. `arguments`)

```models/jaffle_shop.yml
version: 2

sources:
  - name: raw_jaffle_shop
    description: A replica of the postgres database used to power the jaffle_shop app.
    tables:
      - name: customers
        columns:
          - name: id
            description: Primary key of the table
            tests:
              - unique
              - not_null

      - name: orders
        columns:
          - name: id
            description: Primary key of the table
            tests:
              - unique
              - not_null

          - name: user_id
            description: Foreign key to customers

          - name: status
            tests:
              - accepted_values:
                  values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']


models:
  - name: stg_jaffle_shop__customers
    config:
      tags: ['pii']
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    config:
      materialized: view
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: status
        tests:
          - accepted_values:
              values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']
              config:
                severity: warn


```

**How to apply config on resource path**: ([follow the syntax](https://docs.getdbt.com/reference/resource-configs/resource-path))

---

### General properties

#### [columns](https://docs.getdbt.com/reference/resource-properties/columns)
định nghĩa columns properties: data_type, description, quote, tests, tags, meta

```yaml
version: 2

models:
  - name: customers
    description: "Thông tin về khách hàng"
    columns:
      - name: customer_id
        description: "Mã định danh duy nhất của khách hàng"
        data_type: "integer"
        tests:
          - not_null
          - unique
      - name: email
        description: "Địa chỉ email của khách hàng"
        data_type: "string"
        tests:
          - not_null
          - unique
        tags: ["PII"]
        meta:
          sensitivity: "high"

```

models `customers` có hai cột `customer_id` và `email`, mỗi cột được mô tả chi tiết với các thuộc tính như `description`, `data_type`, `tests`, `tags` và `meta`. Việc định nghĩa chi tiết này giúp cải thiện tài liệu hóa và đảm bảo chất lượng dữ liệu trong dự án dbt của bạn.
#### [config](https://docs.getdbt.com/reference/resource-properties/config)

#### constraints

Các **constraints (ràng buộc)** trong dbt không chỉ đơn thuần là validation (kiểm tra dữ liệu) sau khi chạy model, mà chúng thực sự được áp dụng ở cấp độ **cấu trúc bảng** trên database.

> constraints giúp **bảo vệ tính toàn vẹn dữ liệu ngay từ đầu**, trong khi `dbt test` giúp **phát hiện dữ liệu sai nhưng không ngăn chặn**. Nếu database của bạn hỗ trợ constraints, đây là một cách mạnh mẽ để kiểm soát chất lượng dữ liệu trực tiếp trong schema.

Cụ thể:

- Khi bạn **khai báo constraints trong model**, dbt sẽ yêu cầu database **áp dụng ràng buộc** trên bảng (ví dụ: cột không được null, cột phải unique, có khóa chính/khóa ngoại, v.v.).
- Nếu dữ liệu vi phạm constraints này, database **sẽ chặn** việc nhập dữ liệu vào bảng ngay từ đầu.
- Điều này khác với việc chạy **test** trong dbt (ví dụ: `dbt test`), vì test chỉ **kiểm tra sau khi dữ liệu đã được nạp vào**.

#### [deprecation_date](https://docs.getdbt.com/reference/resource-properties/deprecation_date)

#### [description](https://docs.getdbt.com/reference/resource-properties/description)

**`description`** được sử dụng để cung cấp mô tả cho các resources như models, source, seed, snapshot, analyses, macro, test dữ liệu và các cột tương ứng của chúng. Những mô tả này giúp tài liệu hóa dự án và được hiển thị trên trang web tài liệu do dbt tạo ra.

#### [lastest_version](https://docs.getdbt.com/reference/resource-properties/latest_version)

**`latest_version`** được sử dụng để chỉ định phiên bản mới nhất của một mô hình đã được phiên bản hóa. Điều này đặc biệt hữu ích khi bạn có nhiều phiên bản của cùng một mô hình và muốn kiểm soát phiên bản nào sẽ được sử dụng mặc định trong các tham chiếu không chỉ định rõ ràng phiên bản.

```yaml
models:
  - name: ten_mo_hinh
    latest_version: 2
    versions:
      - v: 3
      - v: 2
      - v: 1
```

Trong ví dụ trên, mặc dù có ba phiên bản (`1`, `2`, `3`), nhưng `latest_version` được đặt là `2`. Điều này có nghĩa là bất kỳ tham chiếu nào đến mô hình `ten_mo_hinh` mà không chỉ định phiên bản cụ thể (ví dụ: `ref('ten_mo_hinh')`) sẽ mặc định trỏ đến phiên bản `2`. Phiên bản `3` sẽ được coi là "prerelease" (phiên bản chuẩn bị phát hành), trong khi phiên bản `1` được coi là "old" (cũ).

Nếu không chỉ định `latest_version`, dbt sẽ mặc định coi phiên bản `3` là phiên bản mới nhất. Do đó, `ref('ten_mo_hinh')` sẽ trỏ đến `ten_mo_hinh.v3`

#### [include-exclude columns](https://docs.getdbt.com/reference/resource-properties/include-exclude)

#### [Data tests](https://docs.getdbt.com/reference/resource-properties/data-tests)

**`tests`** property defines assertions about a column, table, or view. 4 kiểm thử tích hợp sẵn trong dbt:

1. **`not_null`**: Xác nhận rằng không có giá trị `null` trong một cột.
2. **`unique`**: Xác nhận rằng không có giá trị trùng lặp trong một cột.
3. **`accepted_values`**: Xác nhận rằng tất cả các giá trị trong một cột đều nằm trong một danh sách giá trị được cung cấp.
4. **`relationships`**: Xác nhận rằng tất cả các bản ghi trong bảng con có một bản ghi tương ứng trong bảng cha (tính toàn vẹn tham chiếu).

Ngoài ra còn có các custom tests. 

#### [versions](https://docs.getdbt.com/reference/resource-properties/versions)

**`versions`** cho phép bạn quản lý và theo dõi các phiên bản khác nhau của một mô hình theo thời gian. Điều này đặc biệt hữu ích khi bạn cần thực hiện các thay đổi quan trọng đối với mô hình mà không muốn ảnh hưởng đến các quy trình hoặc người dùng hiện tại đang dựa vào phiên bản cũ.

```models/<schema>.yml
version: 2

models:
  - name: model_name
    versions:
      - v: <version_identifier> # required
        defined_in: <file_name> # optional -- default is <model_name>_v<v>
        columns:
          # specify all columns, or include/exclude columns from the top-level model YAML definition
          - [include](/reference/resource-properties/include-exclude): <include_value>
            [exclude](/reference/resource-properties/include-exclude): <exclude_list>
          # specify additional columns
          - name: <column_name> # required
      - v: ...
    
    # optional
    [latest_version](/reference/resource-properties/latest_version): <version_identifier> 
```

---

### General configs

| Cấu hình         | Mục đích                                                                                         |
|-----------------|--------------------------------------------------------------------------------------------------|
| [`docs`](https://docs.getdbt.com/reference/resource-configs/docs)               | Điều khiển việc hiển thị tài nguyên trong tài liệu tự động của dbt và đặt màu cho các nút. |
| [`access`](https://docs.getdbt.com/reference/resource-configs/access)           | Xác định mức độ truy cập của mô hình (`private`, `protected`, `public`) để kiểm soát phạm vi tham chiếu. |
| [`alias`](https://docs.getdbt.com/reference/resource-configs/alias)             | Đặt tên thay thế cho bảng hoặc view được tạo trong cơ sở dữ liệu. |
| [`contract`](https://docs.getdbt.com/reference/resource-configs/contract)       | Xác định hợp đồng cho mô hình, bao gồm các ràng buộc về schema và dữ liệu. |
| [`database`](https://docs.getdbt.com/reference/resource-configs/database)       | Chỉ định cơ sở dữ liệu nơi tài nguyên sẽ được tạo. |
| [`enabled`](https://docs.getdbt.com/reference/resource-configs/enabled)         | Bật hoặc tắt tài nguyên trong quá trình chạy dbt. |
| [`event_time`](https://docs.getdbt.com/reference/resource-configs/event_time)   | Đánh dấu một cột là cột thời gian sự kiện, hữu ích cho các thao tác liên quan đến thời gian. |
| [`full_refresh`](https://docs.getdbt.com/reference/resource-configs/full_refresh) | Buộc làm mới hoàn toàn cho các mô hình gia tăng trong lần chạy tiếp theo. |
| [`grants`](https://docs.getdbt.com/reference/resource-configs/grants)           | Áp dụng quyền truy cập cho các đối tượng cơ sở dữ liệu được tạo bởi dbt. |
| [`group`](https://docs.getdbt.com/reference/resource-configs/group)             | Gán mô hình vào một nhóm để quản lý và tổ chức. |
| [`meta`](https://docs.getdbt.com/reference/resource-configs/meta)               | Lưu trữ thông tin bổ sung tùy chỉnh cho tài nguyên. |
| [`persist_docs`](https://docs.getdbt.com/reference/resource-configs/persist_docs) | Lưu trữ mô tả tài nguyên dưới dạng nhận xét trong cơ sở dữ liệu. |
| [`pre-hook & post-hook`](https://docs.getdbt.com/reference/resource-configs/pre-hook-post-hook) | Thực thi các lệnh SQL hoặc macro trước và sau khi chạy một mô hình. |
| [`schema`](https://docs.getdbt.com/reference/resource-configs/schema)           | Chỉ định schema nơi tài nguyên sẽ được tạo. |
| [`tags`](https://docs.getdbt.com/reference/resource-configs/tags)               | Gắn thẻ cho tài nguyên để phân loại và lựa chọn trong các thao tác dbt. |
| [`unique_key`](https://docs.getdbt.com/reference/resource-configs/unique_key)   | Xác định khóa duy nhất cho các mô hình gia tăng. |

---

## Resources

### Models

- Models are the basic building block of your business logic
- Materialized as tables, views, etc...
- They live in SQL files in the `models` folder
- Models can reference each other and use templates and macros

**Materializations types**

| **Category**              | **View**                                                                                                               | **Table**                                                                                     | **Incremental**                                                                    | **Ephemeral (CTEs)**                                                              | **Materialized View**                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Pros**                 | - No additional data is stored. <br> - Always has the latest records from source data.                               | - Fast to query.                                                                             | - Significantly reduces build time by only transforming new records.             | - Allows reusable logic. <br> - Keeps the data warehouse clean by reducing table clutter. | - Combines query performance of a table with data freshness of a view. <br> - Can refresh automatically depending on the database. <br> - `dbt run` works like with views. |
| **Cons**                 | - Slow for significant transformations or when stacked on top of other views.                                        | - Takes time to rebuild, especially for complex transformations. <br> - New records are not automatically added. | - Requires additional configuration and is more complex than other models.       | - Cannot be directly queried. <br> - Cannot be referenced (`ref()`) in `dbt run-operation`. <br> - Overuse can make queries harder to debug. | - Fewer configuration options depending on the database platform. <br> - Not all databases support materialized views. |
| **Advice**               | - Start with views before switching to another materialization. <br> - Best for models that do not perform heavy transformations. | - Use for models queried by BI tools for better user experience. <br> - Suitable for slow transformations used by many downstream models. | - Best for event-style data. <br> - Use when dbt runs become too slow (do not start with incremental models). | - Use for lightweight transformations early in the DAG. <br> - Best for models used in only one or two downstream models. | - Use when incremental models are sufficient, but you want the data platform to manage incremental logic and refresh. |
| **Use it when...**       | - You want a lightweight representation. <br> - You don’t reuse data too often.                                      | - You read from this model repeatedly.                                                       | - Fact tables. <br> - Appends to tables.                                         | - You merely want an alias to your data.                                          | - Similar use cases as incremental models but want the database to manage refresh. |
| **Don't use it when...** | - You read from the same model several times.                                                                       | - Building single-use models. <br> - Your model is populated incrementally.                   | - You want to update historical records.                                         | - You read from the same model several times.                                    | - The database platform doesn’t support materialized views. |

**Có thể config materializations trong 3 cách theo như** [[#^886e82]]

Ví dụ trong `dbt_project.yml`

```dbt_project.yml
models:
  dbtlearn:
    +materialized: view
    dim:
      +materialized: table
```
hoặc trong config block
#### Table/View Models

```sql
{{
  config(
    materialized = 'view'
    )
}}

WITH src_hosts AS (
    SELECT
        *
    FROM
        {{ ref('src_hosts') }}
)
SELECT
    host_id,
    NVL(
        host_name,
        'Anonymous'
    ) AS host_name,
    is_superhost,
    created_at,
    updated_at
FROM
    src_hosts
```

#### Incremental Models

The `fct/fct_reviews.sql` model:
```sql
{{
  config(
    materialized = 'incremental',
    on_schema_change='fail'
    )
}}
WITH src_reviews AS (
  SELECT * FROM {{ ref('src_reviews') }}
)
SELECT * FROM src_reviews
WHERE review_text is not null

{% if is_incremental() %}
  AND review_date > (select max(review_date) from {{ this }})
{% endif %}
```

#### Ephemeral view

`+materialized: ephemeral`

Mỗi 1 model dạng ephemeral sẽ được lưu thành query tạm (mà không tạo thành đối tượng trên database: table, view...)

---
### Seeds

**Seeds** là local files dùng để upload trực triếp lên data warehouse from DBT, được lưu trữ trong folder `/seeds/`

- Các command run model project không tải lại các file seed lên warehouse, ta cần chạy lệnh `dbt seed` hoặc `dbt build` để load các folder lên data warehouse

How to write [Seed properties](https://docs.getdbt.com/reference/seed-properties)

```yml
#seeds/<filename>.yml
version: 2

seeds:
  - name: <string>
    description: <markdown_string>
    docs:
      show: true | false
      node_color: <color_id>
    config:
      <seed_config>: <config_value>
    tests:
      - <test>
      - ... # declare additional tests
    columns:
      - name: <column name>
        description: <markdown_string>
        meta: {<dictionary>}
        quote: true | false
        tags: [<string>]
        tests:
          - <test>
          - ... # declare additional tests

      - name: ... # declare properties of additional columns

  - name: ... # declare properties of additional seeds
```

---

### Sources 

**Sources** là những data layer trừu tượng đại diện cho input data (data từ các nguồn database, schema khác) mà không bị thay đổi trong quá trình build và run DBT, tuy nhiên vì nó là data ở dạng database nên giá trị sẽ có tính chất freshness (thay vì cố định như **seeds local files**)

Định nghĩa **Sources** in `model/`,  check các [properties](https://docs.getdbt.com/reference/source-properties) and [config](https://docs.getdbt.com/reference/source-configs)

```yml
# models/sources.yml
version: 2

sources:
  - name: airbnb # Source name
    schema: raw  # Schema name
    tables:
      - name: listings # reference to the table name
        identifier: raw_listings # Table name of data source

      - name: hosts
        identifier: raw_hosts

      - name: reviews
        identifier: raw_reviews
        loaded_at_field: date # check mức độ freshness của trường 'date' với hiện tại, nếu date quá cũ sau hiện tại thì sẽ warning hoặc error
        freshness:
          warn_after: {count: 1, period: hour}
          error_after: {count: 24, period: hour}
          filter: datediff('day', date, current_timestamp) < 2 # optional
```

**`filter`** sẽ thực hiện query filder bảng trước khi chạy assertions để tránh TH query cả bảng, nhằm tối ưu chi phí và performance.

---
### Snapshots

**Strategy Snapshot** được sử dụng để ghi lại sự thay đổi của dữ liệu theo thời gian bằng cách tạo bảng snapshot. Điều này rất hữu ích cho việc theo dõi các thay đổi trong dữ liệu quan trọng, chẳng hạn như thông tin khách hàng, trạng thái đơn hàng hoặc bất kỳ dữ liệu nào có thể thay đổi theo thời gian.

>**Snapshot** sẽ tạo ra các bảng có cấu trúc gần giống như các bảng được snapshot, bổ sung thêm các trường `snapshot_id`, `dbt_valid_from`, `dbt_valid_to`. Khi bảng gốc được thay đổi và chạy command `dbt snapshot` sẽ update lại row bị thay đổi trong bảng gốc trong bảng snapshot tương ứng.

**Có 2 strategies cho việc snapshot:**

*Timestamp Strategy (Chiến lược dựa trên dấu thời gian)*

- Cơ chế hoạt động: So sánh unique_key `customer_id` + một cột dấu thời gian (`updated_at`, `modified_date`, v.v.) để xác định khi nào bản ghi đã thay đổi.
- Nếu giá trị trong cột này thay đổi, DBT sẽ tạo một bản ghi snapshot mới.
- **Phù hợp với:** Các bảng có một cột timestamp đại diện cho lần cập nhật gần nhất.
    ```sql
  snapshot customer_snapshot {   
	target_database: my_database   
	target_schema: snapshots   
	unique_key: customer_id    
	strategy: timestamp   
	updated_at: updated_at 
	}
	```
    
- Ưu điểm:
    - Hiệu suất cao vì chỉ cần kiểm tra một cột timestamp.
    - Dễ triển khai nếu dữ liệu có cột timestamp đáng tin cậy.
- Nhược điểm:
    - Không thể theo dõi các thay đổi nếu dữ liệu không có cột `updated_at`.
    - Nếu timestamp không được cập nhật đúng cách, có thể bỏ lỡ thay đổi.
    

*Check Strategy (Chiến lược kiểm tra toàn bộ hàng)*

- Cơ chế hoạt động: So sánh toàn bộ giá trị của một hoặc nhiều cột để phát hiện thay đổi.
- Nếu bất kỳ giá trị nào trong danh sách cột được kiểm tra thay đổi, DBT sẽ tạo một snapshot mới.
- **Phù hợp với:** Các bảng không có cột `updated_at` hoặc khi bạn muốn theo dõi sự thay đổi của một tập hợp cột cụ thể.
```sql
snapshot order_snapshot {
  target_database: my_database
  target_schema: snapshots
  unique_key: order_id
  strategy: check
  check_cols: ['status', 'total_price', 'customer_id']
}
```
- Ưu điểm:
    - Linh hoạt hơn vì không phụ thuộc vào cột timestamp.
    - Có thể theo dõi nhiều thay đổi cùng lúc.
- Nhược điểm:
    - Tốn tài nguyên hơn vì phải so sánh toàn bộ dữ liệu trong các cột chỉ định.
    - Cần chọn các cột kiểm tra phù hợp, nếu không có thể tạo quá nhiều snapshot không cần thiết.

**So sánh Timestamp vs Check Strategy**

|Tiêu chí|Timestamp Strategy|Check Strategy|
|---|---|---|
|Cơ chế|Dựa vào cột timestamp|So sánh nhiều cột chỉ định|
|Hiệu suất|Cao hơn do chỉ kiểm tra một cột|Chậm hơn nếu nhiều cột được kiểm tra|
|Dễ triển khai|Dễ nếu có cột timestamp|Phức tạp hơn|
|Độ chính xác|Phụ thuộc vào độ tin cậy của timestamp|Chính xác hơn nếu chọn đúng cột|
**Khi nào nên sử dụng từng loại?**

- **Dùng `timestamp strategy`** nếu bảng dữ liệu có cột `updated_at` hoặc dấu thời gian đáng tin cậy.
- **Dùng `check strategy`** nếu cần theo dõi sự thay đổi của nhiều cột hoặc không có cột timestamp.

**Cấu trúc file snapshot**

```sql
-- `snapshots/scd_raw_listings.sql`

-- snapshot begining block
{% snapshot scd_raw_listings %}

-- define how to snapshot by snapshots config
{{
   config(
       target_schema='DEV',
       unique_key='id',
       strategy='timestamp',
       updated_at='updated_at',
       hard_delete="invalidate" 
   )
}}

-- define what is snapshoted ?
select * FROM {{ source('airbnb', 'listings') }}

-- snapshot ending block
{% endsnapshot %}
```

#### [snapshot properties](https://docs.getdbt.com/reference/snapshot-properties)

- `hard_deletes`: action cho record trong bảng snapshot khi record đó bị delete khỏi bảng nguồn

---
### Tests

**tests** là các kiểm thử dữ liệu giúp đảm bảo tính toàn vẹn và chính xác của dữ liệu trong mô hình. Khi chạy lệnh `dbt test`, dbt sẽ thực thi các kiểm thử đã định nghĩa để xác nhận rằng dữ liệu đáp ứng các quy tắc và ràng buộc đã đặt ra.

dbt hỗ trợ hai loại kiểm thử chính là **Generic Tests** và **Singular Tests**

🔹 **Chạy test:**
- `dbt test` : chạy toàn bộ các tests
- `dbt test --select customers`: chỉ chạy test cho một mô hình cụ thể (`customer`)

🔹 **Kết quả:**
- Nếu test thành công: Hiển thị ✅ PASSED.
- Nếu test thất bại: Hiển thị ❌ FAILED với số dòng không đạt yêu cầu.
#### Generic Tests (Kiểm thử chung)

- Là các kiểm thử có thể áp dụng cho nhiều mô hình hoặc cột khác nhau.
- Được tích hợp sẵn trong dbt hoặc từ các **package mở rộng** như `dbt_utils`.

| **Test Name**     | **Mô tả**                                                    |
| ----------------- | ------------------------------------------------------------ |
| `unique`          | Đảm bảo cột có giá trị duy nhất (không trùng lặp).           |
| `not_null`        | Đảm bảo cột không chứa giá trị NULL.                         |
| `accepted_values` | Đảm bảo giá trị của cột nằm trong danh sách cho phép.        |
| `relationships`   | Đảm bảo giá trị của cột nằm trong danh sách giá trị cột khác |
| macro function    | Sử dụng các macro custom function để test                    |


**Cách sử dụng:**  Generic tests được khai báo trực tiếp trong tệp **models/schema.yml**.
```yaml
# models/schema.yml
version: 2

models:
  - name: dim_listings_cleansed
    description: Cleansed table which contains Airbnb listings.
    columns:

      - name: listing_id
        description: Primary key for the listing
        tests:
          - unique
          - not_null

      - name: host_id
        description: The hosts's id. References the host table.
        tests:
          - not_null
          - relationships:
              to: ref('dim_hosts_cleansed') 
              field: host_id # reference field 'host_id' in `dim_hosts_cleansed`

      - name: room_type
        description: Type of the apartment / room
        tests:
          - accepted_values:
              values: ['Entire home/apt',
                      'Private room',
                      'Shared room',
                      'Hotel room']

      - name: minimum_nights
        description: '{{ doc("dim_listing_cleansed__minimum_nights") }}'
        tests:
          - positive_value # use macro function

  - name: dim_hosts_cleansed
    description: Cleansed table for the Airbnb hosts
    columns:
      - name: host_id
        description: The id of the host. This is the primary key.
        tests:
          - not_null
          - unique
      
      - name: host_name
        description: The name of the host
        tests:
          - not_null
      
      - name: is_superhost
        description: Defines whether the hosts is a superhost.
        tests:
          - accepted_values:
              values: ['t', 'f']

  - name: dim_listings_w_hosts
    tests:
      - dbt_expectations.expect_table_row_count_to_equal_other_table: # use package "dbt_expectations"
          compare_model: source('airbnb', 'listings')
    columns:
      - name: price
        tests:
          - dbt_expectations.expect_column_values_to_be_of_type:
              column_type: number
          - dbt_expectations.expect_column_quantile_values_to_be_between:
              quantile: .99
              min_value: 50
              max_value: 500
          - dbt_expectations.expect_column_max_to_be_between:
              max_value: 5000
              config:
                severity: warn

  - name: fct_reviews
    columns:
      - name: listing_id
        tests:
          - relationships:
              to: ref('dim_listings_cleansed')
              field: listing_id

      - name: reviewer_name
        tests:
          - not_null
      
      - name: review_sentiment
        tests:
          - accepted_values:
              values: ['positive', 'neutral', 'negative']
```
💡 **Khi chạy `dbt test`**, dbt sẽ tự động tạo và chạy các truy vấn SQL để kiểm tra điều kiện trên.
#### Singular Tests (Kiểm thử tùy chỉnh)

- Là các kiểm thử được viết dưới dạng truy vấn SQL.
- Kiểm thử này có thể kiểm tra các quy tắc phức tạp, chẳng hạn như điều kiện logic hoặc dữ liệu bất thường.
- Được khai báo trong thư mục `tests/` dưới dạng file SQL.

**Cách sử dụng:**  Tạo tệp `tests/high_value_orders.sql`:
```yaml
# tests/high_value_orders.sql
SELECT *
FROM {{ ref('orders') }}
WHERE total_amount > 1000000  -- Kiểm tra đơn hàng quá lớn
```
💡 **Nếu truy vấn trả về bất kỳ dòng nào, test sẽ thất bại**.

#### Mở rộng tests với dbt-utils

Dbt hỗ trợ thêm các kiểm thử nâng cao từ **package `dbt-utils`**, giúp kiểm thử linh hoạt hơn.

Trong file `packages.yml`:
```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.3.0 # version
```

**Ví dụ: Kiểm tra trường `email` có đúng định dạng không?**

```yaml
models:
  - name: customers
    columns:
      - name: email
        tests:
          - dbt_utils.expression_is_true:
              expression: "email LIKE '%@%.%'"

```
🔹 *Nếu có email không đúng định dạng, test sẽ thất bại.*

### Macros

### Packages

### Documentation

### Analyses

### Hooks

### Exposures

### Variables

## [DBT Command](https://docs.getdbt.com/reference/commands/build)

| Command                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [init](https://docs.getdbt.com/reference/commands/init)                   | Initializes a new dbt project<br><br>*Khởi tạo một dự án dbt mới trong thư mục hiện tại, tạo ra cấu trúc thư mục và các tệp cấu hình cần thiết.*<br><br>Khi muốn **tạo một dự án dbt mới**.<br>`dbt init my_project`:<br>✔️ Dự án mới được tạo.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [debug](https://docs.getdbt.com/reference/commands/debug)                 | Debugs dbt connections and projects<br><br>*Kiểm tra kết nối và cấu hình của dbt để đảm bảo rằng mọi thứ được thiết lập đúng cách.*<br><br>✔️ Kiểm tra và báo lỗi kết nối nếu có.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [build](https://docs.getdbt.com/reference/commands/build)                 | Builds and tests all selected resources (models, seeds, snapshots, tests), this will do: run models, test tests, snapshot snapshots, seed seeds<br><br>*run model, test, snapshot và seed theo DAG order. Lệnh này giúp xây dựng toàn bộ dự án dbt một cách toàn diện.*<br><br>- Khi muốn chạy **toàn bộ pipeline dữ liệu** bao gồm: mô hình, kiểm thử, snapshot và seed theo đúng thứ tự phụ thuộc.<br>- Hữu ích trong **quá trình vận hành**, đảm bảo dữ liệu được xử lý đúng và kiểm thử dữ liệu tự động.<br><br>Kết quả:  <br>✔️ Mô hình mới được chạy trên database.  <br>✔️ Kiểm thử dữ liệu chạy để đảm bảo tính đúng đắn.  <br>✔️ Snapshot được cập nhật (nếu có). |
| [run](https://docs.getdbt.com/reference/commands/run)                     | Runs the models in a project follow DAG order<br><br>*run models SQL đã được biên dịch trong dự án dbt trên cơ sở dữ liệu mục tiêu. Lệnh này tạo ra các bảng hoặc view dựa trên các mô hình đã định nghĩa.*<br><br>- Khi bạn chỉ muốn **chạy mô hình SQL** mà không cần chạy tests, seed, snapshot.<br>- Hữu ích trong **quá trình phát triển**, để kiểm tra mô hình có chạy đúng không.<br><br>`dbt run --select sales_report` : <br>✔️ Chạy mô hình `sales_report` trên database.                                                                                                                                                                                        |
| [test](https://docs.getdbt.com/reference/commands/test)                   | Executes tests defined (models, sources, snapshots, seeds) in a project<br><br>*Chạy các kiểm thử dữ liệu được định nghĩa trên các mô hình, nguồn dữ liệu, snapshot và seed. Lệnh này giúp xác minh tính toàn vẹn và chất lượng của dữ liệu.*<br><br>- Khi muốn kiểm tra **tính đúng đắn của dữ liệu** (ví dụ: không có giá trị NULL, giá trị duy nhất, quan hệ khóa ngoại đúng).<br>- Hữu ích trong **quá trình vận hành**, giúp phát hiện lỗi dữ liệu kịp thời.<br><br>`dbt test`:<br>✔️ Hiển thị lỗi nếu có dữ liệu không hợp lệ.                                                                                                                                       |
| [seed](https://docs.getdbt.com/reference/commands/seed)                   | Loads CSV files into the database<br><br>*Tải các tệp CSV vào cơ sở dữ liệu. Điều này hữu ích cho việc nhập dữ liệu tĩnh hoặc ít thay đổi, chẳng hạn như bảng mã quốc gia hoặc bảng tra cứu.*<br><br>- Khi muốn **nạp dữ liệu tĩnh** vào database từ file CSV (ví dụ: danh sách quốc gia, danh mục sản phẩm).<br>- Hữu ích khi khởi tạo dự án hoặc chạy thử nghiệm.<br><br>`dbt seed`:<br>✔️ Dữ liệu từ `country_list.csv` trong folder `seed/` được tải lên database.                                                                                                                                                                                                     |
| [snapshot](https://docs.getdbt.com/reference/commands/snapshot)           | Executes "snapshot" jobs defined in a project<br><br>*Thực thi các công việc "snapshot" được định nghĩa trong dự án, cho phép theo dõi lịch sử thay đổi của dữ liệu theo thời gian.*<br><br>- Khi cần **lưu lại lịch sử thay đổi dữ liệu**, giúp phân tích dữ liệu theo thời gian.<br>- Hữu ích với dữ liệu có sự thay đổi theo thời gian như: **giá sản phẩm, trạng thái đơn hàng**.<br><br>`dbt snapshot`:<br>✔️ Lưu trạng thái hiện tại của khách hàng vào bảng snapshot.                                                                                                                                                                                               |
| [docs](https://docs.getdbt.com/reference/commands/cmd-docs)               | Generates documentation for a project<br><br>*Tạo và phục vụ tài liệu cho dự án dbt. Lệnh này có hai lệnh con:*<br>- `dbt docs generate`: *Tạo trang web tài liệu cho dự án bằng cách biên dịch các tài nguyên và thu thập metadata từ cơ sở dữ liệu.*<br>- `dbt docs serve`: *Khởi động máy chủ web để phục vụ tài liệu và mở trang web tài liệu trong trình duyệt mặc định.*<br><br>- Khi muốn **tạo tài liệu tự động** cho mô hình dữ liệu.<br>- Hữu ích trong **quản lý dữ liệu**, giúp team dễ dàng tra cứu thông tin.<br><br>`dbt docs serve`:<br>✔️ Website tài liệu hiển thị metadata và lineage của các mô hình.<br>                                              |
| [run-operation](https://docs.getdbt.com/reference/commands/run-operation) | Invokes a macro, including running arbitrary maintenance SQL against the database<br><br>*Gọi một macro, bao gồm việc chạy các lệnh SQL bảo trì tùy ý trên cơ sở dữ liệu.*<br><br>Khi muốn **chạy macro tùy chỉnh** (ví dụ: xóa cache, cập nhật metadata).<br><br>`dbt run-operation drop_old_tables`<br>✔️ Macro `drop_old_tables` chạy, xóa bảng cũ.                                                                                                                                                                                                                                                                                                                     |
| [clean](https://docs.getdbt.com/reference/commands/clean)                 | Deletes artifacts present (folder: `\targer`) in the dbt project<br><br>Khi muốn **dọn dẹp** thư mục `target/` và `dbt_packages/`, tránh lỗi do dữ liệu cũ.<br><br>`dbt clean`:<br>✔️ Thư mục cũ bị xóa, đảm bảo môi trường sạch.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [clone](https://docs.getdbt.com/reference/commands/clone)                 | Clones selected models from the specified state<br><br>*Sao chép các mô hình được chọn từ trạng thái được chỉ định.*<br><br>Khi muốn **sao chép trạng thái mô hình** từ một môi trường khác.<br>`dbt clone --state prod`<br>✔️ Sao chép dữ liệu từ môi trường `prod`.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [compile](https://docs.getdbt.com/reference/commands/compile)             | Compiles (but does not run) the models in a project<br><br>*Biên dịch các mô hình trong dự án mà không thực thi chúng, tạo ra các tệp SQL đã biên dịch trong thư mục `target`.*<br><br>Khi muốn **xem SQL đã biên dịch** của mô hình mà không chạy nó.<br><br>`dbt compile --select sales_report`:<br>✔️ File SQL được tạo trong `target/compiled/`.                                                                                                                                                                                                                                                                                                                       |
| [deps](https://docs.getdbt.com/reference/commands/deps)                   | Downloads dependencies for a project<br><br>*Tải về các phụ thuộc cho dự án dbt, chẳng hạn như các gói dbt được chỉ định trong tệp `packages.yml`.*<br><br>Khi cần **tải về package dbt** từ `packages.yml` (ví dụ: `dbt_utils`).<br><br>`dbt deps`:<br>✔️ Các package được tải về thư mục `dbt_packages/`.                                                                                                                                                                                                                                                                                                                                                                |
| [invocation](https://docs.getdbt.com/reference/commands/invocation)       | Enables users to debug long-running sessions by interacting with active invocations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [list](https://docs.getdbt.com/reference/commands/list)                   | Lists resources defined in a dbt project<br><br>*Liệt kê các tài nguyên được định nghĩa trong dự án dbt. Lệnh này chấp nhận các đối số lựa chọn tương tự như `dbt run`.*<br><br>Khi muốn **liệt kê các mô hình trong dự án**.<br><br>`dbt ls --resource-type model`:<br>✔️ Liệt kê tất cả các mô hình.                                                                                                                                                                                                                                                                                                                                                                     |
| [parse](https://docs.getdbt.com/reference/commands/parse)                 | Parses a project and writes detailed timing info                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [retry](https://docs.getdbt.com/reference/commands/retry)                 | Retry the last run `dbt` command from the point of failure<br><br>*Thử lại lệnh dbt cuối cùng từ điểm thất bại.*<br>`dbt retry`:<br>✔️ Tiếp tục từ chỗ lỗi trước đó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [show](https://docs.getdbt.com/reference/commands/show)                   | Previews table rows post-transformation<br><br>*Biên dịch định nghĩa dbt-SQL của một mô hình, kiểm thử, phân tích hoặc một truy vấn dbt-SQL tùy ý được truyền vào bằng `--inline`, sau đó chạy truy vấn đó trên kho dữ liệu và xem trước kết quả trong terminal.*<br><br>Khi muốn **xem trước dữ liệu của một mô hình**.<br><br>`dbt show --select sales_report`:<br>✔️ Hiển thị kết quả SQL của `sales_report`.<br>                                                                                                                                                                                                                                                       |
| [source](https://docs.getdbt.com/reference/commands/source)               | Provides tools for working with source data (including validating that sources are "fresh")<br><br>*Cung cấp các lệnh con hữu ích khi làm việc với dữ liệu nguồn. Lệnh này có một lệnh con là `dbt source freshness`, dùng để kiểm tra độ mới của các bảng nguồn.*<br><br>Khi muốn **kiểm tra độ mới của dữ liệu nguồn**.<br><br>`dbt source freshness`:<br>✔️ Cảnh báo nếu dữ liệu quá cũ.                                                                                                                                                                                                                                                                                |



## Test & debug DBT

## Deployment

## Orchestration



The contents of `models/schema.yml`:

```sql
version: 2

models:
  - name: dim_listings_cleansed
    columns:

     - name: listing_id
       tests:
         - unique
         - not_null

     - name: host_id
       tests:
         - not_null
         - relationships:
             to: ref('dim_hosts_cleansed')
             field: host_id

     - name: room_type
       tests:
         - accepted_values:
             values: ['Entire home/apt',
                      'Private room',
                      'Shared room',
                      'Hotel room']
```

##### Generic test for minimum nights check
The contents of `tests/dim_listings_minumum_nights.sql`:

```sql
SELECT
    *
FROM
    {{ ref('dim_listings_cleansed') }}
WHERE minimum_nights < 1
LIMIT 10

```

##### Restricting test execution to a model
```sh
dbt test --select dim_listings_cleansed
```

#### Exercise

Create a singular test in `tests/consistent_created_at.sql` that checks that there is no review date that is submitted before its listing was created: Make sure that every `review_date` in `fct_reviews` is more recent than the associated `created_at` in `dim_listings_cleansed`.


##### Solution
```sql
SELECT * FROM {{ ref('dim_listings_cleansed') }} l
INNER JOIN {{ ref('fct_reviews') }} r
USING (listing_id)
WHERE l.created_at >= r.review_date
```
### Marcos, Custom Tests and Packages 
#### Macros

The contents of `macros/no_nulls_in_columns.sql`:
```sql
{% macro no_nulls_in_columns(model) %}
    SELECT * FROM {{ model }} WHERE
    {% for col in adapter.get_columns_in_relation(model) -%}
        {{ col.column }} IS NULL OR
    {% endfor %}
    FALSE
{% endmacro %}
```

The contents of `tests/no_nulls_in_dim_listings.sql`
```sql
{{ no_nulls_in_columns(ref('dim_listings_cleansed')) }}
```

#### Custom Generic Tests
The contents of `macros/positive_value.sql`
```sql
{% test positive_value(model, column_name) %}
SELECT
    *
FROM
    {{ model }}
WHERE
    {{ column_name}} < 1
{% endtest %}
```

#### Packages
The contents of `packages.yml`:
```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.3.0
```

The contents of ```models/fct_reviews.sql```:
```
{{
  config(
    materialized = 'incremental',
    on_schema_change='fail'
    )
}}
WITH src_reviews AS (
  SELECT * FROM {{ ref('src_reviews') }}
)
SELECT 
  {{ dbt_utils.generate_surrogate_key(['listing_id', 'review_date', 'reviewer_name', 'review_text']) }}
    AS review_id,
  * 
  FROM src_reviews
WHERE review_text is not null
{% if is_incremental() %}
  AND review_date > (select max(review_date) from {{ this }})
{% endif %}
```

#### Documentation

The `models/schema.yml` after adding the documentation:
```yaml
version: 2

models:
  - name: dim_listings_cleansed
    description: Cleansed table which contains Airbnb listings.
    columns:
      
      - name: listing_id
        description: Primary key for the listing
        tests:
          - unique
          - not_null
        
      - name: host_id
        description: The hosts's id. References the host table.
        tests:
          - not_null
          - relationships:
              to: ref('dim_hosts_cleansed')
              field: host_id

      - name: room_type
        description: Type of the apartment / room
        tests:
          - accepted_values:
              values: ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']

      - name: minimum_nights
        description: '{{ doc("dim_listing_cleansed__minimum_nights") }}'
        tests:
          - positive_value

  - name: dim_hosts_cleansed
    columns:
      - name: host_id
        tests:
          - not_null
          - unique
      
      - name: host_name
        tests:
          - not_null
      
      - name: is_superhost
        tests:
          - accepted_values:
              values: ['t', 'f']
  
  - name: fct_reviews
    columns:
      - name: listing_id
        tests:
          - relationships:
              to: ref('dim_listings_cleansed')
              field: listing_id

      - name: reviewer_name
        tests:
          - not_null
      
      - name: review_sentiment
        tests:
          - accepted_values:
              values: ['positive', 'neutral', 'negative']

```
The contents of `models/docs.md`:
```txt
{% docs dim_listing_cleansed__minimum_nights %}
Minimum number of nights required to rent this property. 

Keep in mind that old listings might have `minimum_nights` set 
to 0 in the source tables. Our cleansing algorithm updates this to `1`.

{% enddocs %}
```

The contents of `models/overview.md`:
```md
{% docs __overview__ %}
# Airbnb pipeline

Hey, welcome to our Airbnb pipeline documentation!

Here is the schema of our input data:
![input schema](https://dbtlearn.s3.us-east-2.amazonaws.com/input_schema.png)

{% enddocs %}
```

### Analyses, Hooks and Exposures

#### Create the REPORTER role and PRESET user in Snowflake
```sql
USE ROLE ACCOUNTADMIN;
CREATE ROLE IF NOT EXISTS REPORTER;
CREATE USER IF NOT EXISTS PRESET
 PASSWORD='presetPassword123'
 LOGIN_NAME='preset'
 MUST_CHANGE_PASSWORD=FALSE
 DEFAULT_WAREHOUSE='COMPUTE_WH'
 DEFAULT_ROLE=REPORTER
 DEFAULT_NAMESPACE='AIRBNB.DEV'
 COMMENT='Preset user for creating reports';

GRANT ROLE REPORTER TO USER PRESET;
GRANT ROLE REPORTER TO ROLE ACCOUNTADMIN;
GRANT ALL ON WAREHOUSE COMPUTE_WH TO ROLE REPORTER;
GRANT USAGE ON DATABASE AIRBNB TO ROLE REPORTER;
GRANT USAGE ON SCHEMA AIRBNB.DEV TO ROLE REPORTER;

-- We don't want to grant select rights here; we'll do this through hooks:
-- GRANT SELECT ON ALL TABLES IN SCHEMA AIRBNB.DEV TO ROLE REPORTER;
-- GRANT SELECT ON ALL VIEWS IN SCHEMA AIRBNB.DEV TO ROLE REPORTER;
-- GRANT SELECT ON FUTURE TABLES IN SCHEMA AIRBNB.DEV TO ROLE REPORTER;
-- GRANT SELECT ON FUTURE VIEWS IN SCHEMA AIRBNB.DEV TO ROLE REPORTER;

```

#### Analyses
The contents of `analyses/full_moon_no_sleep.sql`:
```sql
WITH fullmoon_reviews AS (
    SELECT * FROM {{ ref('fullmoon_reviews') }}
)
SELECT
    is_full_moon,
    review_sentiment,
    COUNT(*) as reviews
FROM
    fullmoon_reviews
GROUP BY
    is_full_moon,
    review_sentiment
ORDER BY
    is_full_moon,
    review_sentiment
```
#### Creating a Dashboard in Preset

Getting the Snowflake credentials up to the screen:

* Mac / Linux / Windows Powershell: `cat ~/.dbt/profiles.yml `
* Windows (cmd): `type %USERPROFILE%\.dbt\profiles.yml`

#### Exposures
The contents of `models/dashboard.yml`:
```yaml
version: 2

exposures:
  - name: executive_dashboard
    label: Executive Dashboard
    type: dashboard
    maturity: low
    url: https://00d200da.us1a.app.preset.io/superset/dashboard/x/?edit=true&native_filters_key=fnn_HJZ0z42ZJtoX06x7gRbd9oBFgFLbnPlCW2o_aiBeZJi3bZuyfQuXE96xfgB
    description: Executive Dashboard about Airbnb listings and hosts
      

    depends_on:
      - ref('dim_listings_w_hosts')
      - ref('mart_fullmoon_reviews')

    owner:
      name: Zoltan C. Toth
      email: dbtstudent@gmail.com
```

#### Post-hook
Add this to your `dbt_project.yml`:

```
+post-hook:
      - "GRANT SELECT ON {{ this }} TO ROLE REPORTER"
```

### Debugging Tests and Testing with dbt-expectations

* The original Great Expectations project on GitHub: https://github.com/great-expectations/great_expectations
* dbt-expectations: https://github.com/calogica/dbt-expectations 

For the final code in _packages.yml_, _models/schema.yml_ and _models/sources.yml_, please refer to the course's Github repo:
https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero

#### Testing a single model

```
dbt test --select dim_listings_w_hosts
```

Testing individual sources:

```
dbt test --select source:airbnb.listings
```

#### Debugging dbt

```
dbt --debug test --select dim_listings_w_hosts
```

Keep in mind that in the lecture we didn't use the _--debug_ flag after all as taking a look at the compiled sql file is the better way of debugging tests.

##### Logging

The contents of `macros/logging.sql`:
```
{% macro learn_logging() %}
    {{ log("Call your mom!") }}
    {{ log("Call your dad!", info=True) }} --> Logs to the screen, too
--  {{ log("Call your dad!", info=True) }} --> This will be put to the screen
    {# log("Call your dad!", info=True) #} --> This won't be executed
{% endmacro %}
```

Executing the macro: 
```
dbt run-operation learn_logging
```

#### Variables
The contents of `marcos/variables.sql`:
```
{% macro learn_variables() %}

    {% set your_name_jinja = "Zoltan" %}
    {{ log("Hello " ~ your_name_jinja, info=True) }}

    {{ log("Hello dbt user " ~ var("user_name", "NO USERNAME IS SET!!") ~ "!", info=True) }}

    {% if var("in_test", False) %}
       {{ log("In test", info=True) }}
    {% else %}
       {{ log("NOT in test", info=True) }}
    {% endif %}

{% endmacro %}
```

We've added the following block to the end of `dbt_project.yml`:
```
vars:
  user_name: default_user_name_for_this_project
```

An example of passing variables:
```
dbt run-operation learn_variables --vars "{user_name: zoltanctoth}"
```

More information on variable passing: https://docs.getdbt.com/docs/build/project-variables

#### DBT Orchestration 

##### Links to different orchestrators

 * [dbt integrations](https://docs.getdbt.com/docs/deploy/deployment-tools)
 * [Apache Airflow](https://airflow.apache.org/)
 * [Prefect](https://www.prefect.io/)
 * [Prefect dbt Integration](https://www.prefect.io/blog/dbt-and-prefect)
 * [Azure Data Factory](https://azure.microsoft.com/en-us/products/data-factory)
 * [dbt Cloud](https://cloud.getdbt.com/deploy/)
 * [Dagster](https://dagster.io/)

##### Dagster

**Set up your environment**
Let's create a virtualenv and install dbt and dagster. These packages are located in [requirements.txt](requirements.txt).
```
virutalenv venv -p python3.11
pip install -r requirements.txt
```

**Create a dagster project**
Dagster has a command for creating a dagster project from an existing dbt project: 
```
dagster-dbt project scaffold --project-name dbt_dagster_project --dbt-project-dir=dbtlearn
```

_At this point in the course, open [schedules.py](dbt_dagster_project/dbt_dagster_project/schedules.py) and uncomment the schedule logic._

**Start dagster**
Now that our project is created, start the Dagster server:

***On Windows - PowerShell (Like the VSCode Terminal Window)***
```
cd dbt_dagster_project
$env:DAGSTER_DBT_PARSE_PROJECT_ON_LOAD = 1
dagster dev
```

***On Windows (Using cmd)***
```
cd dbt_dagster_project
setx DAGSTER_DBT_PARSE_PROJECT_ON_LOAD 1
dagster dev
```

***On Linux / Mac***

```
cd dbt_dagster_project
DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1 dagster dev
```

We will continue our work on the dagster UI at [http://localhost:3000/](http://localhost:3000) 

**Making incremental models compatible with orchestrators:**
The updated contents of `models/fct/fct_reviews.sql`:
```
{{
  config(
    materialized = 'incremental',
    on_schema_change='fail'
    )
}}
WITH src_reviews AS (
  SELECT * FROM {{ ref('src_reviews') }}
)
SELECT 
  {{ dbt_utils.generate_surrogate_key(['listing_id', 'review_date', 'reviewer_name', 'review_text']) }} as review_id,
  *
FROM src_reviews
WHERE review_text is not null

{% if is_incremental() %}
  {% if var("start_date", False) and var("end_date", False) %}
    {{ log('Loading ' ~ this ~ ' incrementally (start_date: ' ~ var("start_date") ~ ', end_date: ' ~ var("end_date") ~ ')', info=True) }}
    AND review_date >= '{{ var("start_date") }}'
    AND review_date < '{{ var("end_date") }}'
  {% else %}
    AND review_date > (select max(review_date) from {{ this }})
    {{ log('Loading ' ~ this ~ ' incrementally (all missing dates)', info=True)}}
  {% endif %}
{% endif %}
```

Passing a time range to our incremental model:
```
dbt run --select fct_reviews  --vars '{start_date: "2024-02-15 00:00:00", end_date: "2024-03-15 23:59:59"}'
```

Reference - Working with incremental strategies: https://docs.getdbt.com/docs/build/incremental-models#about-incremental_strategy
