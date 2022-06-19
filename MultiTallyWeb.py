# ─── IMPORTS ────────────────────────────────────────────────────────────────────
import PyATEMMax, web, time
from Config import *

# ─── ATEM CONFIG AND SETUP ──────────────────────────────────────────────────────
switcher = PyATEMMax.ATEMMax()

switcher.connect(SWITCHERIP)
switcher.waitForConnection()

# ─── WEB CONFIG AND SETUP ───────────────────────────────────────────────────────
urls = ('/(.*)', 'TallyWeb', 'Select')

app = web.application(urls, globals())

# ─── WEB CODE AND STATUS DETECTION ──────────────────────────────────────────────
class TallyWeb:
    def GET(self, name):
        
        tally_1 = str(switcher.tally.bySource.flags[1])
        tally_2 = str(switcher.tally.bySource.flags[2])
        tally_3 = str(switcher.tally.bySource.flags[3])
        #Clock
        current_time = time.strftime("%H : %M")

        #Web sorter
        if tally_1 == "[PGM]":
            tally_1_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-danger bg-gradient">
            <p class="text-center fs-1">Source: 1</p>
            <p class="text-center fs-1 ">ON AIR</p>
        </div>
            '''
        elif tally_1 == "[PVW]":
            tally_1_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-success bg-gradient">
            <p class="text-center fs-1">Source: 1</p>
            <p class="text-center fs-1">PREVIEW</p>
        </div>
            '''
        elif tally_1 == "[]":
            tally_1_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-secondary bg-gradient">
            <p class="text-center fs-1">Source: 1</p>
            <p class="text-center fs-1">NOTHING</p>
        </div>
            '''
        if tally_2 == "[PGM]":
            tally_2_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-danger bg-gradient">
            <p class="text-center fs-1">Source: 2</p>
            <p class="text-center fs-1 ">ON AIR</p>
        </div>
            '''
        elif tally_2 == "[PVW]":
            tally_2_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-success bg-gradient">
            <p class="text-center fs-1">Source: 2</p>
            <p class="text-center fs-1">PREVIEW</p>
        </div>
            '''
        elif tally_2 == "[]":
            tally_2_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-secondary bg-gradient">
            <p class="text-center fs-1">Source: 2</p>
            <p class="text-center fs-1">NOTHING</p>
        </div>
            '''
        if tally_3 == "[PGM]":
            tally_3_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-danger bg-gradient">
            <p class="text-center fs-1">Source: 3</p>
            <p class="text-center fs-1 ">ON AIR</p>
        </div>
            '''
        elif tally_3 == "[PVW]":
            tally_3_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-success bg-gradient">
            <p class="text-center fs-1">Source: 3</p>
            <p class="text-center fs-1">PREVIEW</p>
        </div>
            '''
        elif tally_3 == "[]":
            tally_3_state = '''
        <div class="col border border-dark border-3 rounded-pill bg-secondary bg-gradient">
            <p class="text-center fs-1">Source: 3</p>
            <p class="text-center fs-1">NOTHING</p>
        </div>
            '''
        return f'''
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <meta http-equiv="refresh" content="0.5">
</head>
<body style="background-color:#ea3f3f;">
    <div class="row">
        <div class="col">
            
        </div>
        <div class="col">
            <p class="text-center fs-1">{current_time}</p>
        </div>
        <div class="col">

        </div>
    </div>
    <div class="row ">
        {tally_1_state}
        {tally_2_state}
        {tally_3_state}
    </div>
</body>
</html>
        '''

# ─── RUN THE WEBSITE ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run()