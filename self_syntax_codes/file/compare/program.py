import filecmp
file1 = r'C:\Users\kandiyal\Desktop\hdd\knowledgebase\Unix_hdd\Unix_concepts.docx'
file2 = r'C:\Users\kandiyal\Desktop\for_work\knowldgebase\Unix\Unix_concepts.docx'

'''print type(file1)
print file1.read()
print "\n\n"+file2.read()
'''


if filecmp.cmp(file1,file2):
	print "Files are identical"
else:
	print "Not identical"