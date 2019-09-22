import socket # Import thư viện socket
import sys # Import thư viện system

host = str(sys.argv[1]) # Sử dụng tham số môi trường số 1
port = int(sys.argv[2]) # Sử dụng tham số môi trường số 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
Khởi tạo lớp socket
socket.AF_INET có nghĩa khởi tạo lớp socket sử dụng IPv4
socket.SOCK_STREAM là socket sử dụng giao thức TCP
ngoài ra còn socket.SOCK_DGRAM là sử dụng giao thức UDP (không sử dụng ở bài này)
"""
s.bind((host, port)) # Mở socket trên port và host ở trên
s.listen() # Lắng nghe kết nối từ client
conn, addr  = s.accept() # Tạo connection khi có client kết nối
print('Connected by', addr[0])

while True:
  try:
    print('Waiting for response...')
    data = conn.recv(1024) # Nhận data từ client
    print("Client said: ", data.decode()) # In ra data dưới dạng string
    msg = input("Your message: ")
    conn.sendall(str(msg).encode()) # Gửi tất cả data dưới dạng byte
  except :
    conn.close() # Hủy kết nối khi có lỗi kết nối giữa server và client
    print('Client disconnected')
    conn, addr = s.accept() # Đợi kết nối từ client khác
    print('Connected ', addr[0])