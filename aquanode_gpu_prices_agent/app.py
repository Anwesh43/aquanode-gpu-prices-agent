from agents.gpu_ai_agent import recommendGpus
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(recommendGpus(prompt=prompt))