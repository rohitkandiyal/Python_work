import openpyxl

wb=openpyxl.load_workbook('input.xlsx')
print wb.sheetnames			#available sheets in workbook
ws = wb['first']			#select ws

print wb.active				#to see active sheet of the wb
cell=ws['B2']
print cell.value			#access value
print cell.row
print cell.column

cell2=ws.cell(row=2,column=2)	#another way to access value.. recommended.
print cell2.value