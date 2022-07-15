import json
import time

def timestampInMilliseconds():
    return int(round(time.time() * 1000))

class Logger:
    timings = []
    logs = []
    print = lambda _self, message: print(message)

    def startTimeMeasurement(self, identifier, description):
        self.timings.append({
            "identifier": identifier,
            "description": description,
            "start": timestampInMilliseconds(),
            "end": None,
        })
    
    def endTimeMeasurement(self, identifier):
        for index in range(len(self.timings)):
            if self.timings[index]["identifier"] == identifier:
                self.timings[index]["end"] = timestampInMilliseconds()
                return

        self.log(f"❌ Could not find a measurement for {identifier}")

    def log(self, message, params = None, type = "info"):
        jsonMessage = json.dumps(
            {"type": type, "time": timestampInMilliseconds(), "message": message, "params": params},
            ensure_ascii=False
        )
        self.print(jsonMessage)
        self.logs.append(jsonMessage)

    def logError(self, message, params = None):
        self.log(message, params, "error")

    def logTimings(self):
        for timing in self.timings:
            if timing['end'] == None:
                self.log(f"Time measurement for {timing['identifier']} not finished")
            else:
                usedTime = timing['end'] - timing['start']
                message = f"⏳ {timing['description']} in {usedTime}ms"
                self.logWithTiming(message, usedTime)

    def logWithTiming(self, message, timingInMilliseconds):
        self.log(message, {"timingInMilliseconds": timingInMilliseconds})

    def writeToFile(self, fileName):
        with open(fileName, 'w', encoding='utf-8') as fileHandle:
            messages = ",\n".join(self.logs)
            fileHandle.write(f"[\n{messages}\n]")
