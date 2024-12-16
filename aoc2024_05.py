import numpy as np
import math

count = 0
rules = []
updates = []
with open("input5.txt") as input:
    for number, line in enumerate(input):
        line = line.replace('\n','')
        if '|' in line:
            count += 1
        if number < 1176:
            rules.append([int(x) for x in line.split('|')])
        elif number > 1176:
            updates.append([int(x) for x in line.split(',')])

good_updates = []
bad_updates = []
for update in updates:
    rule_count = 0
    rule_correct = 0
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            rule_count += 1
            if update.index(rule[0]) < update.index(rule[1]):
                rule_correct += 1
    if rule_count == rule_correct:
        good_updates.append(update)
    else:
        bad_updates.append(update)

result = sum([update[len(update) // 2] for update in good_updates])
print(result)

corrected_updates = []
for bupdate in bad_updates:
    relevent_rules = []
    for rule in rules:
        if rule[0] in bupdate and rule[1] in bupdate:
            relevent_rules.append(rule)
    corrected_update = []
    update = bupdate.copy()
    for i in range(len(bupdate)):
        upper = set([rule[1] for rule in relevent_rules])
        difference = list(set(update).difference(upper))
        corrected_update.append(difference[0])
        relevent_rules = [x for x in relevent_rules if x[0] != corrected_update[-1]]
        update.remove(corrected_update[-1])
    corrected_updates.append(corrected_update.copy())

result1 = sum([update[len(update) // 2] for update in corrected_updates])
print(result1)
