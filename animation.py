import numpy as np
import time
# import numba
import random as rand
import math
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

import sys
import copy

from mpl_toolkits.mplot3d import Axes3D

start_time = time.time()

"""
Information for entry of each array

customer_list= [  0   ,    1    ,   2  ,   3  ,     4     ,     5    ,     6    ,    7    ,    8    ]
customer_list= [is_inh, is_chope, is_lf, is_ls, is_seating, wait_seat, wait_food, eat_time, time_inh]

---
seat_list = [    0   ,     1    ]
seat_list = [is_taken, seat_time]
"""

looking_for_seat_ls=[]
inflow=0

# @numba.jit
def seat_taken(seats):
    num_seat_taken = 0
    for seat in seats:
        if seat[0] == 1:
            num_seat_taken += 1
    crowdedness = num_seat_taken / len(seats)
    return num_seat_taken, crowdedness


# @numba.jit
def get_status(customers):
    num_queue = 0
    num_look_seat = 0
    num_eating = 0
    num_in_hawker = 0

    for customer in customers:
        if customer[0] == 1:
            num_in_hawker += 1
            if customer[2] == 1:
                num_queue += 1
            elif customer[2] == 2:
                num_look_seat += 1
            elif customer[2] == 3:
                num_eating += 1
    return num_queue, num_look_seat, num_eating, num_in_hawker


def initialize_parameters(hyperparams):
    customer_list = np.zeros((hyperparams[0], 8))
    for i in range(hyperparams[0]):
        customer_list[i][7]=i
    seat_list = np.zeros((hyperparams[1], 2))
    inflow_rate = hyperparams[2]
    feed_time = hyperparams[3]
    num_stalls = hyperparams[4]
    prepare_food_time = hyperparams[5]
    return customer_list, seat_list, inflow_rate, feed_time, num_stalls, prepare_food_time


# @numba.jit
def update_hawker_status(customers, seats, feed_time, t):
    leaving_customers = []
    for person in range(0, len(customers)):

        ###update value of counter for consumer in hawker(looking for seat, eating time, and looking for food)
        if customers[person][0] == 1:
            if customers[person][2] == 2:  # for customer looking for seat, increase looking seat time counter
                customers[person][3] += 1
            if customers[person][2] == 3:  # for customer seating, reduce eating time so we can kick them later
                customers[person][5] -= 1
            if customers[person][2] == 1:  # for customer looking for food (queue), reduce queue time
                customers[person][4] -= 1

        ###once a customer finish queueing
        if customers[person][0] == 1 and customers[person][2] == 1 and customers[person][4] == 0:
            customers[person][2] = 0
            if customers[person][1] == 0:  # if they non_chopper, they will look for seat
                customers[person][2] = 2
                looking_for_seat_ls.append(customers[person])
            elif customers[person][1] == 1:  # if they chopper, they sit down
                customers[person][2] = 3
                customers[person][5] = feed_time

        ###if a customer is sitting and has finished eating, remove them
        if customers[person][0] == 1 and customers[person][2] == 3 and customers[person][5] == 0:
            leaving_customers.append([customers[person][3], customers[person][6], t])
            customers[person][0] = 3

    ###update seat status
    for seat in range(0, len(seats)):
        if seats[seat][0] == 1:  # if seat is occupied, subtract occupied time by one
            seats[seat][1] -= 1
        if seats[seat][1] == 0:  # when counter reach zero, seat is empty
            seats[seat][0] = 0
    return customers, seats, leaving_customers


# @numba.jit
def add_customer(customers, chop_prob, inflow_rate_prob, num_queue, num_stalls, prepare_food_time, crowdedness, t):
    global inflow
    inflow_rate = rand.randint(0, inflow_rate_prob)
    inflow+=inflow_rate
    # print('inflow',inflow_rate)
    for rate in range(0, inflow_rate):
        for people in range(0, len(customers)):
            ###randomiser for choping probability
            randomiser = rand.random() * 100
            if customers[people][0] == 0:
                customers[people][0] = 1
                if randomiser < chop_prob:
                    customers[people][1] = 1
                    customers[people][2] = 2
                    looking_for_seat_ls.append(customers[people])
                else:
                    customers[people][1] = 0
                    customers[people][2] = 1
                    customers[people][4] = prepare_food_time * math.floor(1 + num_queue / num_stalls)
                    customers[people][6] = prepare_food_time * math.floor(1 + num_queue / num_stalls)
                    num_queue += 1
                break

    return customers


