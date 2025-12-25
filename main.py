from modulos import funciones_api as gestapi
from modulos import scrapping_bio as scrap
from modulos import funciones_archivos as gestrkive

dataDriver = {}

sessionInfo = gestapi.get_2025_session()

dataDriver.update(sessionInfo)
session = sessionInfo['IDsession']
driver = gestapi.get_driver(session) 
dataDriver.update(gestapi.get_driver_info(driver))
dataDriver.update(gestapi.get_performance_stats(driver, session))
dataDriver.update(gestapi.get_position(driver, session))

URL = gestapi.create_URL(driver, dataDriver['searchName'])
dataDriver.update(scrap.get_biography(URL))

gestrkive.createArchive(dataDriver)
gestrkive.order_folder()


