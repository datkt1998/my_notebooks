import asyncio


# Giả lập việc tải dữ liệu cho từng trang web
async def download_page(page):
    print(f"Bắt đầu tải trang {page}")
    await asyncio.sleep(2)
    print(f"Tải xong trang {page}")
    return f"Dữ liệu từ trang {page}"


async def main():
    # Tạo nhiều tác vụ tải trang cùng một lúc
    tasks = [download_page(i) for i in range(1, 4)]

    # Đợi tất cả các tác vụ hoàn thành
    results = await asyncio.gather(*tasks)

    print(f"Tất cả dữ liệu: {results}")


# Chạy chương trình
asyncio.run(main())