# @numba.jit
def assign_seat(customers, seats, num_look_seat, num_look_food, feed_time, num_stalls, prepare_food_time):
    # check for all seats
    counter = 0
    for seat in range(0, len(seats)):

        # check for all empty seats
        if seats[seat][0] == 0:
            if len(looking_for_seat_ls) != 0:
                people = looking_for_seat_ls.pop(0)
                # print('p',people)
                if people[1] == 1:
                    people[2] = 1
                    people[4] = prepare_food_time * math.floor(1 + num_look_food / num_stalls)
                    people[6] = prepare_food_time * math.floor(1 + num_look_food / num_stalls)
                    seats[seat][0] = 1
                    seats[seat][1] = feed_time + prepare_food_time * math.floor(1 + num_look_food / num_stalls)
                    print('seat time',seats[seat][1])
                    num_look_food += 1

                else:
                    people[2] = 3
                    people[5] = feed_time

                    seats[seat][0] = 1
                    seats[seat][1] = feed_time

            ###run only for all looking for seats
            # while counter < num_look_seat:
            #
            #     randomiser = rand.randint(0, len(customers) - 1)  # change distribution?
            #
            #     ###update status from look_seat to look_food for choper (random)
            #     if customers[randomiser][0] == 1 and customers[randomiser][2] == 2 and customers[randomiser][1] == 1:
            #         customers[randomiser][2] = 1
            #         customers[randomiser][4] = prepare_food_time * math.floor(1 + num_look_food / num_stalls)
            #         customers[randomiser][6] = prepare_food_time * math.floor(1 + num_look_food / num_stalls)
            #
            #         seats[seat][0] = 1
            #         seats[seat][1] = feed_time + prepare_food_time * math.floor(1 + num_look_food / num_stalls)
            #         counter += 1
            #
            #         num_look_food += 1
            #         break
            #
            #     ###update status from look_seat to eat for non-choper (random)
            #     if customers[randomiser][0] == 1 and customers[randomiser][2] == 2 and customers[randomiser][1] == 0:
            #         customers[randomiser][2] = 3
            #         customers[randomiser][5] = feed_time
            #
            #         seats[seat][0] = 1
            #         seats[seat][1] = feed_time
            #         counter += 1
            #         break
    return customers, seats



