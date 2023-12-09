# Data Warehouse creation and population

Little project to solve the problem with the repetitive creation and population of data warehouses from college (being lazy with alter tables 🤡)


## Modules list:
- MySQL Connector/Python
- Numpy
- Pandas
- Psycopg2
- Pypdf

## Steps:
- [ ] Read tables and attributes from pdf  
<p align='center'>
<img src='.\diagrams\from_diagram_to_dict.png' 
    alt='Image showing the conversion of the tables on the PDF to a python dictionary'
    title='From PDF to Python Dict'
    width=75%>
</p>

- [ ] Using the python dictionary, make the create statements  
<p align='center'>
<img src='.\diagrams\from_dict_to_create_statement.png' 
    alt='Image showing the conversion of the python dictionary to the CREATE statement'
    title='From Python Dict to CREATE statement'
    width=75%>
</p>

- [ ] Read the data on CSVs and send to the database
<p align='center'>
<img src='.\diagrams\from_csvs_to_database.png' 
    alt='Image showing the insertion of data from the CSV into the database'
    title='From CSV to database'
    width=75%>
</p>

- [ ] Final step: Happiness
<p align='center'>
<img src='.\diagrams\true_happiness.jpeg' 
    title='True Happiness from coding'
    width=85%>
</p>
