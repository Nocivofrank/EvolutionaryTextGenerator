import numpy as np
import secrets

class Brain():

    #brian row and columns
    input_size = 100

    hidden_size = 20000
    hidden2_size = 4000
    hidden3_size = 4000
    hidden4_size = 2000
    hidden5_size = 400
    hidden6_size = 200
    output_size = 97

    
    def __init__(self, id):
        # weights and biases
        #for input size
        self.W1 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.input_size)] for _ in range(Brain.hidden_size)])
        self.W1_prev = self.W1

        self.b1 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden_size)])
        self.b1_prev = self.b1

        #for hidden 1
        self.W2 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden_size)] for _ in range(Brain.hidden2_size)])
        self.W2_prev = self.W2

        self.b2 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden2_size)])
        self.b2_prev = self.b2

        #for hidden 2
        self.W3 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden2_size)] for _ in range(Brain.hidden3_size)])
        self.W3_prev = self.W3

        self.b3 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden3_size)])
        self.b3_prev = self.b3

        #for hidden 3
        self.W4 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden3_size)] for _ in range(Brain.hidden4_size)])
        self.W4_prev = self.W4

        self.b4 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden4_size)])
        self.b4_prev = self.b4

        #for hidden 4
        self.W5 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden4_size)] for _ in range(Brain.hidden5_size)])
        self.W5_prev = self.W5

        self.b5 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden5_size)])
        self.b5_prev = self.b5

        #for hidden 5
        self.W6 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden5_size)] for _ in range(Brain.hidden6_size)])
        self.W6_prev = self.W6

        self.b6 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.hidden6_size)])
        self.b6_prev = self.b6

        #for output
        self.W7 = np.array([[Brain.random_range(-1, 1) for _ in range(Brain.hidden6_size)] for _ in range(Brain.output_size)])
        self.W7_prev = self.W7

        self.b7 = np.array([Brain.random_range(-1, 1) for _ in range(Brain.output_size)])
        self.b7_prev = self.b7

        self.information = np.zeros(Brain.input_size)
        self.id = id
        self.prev_token = 0

    def sigmoid(x):
        out = np.empty_like(x, dtype=float)

        pos_mask = x >= 0
        neg_mask = ~pos_mask

        # safe for positive x
        out[pos_mask] = 1 / (1 + np.exp(-x[pos_mask]))

        # safe for negative x
        ex = np.exp(x[neg_mask])
        out[neg_mask] = ex / (1 + ex)

        return out


    def brainThink(self):
        # Layer 1
        z1 = np.dot(self.W1, self.information) + self.b1
        h1 = Brain.sigmoid(z1)

        # Layer 2
        z2 = np.dot(self.W2, h1) + self.b2
        h2 = Brain.sigmoid(z2)

        # Layer 3
        z3 = np.dot(self.W3, h2) + self.b3
        h3 = Brain.sigmoid(z3)

        # Layer 4
        z4 = np.dot(self.W4, h3) + self.b4
        h4 = Brain.sigmoid(z4)

        # Layer 5
        z5 = np.dot(self.W5, h4) + self.b5
        h5 = Brain.sigmoid(z5)

        # Layer 6
        z6 = np.dot(self.W6, h5) + self.b6
        h6 = Brain.sigmoid(z6)

        #output layer
        z7 = np.dot(self.W7, h6) + self.b7
        out = Brain.sigmoid(z7)

        # z5 = np.dot(self.W4, h3) + self.b4
        # action = Brain.sigmoid(z5)

        return out#mn , action

    def brainMutate(self, chance=0.5, super_chance=0.1, strength=0.5, super_strength=0.7):
        print(f"Brain {self.id} mutating")
        layers = [self.W1, self.b1, self.W2, self.b2, self.W3, self.b3, self.W4, self.b4, self.W5, self.b5, self.W6, self.b6, self.W7, self.b7]

        self.W1_prev = self.W1
        self.b1_prev = self.b1
        self.W2_prev = self.W2
        self.b2_prev = self.b2
        self.W3_prev = self.W3
        self.b3_prev = self.b3
        self.W4_prev = self.W4
        self.b4_prev = self.b4
        self.W5_prev = self.W5
        self.b5_prev = self.b5
        self.W6_prev = self.W6
        self.b6_prev = self.b6
        self.W7_prev = self.W7
        self.b7_prev = self.b7

        for layer in layers:
            # Normal mutation mask
            mask = np.random.rand(*layer.shape) < chance
            
            # Super mutation mask
            super_mask = np.random.rand(*layer.shape) < super_chance

            # Normal mutation
            mutation = np.random.uniform(-strength, strength, layer.shape)
            layer += mask * mutation

            # Super mutation overrides normal one
            mutation_super = np.random.uniform(-super_strength, super_strength, layer.shape)
            layer += super_mask * mutation_super

    def revertToPreviousBrain(self):
        self.W1 = self.W1_prev
        self.b1 = self.b1_prev
        self.W2 = self.W2_prev
        self.b2 = self.b2_prev
        self.W3 = self.W3_prev
        self.b3 = self.b3_prev
        self.W4 = self.W4_prev
        self.b4 = self.b4_prev
        self.W5 = self.W5_prev
        self.b5 = self.b5_prev
        self.W6 = self.W6_prev
        self.b6 = self.b6_prev
        self.W7 = self.W7_prev
        self.b7 = self.b7_prev

    def random_range(a, b):
        return a + (b - a) * (secrets.randbits(52) / (1 << 52))