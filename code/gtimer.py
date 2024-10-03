from pygame.time import get_ticks

# Timer Class
class Timer:
    # properties init func
    def __init__(self, duration, repeated=False, func=None)->None:
        self.repeated = repeated
        self.func = func
        self.duration = duration
        self.start_time = 0
        self.active = False
    
    # game activate func
    def activate(self):
        self.active = True
        self.start_time = get_ticks()
    
    # game deactivate func
    def deactivate(self):
        self.active = False
        self.start_time = 0
    
    # game update --> timer movement
    def update(self):
        current_time = get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            # call func
            if self.func and self.start_time != 0:
                self.func()
            # reset timer
            self.deactivate()
            # repeat the timer
            if self.repeated:
                self.activate()