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


