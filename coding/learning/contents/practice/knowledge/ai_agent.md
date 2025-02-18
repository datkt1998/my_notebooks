# AI Agent

source: https://huyenchip.com/2025/01/07/agents.html#agent_overview
## Agent Overview

- Agent là bất cứ thứ gì có thể nhận biết môi trường xung quanh và hành động dựa trên đó.
- Agent được xác định bởi môi trường hoạt động và các hành động có thể thực hiện. Ví dụ, nếu agent được dùng để chơi game, thì game đó là môi trường của nó.
- Các công cụ (tools) giúp agent thực hiện các hành động. Ví dụ, ChatGPT là một agent có các công cụ như tìm kiếm trên web, chạy code Python và tạo ảnh.

Component:
- **Tools**: Tools là các công cụ để Agent thực hiện được ácc actions trong một môi trường được định nghĩa trước. 
	- Ví dụ: an agent built on top of GPT-4. Its environment is the computer with the terminal and the file system. Its set of actions include navigate repo, search files, view files, and edit lines.
	![A coding agent](https://huyenchip.com/assets/pics/agents/1-swe-agent.png)
- **Planning**: là sequence of actions để hoàn thành được step, và được xác định khi step trước được hoàn thành:



Ví dụ: Với 1 Agent được thiết kế có những action như sau:
- response generation,
- SQL query generation, and
- SQL query execution.

Khi người dùng query: `"Project the sales revenue for Fruity Fedora over the next three months"`. Agent sẽ thực hiện theo cơ chế:

1. *Planning* | Suy nghĩ làm thế nào để có kết quả ? Nó có thể lấy được từ bằng việc predict future sales, Nên nó cần lấy được dữ liệu quá khứ của sale để predict kết quả. An agent’s reasoning can be shown as intermediate responses.
2. *Action* | Invoke SQL query generation to generate the query to get sales numbers from the last five years.
3. *Action* | Invoke SQL query execution to execute this query.
4. *Planning* | Reason about the tool outputs (outputs from the SQL query execution) and how they help with sales prediction. It might decide that these numbers are insufficient to make a reliable projection, perhaps because of missing values. It then decides that it also needs information about past marketing campaigns.
5. *Action* | Invoke SQL query generation to generate the queries for past marketing campaigns.
6. *Action* | Invoke SQL query execution.
7. *Planning* | Reason that this new information is sufficient to help predict future sales. It then generates a projection.
8. *Planning* | Reason that the task has been successfully completed.

Agent tiếp tục planning khi có kết quả của task trước.

**Lưu ý:**
- Do Agent là kết quả tổ hợp sau nhiều bước, nên với một task sử dụng nhiều steps, mỗi steps có tỷ lệ sai số nhất định. Kết quả cuối cùng chỉ đúng khi kết quả của các step đều đúng, nên khi có nhiều steps thì độ chính xác tổng thể sẽ giảm xuống.
- 1 Task chứa nhiều steps, có thể mất nhiều time và money để tính toán.
- Với một môi trường cho Agent cụ thể, thì độ thành công của Agent phụ thuộc và những **Tool nó có quyền access** và khả năng **planning của AI**

## Tools

Công cụ giúp agent nhận biết và tác động vào môi trường. Có những công cụ chỉ để đọc thông tin (read-only actions) và những công cụ để thay đổi thông tin (write actions). Việc lựa chọn công cụ rất quan trọng, vì nó quyết định khả năng của agent.

Các loại công cụ:
- **Tăng cường kiến thức (Knowledge augmentation)**: 
	- Công cụ tìm kiếm văn bản
	- Công cụ retriever hình ảnh
	- Công cụ thực thi SQL để lấy thông tin từ cơ sở dữ liệu. 
	- Web browsing (duyệt web) giúp agent cập nhật thông tin mới nhất.
	- API
	- ....
- **Mở rộng khả năng (Capability extension)**: 
	- máy tính
	- công cụ chuyển đổi múi giờ
	- code interpreter (trình thông dịch code).... Code interpreter cho phép agent viết code để phân tích dữ liệu hoặc chạy các thí nghiệm.
	- ...
- **Hành động ghi (Write actions)**: Cho phép agent thay đổi dữ liệu. Cần phải cẩn trọng khi cho phép AI thực hiện các hành động này.
	- sửa đổi cơ sở dữ liệu
	- gửi email. 

## Planning

**Tasks** của user sẽ có mục tiêu (goal) và constraint (các ràng buộc đi kèm). Planning giúp giải quyết các complex tasks, giúp các Agent hiểu được task, đánh trọng số cho từng solution và lựa chọn solution phù hợp là roadmap of steps để hoàn thành được task.
- Nên tách việc lập kế hoạch và thực thi để tránh lãng phí tài nguyên. Có thể dùng các phương pháp như heuristics hoặc AI để đánh giá kế hoạch.
- Quá trình planning bao gồm: generate plan --> validate plan (nếu ko phù hợp thì generate lại) --> executed
- Quá trình validate có thể sử dụng:
	- heuristics: xoá bỏ cũng plans có invalid action hoặc quá nhiều steps
	- AI judges: đánh giá plan xem có phù hợp hay không
- Plans can be generated in parallel to speed up the process

**System** have 3 components (considered an agent) of planning: 
- a plan generator: 
- a plan validator
- a plan executor

**Intent classification** is often used to help agents plan. 
- An intent classifier can classify requests, and knowing the intent helps the agent pick the right tools. 
- The intent classification mechanism can be considered another agent in a multi-agent system. 
- The agent should be able to reject irrelevant requests.

**Humans** can be involved in any stage to aid with the process and mitigate risks. 
- A human expert can provide a plan, validate a plan, or execute parts of a plan. 
- For risky operations, the system can ask for explicit human approval before executing or defer to humans to execute these operations

**Solving a task** typically involves these processes:
1. *Plan generation*: Devising a plan to accomplish the task.
	- The simplest way to turn a model into a plan generator is with prompt engineering. 
	- *Function calling* is a feature offered by many model providers that allows models to use tools
2. *Reflection and error correction*: Evaluating the plan and generating a new one if the initial plan is flawed.
3. *Execution*: Taking actions as outlined in the generated plan, often involving function calls.
4. *Reflection and error correction*: Evaluating the outcomes of actions and determining whether the goal has been achieved, correcting mistakes, and generating a new plan if the goal is not completed.

**Planning/execution tradeoff**:
- A detailed plan is harder to generate, but easier to execute
- A higher-level plan is easier to generate, but harder to execute
- An approach to circumvent this tradeoff is to plan hierarchically

**Complex plan**:
- different control flows: sequential or parallel
- if statement
- for loop


**Reflection and error correction** are important for an agent's success:
- After receiving a user query to evaluate if the request is feasible.
- After the initial plan generation to evaluate whether the plan makes sense.
- After each execution step to evaluate if it’s on the right track.
- After the whole plan has been executed to determine if the task has been accomplished.

**Tool Selection**: More tools give the agent more capabilities, but the more tools there are, the harder it is to efficiently use them
- Compare how an agent performs with different sets of tools.
- Do an ablation study to see how much the agent’s performance drops if a tool is removed from its inventory. If a tool can be removed without a performance drop, remove it.
- Look for tools that the agent frequently makes mistakes on. If a tool proves too hard for the agent to use—for example, extensive prompting and even finetuning can’t get the model to learn to use it—change the tool.
- Plot the distribution of tool calls to see what tools are most used and what tools are least used. Figure 6-14 shows the differences in tool use patterns of GPT-4 and ChatGPT in [Chameleon](https://arxiv.org/abs/2304.09842) (Lu et al., 2023).

![Different models have different tool preferences](https://huyenchip.com/assets/pics/agents/7-tool-preference.png)
