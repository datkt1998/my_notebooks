# Model workflow development

| **BigQuery Type** | **JSON Type** | **Example value**                  |
| ----------------- | ------------- | ---------------------------------- |
| String            | String        | "abc"                              |
| Integer           | Integer       | 1                                  |
| Float             | Float         | 1.2                                |
| Numeric           | Float         | 4925.000000000                     |
| Boolean           | Boolean       | true                               |
| TimeStamp         | String        | "2019-01-01 23:59:59.999999+00:00" |
| Date              | String        | "2018-12-31"                       |
| Time              | String        | "23:59:59.999999"                  |
| DateTime          | String        | "2019-01-01T00:00:00"              |
| Record            | Object        | { "A": 1,"B": 2}                   |
| Repeated Type     | Array[Type]   | [1, 2]                             |
| Nested Record     | Object        | {"A": {"a": 0}, "B": 1}            |
