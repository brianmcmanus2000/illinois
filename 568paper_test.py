import random

def run_sim(p_flip : float, p_true : float, num_trials: int):
    count = 0
    for _ in range(num_trials):
        label = random.random()
        flip_prob = random.random()
        flip = False
        if label<p_true:
            flip = True
        if flip_prob<p_flip:
            flip = not flip
        if flip:
            count = count+1
    return count/num_trials, (num_trials-count)/num_trials

def correction(p_flip : float, true_prop: float, false_prop : float):
    true_adj = true_prop-p_flip
    false_adj = false_prop-p_flip
    scaling_factor = 1/(true_adj+false_adj)
    return true_adj*scaling_factor,false_adj*scaling_factor

p_flip=0.25
p_true=0.8
num_trials=1000000
true_prop,false_prop = run_sim(p_flip,p_true,num_trials)
print(f"proportion of true labels: {true_prop}, falses: {false_prop}")
true_adj,falase_adj = correction(p_flip, true_prop, false_prop)
print(f"corrected proportion of true labels: {true_adj}, falses: {falase_adj}")
