import pandas as pd
import psycopg2 
from fill_website_field import fill_site

def insert_query(query, comp, url, text):
    try:
        print("connecting to db")
        conn = psycopg2.connect(database='DEP', user='postgres', password='', host='vichogent.be', port='40045',options="-c search_path=dep" )
        cur = conn.cursor()
        print("doing query")
        cur.execute(query,(str(comp), str(url), str(text)))
        conn.commit()
        cur.close()
        conn.close()
    except (Exception) as error : 
        print(f"postgres error : {error}")
        print(text)

def get_onderneming_2():
    query = 'SELECT * FROM dep."Onderneming_2"'
    conn = psycopg2.connect(database='DEP', user='postgres', password='', host='vichogent.be', port='40045',options="-c search_path=dep" )
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


 

    
	                                                        


