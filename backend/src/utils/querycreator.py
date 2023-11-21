from utils.states import states

def querycreator(querybuilderdata):
    # Unpack querybuilderdata dictionary into variables for easier access and readability of code
    birthTable = querybuilderdata['birthTable']
    state = querybuilderdata['state']
    year = querybuilderdata['year']
    avgBirthWeight = querybuilderdata['avgBirthWeight']
    avgAgeMother = querybuilderdata['avgAgeMother']
    if state != '': state = states[querybuilderdata['state']]

    # Verify the table name to request and the conditional option to seggregate the data
    if birthTable == '': birthTable = 'g'
    table, conditional = '', ''
    if birthTable == 'mm':
        table = '_by_maternal_morbidity'
        conditional = 'Maternal_Morbidity_Desc'
    elif birthTable == 'ac':
        table = '_by_abnormal_conditions'
        conditional = 'Abnormal_Conditions_Checked_Desc'
    elif birthTable == 'ca':
        table = '_by_congenital_abnormalities'
        conditional = 'Congenital_Abnormality_Checked_Desc'
    elif birthTable == 'mr':
        table = '_by_mother_race'
        conditional = 'Mothers_Single_Race'
    elif birthTable == 'fr':
        table = '_by_father_race'
        conditional = 'Fathers_Single_Race'
    elif birthTable == 'p':
        table = '_by_payment'
        conditional = 'Source_of_Payment'
    
    # Verify the columns to request
    aam, abw = '', ''
    if avgAgeMother: aam = 'AVG(Ave_Age_of_Mother) AS AverageAgeMother'
    if avgBirthWeight: abw = 'AVG(Ave_Birth_Weight_gms) AS AverageBirthWeight'

    columns = '''SUM(Births) AS SumBirths, AVG(Births) AS AverageBirths'''
    if aam != '' and abw != '':
        columns = f'''{columns}, {aam}, {abw}'''
    elif aam != '' and abw == '':
        columns = f'''{columns}, {aam}'''
    elif aam == '' and abw != '':
        columns = f'''{columns}, {abw}'''

    # Verify the year to request
    yearwhere = ''
    if year != 'All': 
        yearwhere = f'''AND Year = "{year}-01-01"'''
    
    # Create the query based on the previous variables and return it
    dataset = 'bigquery-public-data.sdoh_cdc_wonder_natality.county_natality'
    if state != '' and birthTable != 'g':
        query = f'''SELECT SUBSTRING(County_of_residence, -2) AS State, {columns}, {conditional} AS Condition
                    FROM `{dataset}{table}`
                    WHERE SUBSTRING(County_of_residence, -2) = '{state}' {yearwhere}
                    GROUP BY State, Condition
                '''
    elif state != '' and birthTable == 'g':
        query = f'''SELECT SUBSTRING(County_of_residence, -2) AS State, {columns}
                    FROM `{dataset}{table}`
                    WHERE SUBSTRING(County_of_residence, -2) = '{state}' {yearwhere}
                    GROUP BY State
                '''
    elif state == '' and birthTable != 'g':
        if year != 'All':
            query = f'''SELECT {columns}, {conditional} AS Condition
                        FROM `{dataset}{table}`
                        WHERE {yearwhere.split('AND')[1]}
                        GROUP BY Condition
                    '''
        else:
            query = f'''SELECT {columns}, {conditional} AS Condition
                        FROM `{dataset}{table}`
                        GROUP BY Condition
                    '''
    elif state == '' and birthTable == 'g':
        if year != 'All':
            query = f'''SELECT {columns}
                        FROM `{dataset}{table}`
                        WHERE {yearwhere.split('AND')[1]}
                    '''
        else:
            query = f'''SELECT {columns}
                        FROM `{dataset}{table}`
                    '''
    return query