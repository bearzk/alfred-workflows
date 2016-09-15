import sys, sched, time

class Timer(object):

    def __init__(self, minutes):
        self.schedule = sched.scheduler(time.time, time.sleep)
        self.minutes = minutes

    def _times_up(self):
        sys.stdout.write('Timer of ' + str(self.minutes) + ' minutes is up!')

    def run(self):
        self.schedule.enter(60 * self.minutes, 1, self._times_up, ())
        self.schedule.run()


query = int("{query}")

if query > 120:
    query = 120

timer = Timer(query)
timer.run()
