import socket # Import thư viện socket

host = '127.0.0.1' # Gán địa chỉ ip cho biến host, đây là địa chỉ máy hiện tại
port = 8080 # Gán port mở socket ip1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
Khởi tạo lớp socket
socket.AF_INET có nghĩa khởi tạo lớp socket sử dụng IPv4
socket.SOCK_STREAM là socket sử dụng giao thức TCP
ngoài ra còn socket.SOCK_DGRAM là sử dụng giao thức UDP (không sử dụng ở bài này)
"""
s.bind((host, port)) # Sử dụng IP và PORT để gán lớp socket
s.listen() # Sử dụng IP và PORT để gán lớp socket
conn, addr  = s.accept() # Blocking cho đến khi có kết nối từ client (lần khởi tạo)

viDict = {  # Định nghĩa kiểu dictionary trong python để chuyển số về chữ
  0: "không", 1: "một", 2: "hai", 3: "ba",
  4: "bốn", 5: "năm", 6: "sáu", 7: "bảy",
  8: "tám", 9: "chín"
}

def numberToString (num): # Chuyển đổi số thành chữ
  return viDict[int(num)]

while True: # Lặp vĩnh viễn
  try:
    print('Connected by', addr[0])
    data = conn.recv(1024) # Nhận data từ client dưới dạng byte (tối đa 1024)
    try:
      if 0 <= (int(data.decode())) < 10: # Kiểm tra có nằm trong khoảng 0 - 10 hay không
        result = numberToString(data.decode()) # data.decode() giúp chuyển dạng byte về string (utf-8)
      else:
        result = "Giá trị nằm trong dãy từ 0 - 9"
    except ValueError: # Exception tránh trường hợp không phải số
      result = "Không phải số nguyên"
    conn.sendall(result.encode()) # Gửi tất cả các byte đi, trước khi gửi chuyển string về byte bằng .encode()
  except: # Tránh trường hợp client ngắt kết nối
    conn.close() # Nếu ngắt kết nối thì ngắt kết nối với client
    conn, addr = s.accept() # Blocking code đến khi có kết nối mới