def variable_prob(stalls):
    fig = plt.figure()

    # initialise all parameters and hyperparameters
    g_counter = 0
    repeat = 3
    prob_step = 10

    chop_probs = [np.round(x, 5) for x in np.arange(0, 100 + prob_step, prob_step)]
    chop_probs = np.repeat(chop_probs, repeat)
    running_average = 20
    simulation_length = 500
    critical_time = 100

    max_custs = 4000
    # hyperparameters = [[max_custs, 70, 4, 25, stalls, 1], [max_custs, 70, 5, 25, stalls, 1], [max_custs, 70, 6, 25, stalls, 1],
    #                    [max_custs, 60, 4, 25, stalls, 1], [max_custs, 60, 5, 25, stalls, 1], [max_custs, 60, 6, 25, stalls, 1]]
    # hyperparameters = [[max_custs,40,4,25,2,1],[max_custs,50,4,25,2,1],[max_custs,70,4,25,2,1]]
    hyperparameters = [[4000, 130, 7, 25, 5, 1]]
    # hyperparameters = [[1500,60,1,25,2,1],[1500,60,2,25,2,1],[1500,60,3,25,2,1],[1500,60,4,25,2,1],[1500,60,5,25,2,1],[1500,60,6,25,2,1]]

    for hyperparam in hyperparameters:
        _, _, inflow_rate, feed_time, num_stalls, prepare_food_time = initialize_parameters(hyperparam)

        result_data = []
        satisfaction_data = []

        customers, seats, _, _, _, _ = initialize_parameters(hyperparam)

        outflow_data = []
        prob_data = []


        for t in range(simulation_length):
            plt.clf()
            f1 = plt.subplot(111)
            f1.plot([0.3,0.3],[0,1])
            f1.plot([0.6,0.6],[0,1])
            f1.plot([1,1],[0,1])
            f1.plot([0,0],[0,1])
            # ax = fig.add_subplot(111)
            # rect1 = plt.Rectangle((0, 0), 0.4, 1, color='#00ffff')
            # rect2 = plt.Rectangle((0.4, 0), 0.2, 1, color='#ff6666')
            # rect3 = plt.Rectangle((0.6, 0), 0.4, 1, color='#66ff33')
            # stall1 = plt.Circle((0.1, 0.9), 0.05, color='black')
            # stall2 = plt.Circle((0.3, 0.9), 0.05, color='black')
            # ax.add_patch(rect1)
            # ax.add_patch(rect2)
            # ax.add_patch(rect3)
            # ax.add_patch(stall1)
            # ax.add_patch(stall2)
            f1.axis('off')

            queue_list_x = []
            queue_list_y = []
            lookseat_list_x=[]
            lookseat_list_y=[]
            eating_list_x=[]
            eating_list_y=[]
            count_queue = 0
            count_lookforseat=0

            num_seat_taken, crowdedness = seat_taken(seats)
            # num_queue, num_look_seat, num_eating, num_in_hawker = get_status(customers)

            num_queue, num_look_seat, num_eating, num_in_hawker = get_status(customers)

            chop_prob = math.exp(12*crowdedness-6)/(1 + math.exp(12*crowdedness-6))*100
            # chop_prob = 4* crowdedness* (1-crowdedness)*100
            # chop_prob = 5

            if num_in_hawker < len(customers):
                customers = add_customer(customers, chop_prob, inflow_rate, num_queue, num_stalls, prepare_food_time,
                                         crowdedness, t)
            customers, seats, leaving_customers = update_hawker_status(customers, seats, feed_time, t)
            # print(leaving_customers)

            num_queue, num_look_seat, num_eating, num_in_hawker = get_status(customers)
            customers, seats = assign_seat(customers, seats, num_look_seat, num_queue, feed_time, num_stalls,
                                           prepare_food_time)
            for i in range(num_queue):
                queue_list_y.append(-i*0.01+1)
                if count_queue%3==0:
                    queue_list_x.append(0.05)
                elif count_queue%3==1:
                    queue_list_x.append(0.15)
                else:
                    queue_list_x.append(0.25)
                count_queue+=1
            # print(queue_list_x,queue_list_y)
            p1=f1.scatter(queue_list_x,queue_list_y,c='r', marker='s', s=10)

            for i in range(num_look_seat):
                lookseat_list_y.append(1-i*0.01)
                if count_lookforseat%3==0:
                    lookseat_list_x.append(0.35)
                elif count_lookforseat%3==1:
                    lookseat_list_x.append(0.45)
                else:
                    lookseat_list_x.append(0.55)
                count_lookforseat+=1
            p2=f1.scatter(lookseat_list_x,lookseat_list_y,c='g', marker='o', s=10)

            print('seat taken:',num_seat_taken)
            for i in range(num_seat_taken):
                eating_list_x.append(0.9-0.1*(i%3))
                eating_list_y.append(1-0.03*(i//3))
            p3=f1.scatter(eating_list_x, eating_list_y, c='b', marker='x', s=10)

            # if t >= critical_time:
            prob_data.append(chop_prob)
            outflow_data.append(len(leaving_customers))
            plt.text(0.08,-0.15,'number of people\n waiting to order is {}'.format(int(num_queue)))
            plt.text(0.35,-0.15,'number of people\n looking for a seat is {}'.format(int(num_look_seat)))
            plt.legend([p1,p2,p3],['queue for ordering','looking for a seat','eating'],bbox_to_anchor=(0.4, 1))
            plt.pause(0.05)
        # print('total',inflow)
        plt.ioff()
        plt.show()

        g_counter += 1


variable_prob(3)
# print(time.time() - start_time)




