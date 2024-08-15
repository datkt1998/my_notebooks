## 0.1. Nightscout

### 0.1.1. Guide

Setup nightscout account:

**DB**: MongoDB Atlas (M0 - free - 512MB storage) : [https://nightscout.github.io/vendors/mongodb/atlas/](https://nightscout.github.io/vendors/mongodb/atlas/)

**Webservice**: Render ([https://nightscout.github.io/vendors/render/new_user/](https://nightscout.github.io/vendors/render/new_user/))

**Troubleshoot Render**: [https://nightscout.github.io/troubleshoot/render/#troubleshoot-render](https://nightscout.github.io/troubleshoot/render/#troubleshoot-render)

### 0.1.2. Nightscout profile

### 0.1.3. Code to free up space

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

## 0.2. Loop & iAPS

### 0.2.1. App install