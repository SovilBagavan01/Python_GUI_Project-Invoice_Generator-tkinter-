from docxtpl import DocxTemplate


doc  = DocxTemplate("Relecloud.docx")

invoice_list = [[2,"mouse",200,2]]

#get the current date and time


doc.render({"name":"sovil","invoice_list":invoice_list,"current_datetime":current_datetime})

doc.save("new_relecloud.docx")