# 1. Profile 

| TDD              | 45~50U                                                |
| ---------------- | ----------------------------------------------------- |
| Basal            | 15.5U = 0.7 (0h) + 0.75 (6h) + 0.65 (10h) + 0.6 (15h) |
| ISF              | 2.7 mmol/L/U                                          |
| CR               | 10.2 g/U (~ 500 / TDD )                               |
| Target GB        | 108 mg/dl (6 mmol/l)                                  |
| **Calculate UI** | = adj + carb/10.2+ (gb - 108)/(2.7\*18)               |
https://www.adces.org/danatech/insulin-pumps/insulin-pumps-101/insulin-pump-infusion-set-placements

## 1.1. IAps Profile


| group         | index            | value |
| ------------- | ---------------- | ----- |
| Fat & protein | Delay in minutes | 1     |

# 2. Resource

| No. | Loại                              | Chi tiết                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Note                             |
| --- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 0.  | Nightscout (đang dùng - for iAPS) | **Atlas DB user/pass**:  by datkt98@gmail.com<br>Connection :<br>- Cluster : datcgm<br>- user/pass: datkt98 / nguchochet1998<br>- database : datcgm <br>- url: mongodb+srv://datkt98:nguchochet1998@datcgm.srqfv4n.mongodb.net/datcgm?retryWrites=true&w=majority                                                                                                                                                                                                                                                       |                                  |
| 1.  | Nightscout (đang dùng - for loop) | - **Atlas** DB user/pass: datnightscout / nguchochet1998  <br>-  <br>**Connection**: mongodb+srv://datnightscout:nguchochet1998@datkhong.ylieg2n.mongodb.net/mycgm?retryWrites=true&w=majority  <br>-  <br>**Database name**: mycgm  <br>-  <br>**API secret**: Clearinghouse@1998  <br>-  <br>**site**: https://nightscout-pz7j.onrender.com/                                                                                                                                                                          |                                  |
| 2.  | Nightscout - khách 1              | - **Gmail**: nightscout.vn01 / abc@123123456  <br>-  <br>**Cluster name**: Cluster0  <br>-  <br>**Atlas DB user/pass**: nightscoutvn01 / abc@123123456  <br>-  <br>**Database name**: nightscout  <br>-  <br>**Connection**: mongodb+srv://nightscoutvn01:abc@123123456@cluster0.ss1xski.mongodb.net/nightscout?retryWrites=true&w=majority  <br>-  <br>**github**: nightscout.vn01@gmail.com / Clearinghouse@1998  <br>-  <br>**API secret**: Abc123123456  <br>-  <br>**site**: https://nightscout-es6c.onrender.com/ | phone gmail recovery: 0559821698 |
| 3.  | Nightscout - khách 2              | - **Gmail**: nightscout.vn02 / abc@123123456  <br>-  <br>**Cluster name**: Cluster0  <br>-  <br>**Atlas DB user/pass**: nightscoutvn02 / abc@123123456  <br>-  <br>**Database name**: nightscout  <br>-  <br>**Connection**: mongodb+srv://nightscoutvn02:abc@123123456@cluster0.tmuylu2.mongodb.net/nightscout?retryWrites=true&w=majority  <br>-  <br>**github**: nightscout.vn02@gmail.com / Clearinghouse@1998  <br>-  <br>**API secret**: Abc123123456  <br>-  <br>**site**: https://nightscout-kr8a.onrender.com/ | phone gmail recovery: 0944921214 |

# 3. Setup
## 3.1. Nightscout

### 3.1.1. Guide

Setup nightscout account:

**DB**: MongoDB Atlas (M0 - free - 512MB storage) : [https://nightscout.github.io/vendors/mongodb/atlas/](https://nightscout.github.io/vendors/mongodb/atlas/)

**Webservice**: Render ([https://nightscout.github.io/vendors/render/new_user/](https://nightscout.github.io/vendors/render/new_user/))

**Troubleshoot Render**: [https://nightscout.github.io/troubleshoot/render/#troubleshoot-render](https://nightscout.github.io/troubleshoot/render/#troubleshoot-render)

### 3.1.2. Nightscout profile

### 3.1.3. Code to free up space

- Cách 1: Sử dụng giao diện nightscout [https://nightscout-kdu7.onrender.com/admin/](https://nightscout-kdu7.onrender.com/admin/)
    
    ![[nightscout_interface.png]]
    
- Cách 2: Sử dụng code mongodb
    ![[freespace mongo.jpeg]]
    Connect to db : sử dụng mongo compass và URL connection string
    > mongodb+srv://datnightscout:nguchochet1998@datkhong.ylieg2n.mongodb.net/
    
    ```bash
    
    # show database
    show dbs
    
    # choose database [database name]
    use mycgm 
    
    # count documents
    db.devicestatus.countDocuments()
    
    # delete documents before 2023-12-24 (the last 30 days)
    db.devicestatus.deleteMany({"created_at":{"$lt":"2023-12-24T00:00:00.000Z"}})
    ```

## 3.2. Loop & iAPS

### 3.2.1. App install