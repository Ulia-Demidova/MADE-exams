class User:
    def __init__(self, order_id, ordered_at, x, y, k):
        self.orders = {order_id : ordered_at + x*60 + y*60 + k*60} #car id : expected_finish
        self.sum_lateness = 0
            
    def ordered(self, order_id, ordered_at, x, y, k):
        self.orders[order_id] = ordered_at + x*60 + y*60 + k*60
    
    def late(self, time):
        self.sum_lateness += time
        
class Car:
    def __init__(self):
        self.arrived_at = -1
        self.started_at = -1
        self.finished_at = -1
        
    def arrive(self, time):
        self.arrived_at = time
    
    def start(self, time):
        self.started_at = time
        
    def finish(self, time):
        self.finished_at = time
        
def create_data(events, k):
    users = {}
    cars = {}
    for event in events:
        if event[0] == 'ordered':
            if event[2] not in users:
                users[event[2]] = User(event[1], int(event[3]), int(event[4]), int(event[5]), k)
            else:
                users[event[2]].ordered(event[1], int(event[3]), int(event[4]), int(event[5]), k)
        elif event[0] == 'arrived':
            if event[1] not in cars:
                cars[event[1]] = Car()
                cars[event[1]].arrive(int(event[2]))
            else:
                cars[event[1]].arrive(int(event[2]))
        elif event[0] == 'started':
            if event[1] not in cars:
                cars[event[1]] = Car()
                cars[event[1]].start(int(event[2]))
            else:
                cars[event[1]].start(int(event[2]))
        else:
            if event[1] not in cars:
                cars[event[1]] = Car()
                cars[event[1]].finish(int(event[2]))
            else:
                cars[event[1]].finish(int(event[2]))
    return users, cars

def passengers(events, n, k):
    users, cars = create_data(events, k)              
    for user in users.values():
        for car_id, expected_finish in user.orders.items():
            try:
                car = cars[car_id]
                if expected_finish < car.finished_at and \
                        car.started_at >= 0 and \
                        car.arrived_at >= 0 and \
                        car.started_at - car.arrived_at <= k*60:
                    user.late(car.finished_at - expected_finish)
            except:
                continue
                    
    lateness_user = [(user.sum_lateness, name) for name, user in users.items()]
    lateness_user.sort(key = lambda x: (-x[0], x[1]))
    answer = []
    for lateness, name in lateness_user:
        if lateness > 0 and n > 0:
            answer.append(name)
            n -= 1
        else:
            break
    return answer



def main():
    x = int(input())
    answers = []
    for _ in range(x):
        n_events, n, k = map(int, input().split())
        events = []
        for _ in range(n_events):
            events.append(input().split())
        answers.append(passengers(events, n, k))
    for ans in answers:
        if not ans:
            print('-')
        else:
            print(" ".join(ans))
        
        
if __name__ == "__main__":
    main()