import requests

def get_driver_info(driverNumber):
    url = f'https://api.openf1.org/v1/drivers?driver_number={driverNumber}' 
    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()
            driver = data[0] 
            shearchName = driver['full_name'].replace(' ', '_')

            info = {
                "teamName": driver["team_name"],
                "country": driver["country_code"],
                "fullName": driver["full_name"],
                'searchName': shearchName
            }
            return info
        
        return None
    except requests.exceptions.ConnectionError:
        print("No hay conexion a internet.")
        return None

def get_performance_stats(driverNumber, session):
    time = []
    url = f'https://api.openf1.org/v1/laps?session_key={session}&driver_number={driverNumber}' 
    response = requests.get(url)

    try:
        if response.status_code == 200:
            vueltas = response.json()
            for i in range(len(vueltas)):
                lapTime = vueltas[i]["lap_duration"]
                if lapTime is not None:
                    time.append(lapTime)
        
            if time:
                bestLap = min(time)
                promLap = sum(time)/len(vueltas)

                performance = {
                'bestLap': bestLap,
                'promLap': promLap,
            }
            
                return performance
            
            return None #si no trae informacion de tiempos
        
        return None
    except requests.exceptions.ConnectionError:
        print("No hay conexion a internet.")
        return None

def get_position(driverNumber, session):
    url = f'https://api.openf1.org/v1/position?session_key={session}&driver_number={driverNumber}' 
    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()
            rango = len(data)

            if rango > 1: 
                start = data[0]["position"]
                end = data[rango - 1]["position"]
                change = start - end
            
            position = {
                'start': start,
                'end': end,
                'change': change
            }

            return position
        
        return None
    except requests.exceptions.ConnectionError:
        print("No hay conexion a internet.")
        return None


def get_2025_session():
    url = "https://api.openf1.org/v1/sessions?year=2025&session_name=Race"
    IDs = []
    locations = []
    session = ''

    try:
        response = requests.get(url)
        if response.status_code == 200:
            carreras = response.json()
            
            print("Sesiones 2025")
            for carrera in carreras:
                print(f"{carrera['location']} - {carrera['session_name']} (ID: {carrera['session_key']})")
                IDs.append(str(carrera['session_key']))
                locations.append(str(carrera['location']))
            
            while carrera not in IDs:
                carrera = input('Selecciona el ID de la session a investigar: ')

                if carrera not in IDs:
                    print('El ID indicado no esta en el listado proporcionado. Intente nuevamente')

            indice = IDs.index(carrera)
            nameSession = locations[indice]

            session = {
                'nameSession': nameSession,
                'IDsession': carrera

            }
            return session
        else:
            print(f"Error al conectar: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("No hay conexion a internet.")
        return None


def get_driver(session):
    url = f"https://api.openf1.org/v1/drivers?session_key={session}"
    numberList = []
    driverNumber = ''

    response = requests.get(url)

    try:
        if response.status_code == 200:
            pilotos = response.json()

            if not pilotos:
                print('No hay informacion de la session indicada. Verifique el session ID')
                return None
            
            else:
                print(f"\n--- Pilotos en la sesión {session} ---")
                for piloto in pilotos:
                    print(f"#{piloto['driver_number']} - {piloto['full_name']} ({piloto['team_name']})")
                    numberList.append(str(piloto['driver_number']))
                print(numberList)

                while driverNumber not in numberList:
                    driverNumber = input('Seleccione un piloto de la lista: ')

                    if driverNumber not in numberList:
                        print('Debe ingresar el numero del piloto en la lista')

            return driverNumber
        else:
            print(f"Error al conectar: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("No hay conexion a internet.")
        return None


def create_URL(numberDriver, searchName):
    generalURL = 'https://es.wikipedia.org/wiki/'

    match numberDriver:
        case 63: URL = generalURL + 'George_Russell_(piloto)'
        case 55: URL = generalURL + 'Carlos_Sainz_Jr.'
        case _: URL = generalURL + searchName

    return URL

PRUEBA = {
            'start': "start",
            'end': "end",
            'change': "change",
            'bestLap': "bestLap",
            'promLap': "promLap",
            "teamName": "team_name",
            "country": "country_code",
            "fullName": "full_name",
            'searchName': "shearchName"
            }