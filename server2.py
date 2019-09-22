import socket

host = '127.0.0.1'
port = 8081
"""
Khởi tạo lớp socket
socket.AF_INET có nghĩa khởi tạo lớp socket sử dụng IPv4
socket.SOCK_STREAM là socket sử dụng giao thức TCP
ngoài ra còn socket.SOCK_DGRAM là sử dụng giao thức UDP (không sử dụng ở bài này)
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM means using TCP protocol
s.bind((host, port)) # Sử dụng IP và PORT để gán lớp socket
s.listen() # Sử dụng IP và PORT để gán lớp socket
conn, addr  = s.accept() # Blocking cho đến khi có kết nối từ client (lần khởi tạo)
print('Connected by', addr[0])

while True: # Lặp vĩnh viễn
  try:
    print('Waiting for response...')
    data = conn.recv(1024) # Nhận data từ client dưới dạng byte (tối đa 1024)
    print("Client said: ", data.decode()) # In ra nội dung nhận được dạng byte, sau đó decode ra str
    msg = input("Your message: ") # Server nhập vào tin nhắn
    conn.sendall(str(msg).encode()) # sendall gửi tất cả tin nhắn dạng byte,
  except :
    conn.close() # Đóng kết nối với client nếu có lỗi kết nối giữa client và server
    print('Client disconnected')
    conn, addr = s.accept() # Đợi kết nối từ client khác (blocking)
    print('Connected ', addr[0])
