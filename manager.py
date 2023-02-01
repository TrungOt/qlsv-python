
from students import Student
import students as st

select = 1

dict1 = {1: "MySQL", 2: "SQLServer", "T":"A", (1,4):"V", 3:4}
#dict1[4] = "jqk"
print (dict1)

while select != 0:
	print("\n")
	print(""" QUẢN LÝ SINH VIÊN """)
	print("------------------------")
	print("- Nhập 1: Danh sách ---")
	print("- Nhập 2: Thêm      ---")
	print("- Nhập 3: Xóa       ---")
	print("- Nhập 4: Sửa       ---")
	print("- Nhập 0: Thoát     ---")
	print("------------------------\n")
	print("Nhập lựa chọn: ")

	select = int(input())
	s = st.Student()

	if select == 1:
		print("DANH SÁCH SINH VIÊN")
		s.show()

	elif select == 2:
		print("THÊM SINH VIÊN")
		print("Nhập tên sinh viên: ", end="")
		name = input()
		s.insert(name)

	elif select == 3:
		print("XÓA SINH VIÊN")
		print("Nhập id sinh viên: ", end="")
		id = input()
		s.delete(id)

	elif select == 4:
		print("SỬA SINH VIÊN")
		print("Nhập id sinh viên: ", end="")
		id = input()
		print("Nhập tên sinh viên: ", end="")
		name = input()
		s.update(id,name)
	else:
		break