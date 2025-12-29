from modulos import get_info as info
from modulos import utilidades as util

dataDriver = {}
menu = ''

while menu != '0':

    try:
        menu = util.show_menu()

        match menu:
            case '0':
                print('Saliendo... Hasta luego!')
            case '1': 
                sessionData = info.get_2025_session()
                if sessionData:
                    session = sessionData['IDsession']
                    dataDriver.update(sessionData)

                    driverInfo = info.get_driver(session)
                    if driverInfo:
                        numberDriver = driverInfo['driverNumber']
                        dataDriver.update(driverInfo)

                        print('Generando reporte...')
                        util.safe_update(dataDriver, info.get_driver_info(numberDriver))
                        util.safe_update(dataDriver, info.get_performance_stats(numberDriver, session))
                        util.safe_update(dataDriver, info.get_position(numberDriver, session))

                        URL = util.create_URL(numberDriver, dataDriver['searchName'])
                        util.safe_update(dataDriver, info.get_biography(URL))

                        util.createArchive(dataDriver)
                        util.order_folder()  
                    
                    else:
                        print('Ha ocurrido un error al obtener la informacion de un piloto')
                else:
                    print('Ha ocurrido un error al obtener la informacion de la session')

                util.clean_temp_files()
                
            case '2':
                util.order_folder()  
            case '3':
                util.clean_temp_files()                
            case _:
                print('Debe seleccionar una opcion del menu')
    

    except ValueError:
        print('Debe seleccionar una de las opciones en numeros')





