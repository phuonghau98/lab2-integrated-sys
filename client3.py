import socket # Import thư viện socket
import sys # Import thư viện system

host = str(sys.argv[1]) # Lấy biến môi trường số 1
port = int(sys.argv[2]) # Lấy biến môi trường số 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Khởi tạo lớp socket
"""
Khởi tạo lớp socket
socket.AF_INET có nghĩa khởi tạo lớp socket sử dụng IPv4
socket.SOCK_STREAM là socket sử dụng giao thức TCP
ngoài ra còn socket.SOCK_DGRAM là sử dụng giao thức UDP (không sử dụng ở bài này)
"""
s.connect((host, port)) # Kết nối tiến trình với socket đã mở ra từ server

while True:
  msg = input('Enter yor message: ') # Nhận vào tin nhắn của người dùng
  s.sendall(msg.encode()) # Gửi thông tin tới socket
  print('Waiting for response...')
  data = s.recv(1024) # Nhận data với từ buffer lên tới 1024 bytes từ server
  print('Server said: {}'.format(data.decode())) # In ra data nhận được và decode sang utf-8