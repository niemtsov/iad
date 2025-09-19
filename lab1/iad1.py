import numpy as np

def euclidean_distance(x, y):
    # евклідова відстань між двома векторами
    return np.sqrt(np.sum((x - y) ** 2))

def build_distance_matrix(clusters):
    # матриця відстаней між усіма кластерами
    n = len(clusters)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            d = min(euclidean_distance(a, b) for a in clusters[i] for b in clusters[j])
            dist_matrix[i, j] = d
            dist_matrix[j, i] = d
    return dist_matrix

def format_cluster(cluster):
    # форматуємо кластер для нормального виведення
    return "{" + ", ".join(f"({p[0]:.0f}, {p[1]:.0f})" for p in cluster) + "}"

def hierarchical_clustering(data):
    clusters = [[point] for point in data]
    dist_matrix = build_distance_matrix(clusters)
    step = 1

    while len(clusters) > 1:
        n = len(clusters)
        # знаходження двох найближчих кластерів
        np.fill_diagonal(dist_matrix, np.inf)
        p, q = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
        print(f"\nКрок {step}. об'єднуємо кластери {p} і {q} (відстань = {dist_matrix[p, q]:.3f})")

        # об'єднуємо кластери
        new_cluster = clusters[p] + clusters[q]

        # оновляємо список кластерів
        new_clusters = [clusters[k] for k in range(n) if k not in (p, q)]
        new_clusters.append(new_cluster)
        
        # оновляємо матрицю відстаней
        new_n = len(new_clusters)
        new_dist = np.zeros((new_n, new_n))
        mask = [k for k in range(n) if k not in (p, q)]
        for i in range(len(mask)):
            for j in range(i+1, len(mask)):
                new_dist[i, j] = dist_matrix[mask[i], mask[j]]
                new_dist[j, i] = new_dist[i, j]
        for s in range(len(mask)):
            dps = dist_matrix[p, mask[s]]
            dqs = dist_matrix[q, mask[s]]
            drs = (dps + dqs) / 2
            new_dist[s, new_n-1] = drs
            new_dist[new_n-1, s] = drs
        clusters = new_clusters
        dist_matrix = new_dist

        # друк кластерів
        print("кластери:")
        for idx, cl in enumerate(clusters):
            print(f"  {idx}: {format_cluster(cl)}")

        # друк матриці відстаней
        print("Матриця відстаней:")
        for row in dist_matrix:
            print("  ", [f"{x:.2f}" for x in row])
        step += 1

T = np.array([
    [1.0, 2.0],
    [2.0, 1.0],
    [5.0, 4.0],
    [6.0, 5.0]
])

hierarchical_clustering(T)
