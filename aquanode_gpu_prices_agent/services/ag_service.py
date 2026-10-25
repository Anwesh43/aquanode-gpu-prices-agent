from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class AgService:
    def __init__(self):
        self.client = BaseHTTPClient(baseURL = os.environ["AQ_BASE_URL"])
        self.gpuDetailsMap = {}

    def _handleError(self, e):
        print("Error", str(e))
        return {
            "status": "Error",
            "message": str(e)
        }
    
    def getGpusMartetplaceData(self):
        try:
            response = self.client.getCall("marketplace")
            results = []
            if "data" in response:
                gpus = response["data"]
                for gpu in gpus:
                    gpuObj = {}
                    gpuObj["gpuShortName"] = gpu["gpuShortName"]
                    gpuObj["region"] = gpu["region"]
                    gpuObj["price"] = gpu["price"]
                    gpuObj["gpuMemory"] = gpu["gpuMemory"]
                    self.gpuDetailsMap["gpuShortName"] = gpu 
                    results.append(gpuObj)
            return results 
        except Exception as e:
            return self._handleError(e)

    def getGpuDetails(self, gpuShortName : str):
        if not(gpuShortName in self.self.gpuDetailsMap):
            self.getGpusMartetplaceData()
        return self.getGpusMartetplaceData[gpuShortName]
