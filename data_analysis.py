import pandas as pd
import numpy as np


def data_structure(list_info, parameter):
    link = r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\The_Global_Dataset_Apr_2020.csv'
    data = pd.read_csv(link, index_col=0)
    for info in list_info:
        if(info == 'num_labels'):
            a = list(set(data[parameter]))
            print('Num_Labels: {}'.format(len(a)))
        if(info == 'names_labels'):
            a = list(set(data[parameter]))
            print('Name_Labels: {}'.format(a))
        if(info == 'min_max'):
            print('Min_Value: {}'.format(data[parameter].min()))
            print('Max_Value: {}'.format(data[parameter].max()))
        
# data_structure(['names_labels'], 'typeOfSexConcatenated') # 'num_labels','names_labels','min_max'

columns_names = ['yearOfRegistration', 'Datasource', 'gender', 'ageBroad', 'majorityStatus', 'majorityStatusAtExploit', 'majorityEntry', 'citizenship', 'meansOfControlDebtBondage', 'meansOfControlTakesEarnings',
 'meansOfControlRestrictsFinancialAccess', 'meansOfControlThreats', 'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse', 'meansOfControlSexualAbuse', 'meansOfControlFalsePromises',
  'meansOfControlPsychoactiveSubstances', 'meansOfControlRestrictsMovement', 'meansOfControlRestrictsMedicalCare', 'meansOfControlExcessiveWorkingHours', 'meansOfControlUsesChildren',
   'meansOfControlThreatOfLawEnforcement', 'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlOther', 'meansOfControlNotSpecified', 'meansOfControlConcatenated', 
   'isForcedLabour', 'isSexualExploit', 'isOtherExploit', 'isSexAndLabour', 'isForcedMarriage', 'isForcedMilitary', 'isOrganRemoval', 'isSlaveryAndPractices', 'typeOfExploitConcatenated',
    'typeOfLabourAgriculture', 'typeOfLabourAquafarming', 'typeOfLabourBegging', 'typeOfLabourConstruction', 'typeOfLabourDomesticWork', 'typeOfLabourHospitality', 'typeOfLabourIllicitActivities',
     'typeOfLabourManufacturing', 'typeOfLabourMiningOrDrilling', 'typeOfLabourPeddling', 'typeOfLabourTransportation', 'typeOfLabourOther', 'typeOfLabourNotSpecified', 'typeOfLabourConcatenated',
      'typeOfSexProstitution', 'typeOfSexPornography', 'typeOfSexRemoteInteractiveServices', 'typeOfSexPrivateSexualServices', 'typeOfSexConcatenated', 'isAbduction', 'RecruiterRelationship', 
      'CountryOfExploitation', 'recruiterRelationIntimatePartner', 'recruiterRelationFriend', 'recruiterRelationFamily', 'recruiterRelationOther', 'recruiterRelationUnknown']

def null_values_replacement():
    link = r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\The_Global_Dataset_Apr_2020.csv'
    data = pd.read_csv(link, index_col=0)
    data = data.replace('-99',np.nan)
    data = data.replace(-99,np.nan)
    data.to_csv(r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\The_Global_Dataset_Apr_2020_nan.csv')

# null_values_replacement()

def country_code():
    # Se define la ubicación de los datos con el nombre de los paises y el código.
    source = r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\country_code.txt'
    # Se cargan los datos de tipo CSV.
    country_data = pd.read_csv(source, index_col = 0)
    # Se reinicia el index con el fin de poder disponer de 
    country_data = country_data.reset_index()
    # Se cambian los nombres con el fin de dejar uno estandarizado junto con el que presenta el otro dataset
    country_data.columns = ['Country_citizenship','citizenship']
    # Se carga la base de datos globales
    source_2 = r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\The_Global_Dataset_Apr_2020_nan.csv'
    # Se cargan los datos de tipo CSV.
    global_dataset = pd.read_csv(source_2, index_col = 0)
    # Se reemplazan los valores '00' por nulos para ambas columnas con información de la ubicación
    global_dataset['citizenship'] = global_dataset['citizenship'].replace('00',np.nan)
    global_dataset['CountryOfExploitation'] = global_dataset['CountryOfExploitation'].replace('00',np.nan)
    # Se unen ambas bases de datos, usando el tipo LEFT.
    final_data = pd.merge(global_dataset,country_data,how="left", on=['citizenship'])
    # Se crea una nueva columna con el nombre de la otra columna que hace referencia a la ubicación
    country_data['CountryOfExploitation'] = country_data['citizenship']
    # Se realiza la modificación del nombre de la columna del código del país, con el fin de integrar la información con la columna que hace referencia al pais en donde fue explotado.
    country_data = country_data[['Country_citizenship','CountryOfExploitation']]
    country_data.columns = ['Country_Exp','CountryOfExploitation']
    # Se realiza la segunda union para el pais de explotacion
    final_data = pd.merge(final_data,country_data,how="left", on=['CountryOfExploitation'])
    # Ya que existe un país con código NA, se cambia mencionado país por null ya que de acuerdo a lo verificado ese código no existe, pero si es interpretado como tal por los valores nulos
    final_data['Country_citizenship'] = final_data['Country_citizenship'].replace('Namibia',np.nan)
    final_data['Country_Exp'] = final_data['Country_Exp'].replace('Namibia',np.nan)
    # Se remplaza el nombre del pais considerando que no es reconocido por Tableau.
    final_data['Country_citizenship'] = final_data['Country_citizenship'].replace('CÃ´te d\'Ivoire','Ivory Coast')
    # Se almacena la informacion en un archivo de tipo CSV
    
    # print(set(list(final_data['gender'])))

    final_data.to_csv(r'C:\Users\User\OneDrive\ESTUDIOS\MAESTRIA\MASTER_DATA_SCIENCE\5. Fifth Semester\Visualizacion de Datos\PRA1 Seleccion Datos\Datos Explotacion\The_Global_Dataset_Country_nan.csv')
    
# country_code()

print('Hello World')