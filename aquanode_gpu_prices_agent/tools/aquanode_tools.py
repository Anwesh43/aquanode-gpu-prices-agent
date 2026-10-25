from services.ag_service import AgService

ags = AgService()

def getGpusMarketplaceData():
    print(f"Calling getGpusMarketplaceData tool")
    return ags.getGpusMartetplaceData()

def getGpuDetails(gpuShortName : str):
    print(f"Calling getGpuDetails tool {gpuShortName}")
    return ags.getGpuDetails(gpuShortName=gpuShortName)

def getTools():
    tools = []
    tools.append(getGpusMarketplaceData)
    tools.append(getGpuDetails)
    return tools 
