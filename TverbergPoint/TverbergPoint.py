from utils.GeoUtils import *


class TverbergPoint:
    """
    Compute Tverberg point for 2D dimension.
    """

    def __init__(self):
        self.point_set = None

    def getTvbPoint(self, point_set):
        self.point_set = point_set
        sorted_point_set = sorted(self.point_set, key=lambda p: p.x)
        sorted_index = [i[0] for i in sorted(enumerate(self.point_set), key=lambda p: p[1].x)]
        size = len(self.point_set)
        tver_pairs = []
        for i in range(0, math.floor(size / 2)):
            tver_pairs.append([sorted_index[i], sorted_index[size - i - 1]])
        if size % 2 == 1:
            tver_pairs.append(sorted_index[math.floor(size / 2)])
        tverp_x = np.median([p.x for p in point_set])
        y_values = []
        for i in range(0, len(tver_pairs)):
            if isinstance(tver_pairs[i],int):
                y_values.append(self.point_set[tver_pairs[i]].y)
            else:
                if point_set[tver_pairs[i][0]].x == self.point_set[tver_pairs[i][1]].x:
                    y_values.append(np.mean(self.point_set[tver_pairs[i][0]].y, self.point_set[tver_pairs[i][1]].y))
                else:
                    l = line_over_two_points(self.point_set[tver_pairs[i][0]], self.point_set[tver_pairs[i][1]])
                    y_values.append(l.m * tverp_x + l.b)
        tverp_y =  np.median(y_values)
        return Point(tverp_x, tverp_y)


if __name__ == '__main__':
    random.seed(1)
    num = 11
    point_set = []
    plot = True
    for i in range(num):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        point_set.append(Point(x, y))

    Tverp = TverbergPoint()
    tvp = Tverp.getTvbPoint(point_set)
    print(tvp.x, tvp.y)

    if plot:
        plt.clf()
        x_min, x_max = find_x_bounds(point_set)
        interval = Interval(x_min - 10, x_max + 10)
        y_min, y_max = find_y_bounds(point_set)
        prepare_axis(interval.l - 5, interval.r + 5, y_min - 5, y_max + 5)
        plot_point_set(point_set, color='r')
        plot_point(tvp, color='g')
        plt.pause(1)
        end = input('Press enter to the next step.')
