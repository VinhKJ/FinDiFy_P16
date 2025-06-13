# Hướng dẫn Project #16: Mô phỏng Blockchain đơn giản

## Giới thiệu

Project này mô phỏng hoạt động cơ bản của một Blockchain, bao gồm việc tạo các khối (Block) và xâu chuỗi chúng lại với nhau để tạo thành một chuỗi khối (Blockchain). Mục tiêu là giúp bạn hiểu rõ hơn về cấu trúc dữ liệu của Blockchain mà không đi sâu vào các khái niệm phức tạp như mining hay cơ chế đồng thuận.

## Cấu trúc Project

Project bao gồm hai class chính:

1.  **`Block`**: Đại diện cho một khối trong Blockchain.
2.  **`Blockchain`**: Đại diện cho toàn bộ chuỗi khối.

## Class `Block`

Mỗi `Block` có các thuộc tính sau:

*   `index`: Số thứ tự của khối trong chuỗi.
*   `timestamp`: Thời gian tạo khối.
*   `data`: Dữ liệu được lưu trữ trong khối (ví dụ: thông tin giao dịch).
*   `previous_hash`: Mã băm (hash) của khối trước đó trong chuỗi. Đây là yếu tố quan trọng tạo nên tính liên kết của Blockchain.
*   `hash`: Mã băm của chính khối hiện tại, được tính toán dựa trên tất cả các thuộc tính khác của khối.

### Phương thức

*   `__init__(self, index, timestamp, data, previous_hash)`: Hàm khởi tạo của Block.
*   `calculate_hash(self)`: Phương thức này tính toán mã băm SHA256 của khối. Mã băm được tạo ra bằng cách kết hợp tất cả các thuộc tính của khối (index, timestamp, data, previous_hash). Bất kỳ thay đổi nào trong dữ liệu của khối sẽ làm thay đổi mã băm, từ đó làm mất hiệu lực của các khối tiếp theo trong chuỗi.

## Class `Blockchain`

Class `Blockchain` quản lý một danh sách các `Block`.

### Thuộc tính

*   `chain`: Một danh sách chứa tất cả các khối trong Blockchain.

### Phương thức

*   `__init__(self)`: Hàm khởi tạo của Blockchain. Khi một Blockchain mới được tạo, nó sẽ tự động tạo ra một khối đầu tiên, được gọi là 


khối Genesis (Genesis Block).
*   `create_genesis_block(self)`: Tạo khối đầu tiên của Blockchain. Khối Genesis có `index` là 0, `previous_hash` là "0" và dữ liệu là "Genesis Block".
*   `get_latest_block(self)`: Trả về khối cuối cùng trong chuỗi Blockchain.
*   `add_block(self, new_block)`: Thêm một khối mới vào chuỗi. Trước khi thêm, phương thức này sẽ cập nhật `previous_hash` của `new_block` bằng `hash` của khối cuối cùng hiện có trong chuỗi, sau đó tính toán lại `hash` cho `new_block`.

## Cách sử dụng

Để chạy mô phỏng, bạn cần có hai file:

1.  `blockchain_simulation.py`: Chứa định nghĩa của `Block` và `Blockchain` classes.
2.  `demo.py`: Chứa script để tạo và tương tác với Blockchain.

### `blockchain_simulation.py`

```python
import datetime
import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode("utf-8") +
                   str(self.timestamp).encode("utf-8") +
                   str(self.data).encode("utf-8") +
                   str(self.previous_hash).encode("utf-8"))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
```

### `demo.py`

```python
import datetime
from blockchain_simulation import Block, Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

print("Mining block 1...")
my_blockchain.add_block(Block(1, datetime.datetime.now(), {"amount": 4, "sender": "Alice", "receiver": "Bob"}, ""))

print("Mining block 2...")
my_blockchain.add_block(Block(2, datetime.datetime.now(), {"amount": 8, "sender": "Bob", "receiver": "Charlie"}, ""))

print("Mining block 3...")
my_blockchain.add_block(Block(3, datetime.datetime.now(), {"amount": 12, "sender": "Charlie", "receiver": "David"}, ""))

print("\nBlockchain:")
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 20)
```

### Chạy chương trình

Để chạy mô phỏng, mở terminal trong thư mục chứa hai file trên và thực hiện lệnh sau:

```bash
python3.11 demo.py 
```
(Điều kiện cần: máy tính cài đặt sẵn python phiên bản 3.11 trở lên)

### Kết quả đầu ra

Chương trình sẽ in ra thông tin chi tiết của từng khối trong chuỗi Blockchain, bao gồm `index`, `timestamp`, `data`, `previous_hash` và `hash` của từng khối. Bạn sẽ thấy rằng `previous_hash` của mỗi khối khớp với `hash` của khối trước đó, minh họa tính liên kết của chuỗi.
