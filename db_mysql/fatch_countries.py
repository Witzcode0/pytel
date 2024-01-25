from .dbConnection import cursor

def get_specific_char_to_countries(ch):
    sql = f"SELECT country_id, country_name FROM countries WHERE UPPER(country_name) LIKE '{ch}%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_specific_country_details(country_name):
    sql = f"SELECT * FROM countries WHERE country_name = '{country_name}'"
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result