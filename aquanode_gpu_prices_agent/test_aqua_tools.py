from tools.aquanode_tools import getGpuDetails, getGpusMarketplaceData
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")

if __name__ == "__main__":
    gpus = getGpusMarketplaceData()
    writeFile("test_martketplace.json", gpus)
    if len(gpus) > 0 and "gpuShortName" in gpus[0]:
        writeFile("test_gpus.json", getGpuDetails(gpus[0]["gpuShortName"]))