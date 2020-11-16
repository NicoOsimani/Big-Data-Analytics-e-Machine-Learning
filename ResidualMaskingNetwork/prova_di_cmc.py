import matplotlib.pyplot as plt
import numpy as np

from utils.CMC import CMC


def plot_cmc(values, title, ranks):

    value1 = []
    value2 = []
    value3 = []
    value4 = []
    value5 = []
    
    rank = ranks
    
    value1.append(values[1])
    value2.append(values[2])
    value3.append(values[3])
    value4.append(values[4])
    value5.append(values[5])
    
    new_color = ['w', 'r', 'w', 'w', 'w', 'w']
    new_marker = ['', '*', '', '', '', '']
    
    cmc_dict = {
        "at Rank 1" : values,
        "at Rank 2" : value1,
        "at Rank 3" : value2,
        "at Rank 4" : value3,
        "at Rank 5" : value4,
        "at Rank 6" : value5
    }
    
    cmc = CMC(cmc_dict, color = new_color, marker = new_marker)
    
    fig = cmc.plot(title = title, rank = rank)
    
    fig.savefig("./saved/cmc/cmc.png")
    plt.show()
    plt.close(fig)
    

def cmc_values(all_target, all_prob_matrix):
    rank_matrix = []
    num_classes = int(len(all_prob_matrix[0]))
    rank = np.zeros(shape=(num_classes, 3))

    for i in range(len(all_prob_matrix)):

        trueClass = all_target[i]

        for j in range(0, num_classes):
            rank[j][0] = j
            rank[j][1] = all_prob_matrix[i][j]
            rank[j][2] = trueClass

        rankO = rank[np.argsort(-rank[:, 1])]

        sortedClass = []
        for j in range(num_classes):
            sortedClass.append(int(rankO[j][0]))

        sortedClass.append(int(rankO[0][2]))
        rank_matrix.insert(i, sortedClass)

    count = np.zeros(shape=num_classes)

    for i in range(len(rank_matrix)):
        trueClass = rank_matrix[i][num_classes]
        for j in range(num_classes):
            if trueClass == rank_matrix[i][j]:
                count[j] += 1
                break

    score = 0
    values = []
    for i in range(0, len(count)):
        score = score + float(count[i]) / float(len(rank_matrix))
        values.append(score)

    return values


def main():

    class_names = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

    all_target = [0, 1, 2]
    all_prob_matrix = np.array([[7, 6, 5, 4, 3, 2, 1], [1, 7, 6, 5, 4, 3, 2], [2, 1, 6, 7, 5, 4, 3]])

    values = cmc_values(all_target, all_prob_matrix)
    plot_cmc(values, "CMC", len(class_names))


if __name__ == "__main__":
    main()
