import numpy as np

from Scripts.NumpyArrayUtilities import sample_from_array


class CreateTrainingBatches(object):
    def __init__(self, x_train, y_train, x_valid, y_valid):
        self.x_train = x_train
        self.y_train = y_train
        self.x_valid = x_valid
        self.y_valid = y_valid

    @staticmethod
    def create_data(x, y, num_pos, num_neg):
        x = np.asarray(x)
        y = np.squeeze(np.asarray(y))

        pos_x = x[y == 1]
        neg_x = x[y == 0]

        pos_x_samples = sample_from_array(pos_x, num_pos, num_rows=True)
        pos_y_samples = np.asarray([1] * num_pos)

        neg_x_samples = sample_from_array(neg_x, num_neg, num_rows=True)
        neg_y_samples = np.asarray([0] * num_neg)

        x_samples = np.vstack((pos_x_samples, neg_x_samples))
        y_samples = np.hstack((pos_y_samples, neg_y_samples)).T.reshape(-1, 1)
        return x_samples, y_samples

    def create_training_data(self, num_pos=256, num_neg=256):
        x_train_samples, y_train_samples = self.create_data(self.x_train, self.y_train, num_pos, num_neg)
        return x_train_samples, y_train_samples

    def create_validation_data(self, num_pos=256, num_neg=256):
        x_valid_samples, y_valid_samples = self.create_data(self.x_valid, self.y_valid, num_pos, num_neg)
        return x_valid_samples, y_valid_samples
