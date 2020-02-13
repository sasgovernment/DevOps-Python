#https://sassoftware.github.io/python-swat/getting-started.html
#https://github.com/sassoftware/python-swat

import swat

sess = swat.CAS('sasserver.demo.sas.com', 5570, 'sasdemo', 'Orion123')

file_name="viya_reg.csv"
indata="viya_reg"

sess.loadactionset(actionset="table")

if not sess.table.tableExists(table=indata).exists:
    tbl = sess.upload_file(file_name, casout={"name":indata}, promote='True')
    
tbl.head()

sess.close()
