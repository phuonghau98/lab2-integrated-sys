import socket # Import thư viện socket
host = "127.0.0.1" # Địa chỉ loopback, là máy hiện tại
port = 8080 # Port có socket api của server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Khởi tạo lớp socket

s.connect((host, port)) # Kết nối tiến trình với socket

while True:
  msg = input('Enter your number: ') # Nhận vào tin nhắn của người dùng
  s.sendall(msg.encode()) # Gửi thông tin tới socket
  data = s.recv(1024) # Nhận data với từ buffer lên tới 1024 bytes từ server
  print('Response: {}'.format(data.decode())) # In ra data nhận được và decode sang utf-8